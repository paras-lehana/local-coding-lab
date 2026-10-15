"""Independent SQLite contract checks; run only inside the grading sandbox."""
import json
from pathlib import Path
import re
import sqlite3


def transaction_encloses_writes(statements: list[str]) -> bool:
    """Check SQLite trace statements, allowing comments before real SQL."""
    normalized = [re.sub(r'\A(?:\s|--[^\n]*(?:\n|$)|/\*.*?\*/)*', '',
                         statement, flags=re.S).upper()
                  for statement in statements]
    begin = next((i for i, sql in enumerate(normalized)
                  if re.match(r'BEGIN\b', sql)), -1)
    commit = next((i for i, sql in enumerate(normalized)
                   if re.match(r'(?:COMMIT|END)\b', sql)), -1)
    writes = [i for i, sql in enumerate(normalized)
              if re.match(r'(?:CREATE\s+TABLE|DROP\s+TABLE|ALTER\s+TABLE|'
                          r'INSERT\s+INTO|UPDATE\b|DELETE\s+FROM)', sql)]
    return bool(writes) and begin >= 0 and all(begin < i < commit for i in writes)


def main() -> int:
    """Exercise migration preservation and the new constraints independently."""
    db = sqlite3.connect(':memory:')
    db.executescript(Path('/work/schema.sql').read_text())
    db.executescript("""
        INSERT INTO jobs VALUES(1,'alpha','shared','payload-one',3);
        INSERT INTO jobs VALUES(2,'beta','other','payload-two',NULL);
        INSERT INTO job_events VALUES(10,1,'event-one');
        INSERT INTO job_events VALUES(20,2,'event-two');
    """)
    trace = []
    db.set_trace_callback(trace.append)
    try:
        db.executescript(Path('/work/migration.sql').read_text())
    except sqlite3.Error as error:
        print(json.dumps({'migration_error': str(error), 'passed': 0, 'total': 6}))
        return 1
    migration_trace = list(trace)
    results = []

    def check(name, body):
        try:
            body()
            results.append({'name': name, 'passed': True})
        except (AssertionError, StopIteration, sqlite3.Error) as error:
            results.append({'name': name, 'passed': False, 'error': str(error)})

    def preservation():
        assert db.execute('SELECT id,tenant_id,external_id,payload,attempts FROM jobs ORDER BY id').fetchall() == [
            (1, 'alpha', 'shared', 'payload-one', 3),
            (2, 'beta', 'other', 'payload-two', 0)]
        assert db.execute('SELECT * FROM job_events ORDER BY id').fetchall() == [
            (10, 1, 'event-one'), (20, 2, 'event-two')]

    def foreign_keys():
        assert db.execute('PRAGMA foreign_keys').fetchone()[0] == 1
        assert db.execute('PRAGMA foreign_key_check').fetchall() == []
        keys = db.execute('PRAGMA foreign_key_list(job_events)').fetchall()
        assert any(row[2:5] == ('jobs', 'job_id', 'id') for row in keys)

    def expect_rejected(sql):
        try:
            db.execute(sql)
        except sqlite3.IntegrityError:
            return
        raise AssertionError('Invalid record was accepted')

    def uniqueness():
        # Use fresh rows so earlier data loss does not masquerade as a missing
        # uniqueness constraint. Preservation is already its own check.
        db.execute("INSERT INTO jobs VALUES(1001,'check-a','check-key','one',0)")
        db.execute("INSERT INTO jobs VALUES(1002,'check-b','check-key','two',0)")
        expect_rejected("INSERT INTO jobs VALUES(1003,'check-a','check-key','three',0)")

    def attempts():
        db.execute("INSERT INTO jobs(id,tenant_id,external_id,payload) VALUES(5,'a','default','five')")
        assert db.execute('SELECT attempts FROM jobs WHERE id=5').fetchone()[0] == 0
        expect_rejected("INSERT INTO jobs VALUES(6,'a','null','six',NULL)")
        expect_rejected("INSERT INTO jobs VALUES(7,'a','negative','seven',-1)")
        info = {r[1]: r for r in db.execute('PRAGMA table_info(jobs)')}
        assert info['attempts'][2].upper() == 'INTEGER'
        assert info['attempts'][3] == 1

    def references():
        # A referenced row must exist even if the migration lost original data.
        db.execute("INSERT INTO jobs VALUES(1005,'check-c','check-parent','parent',0)")
        db.execute("INSERT INTO job_events VALUES(1006,1005,'check-event')")
        expect_rejected("INSERT INTO job_events VALUES(30,999,'orphan')")
        expect_rejected('DELETE FROM jobs WHERE id=1005')

    def transaction():
        assert transaction_encloses_writes(migration_trace)

    for name, body in [('data and event preservation', preservation),
                       ('foreign key restoration', foreign_keys),
                       ('tenant-scoped uniqueness', uniqueness),
                       ('attempt constraints and default', attempts),
                       ('referential integrity enforcement', references),
                       ('migration transaction', transaction)]:
        check(name, body)
    print(json.dumps({'groups': results, 'passed': sum(r['passed'] for r in results),
                      'total': len(results)}))
    return 0 if all(r['passed'] for r in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
