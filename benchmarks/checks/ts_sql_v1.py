"""Independent SQLite contract checks; run only inside the grading sandbox."""
import json
from pathlib import Path
import sqlite3


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
        db.execute("INSERT INTO jobs VALUES(3,'beta','shared','three',0)")
        expect_rejected("INSERT INTO jobs VALUES(4,'alpha','shared','four',0)")

    def attempts():
        db.execute("INSERT INTO jobs(id,tenant_id,external_id,payload) VALUES(5,'a','default','five')")
        assert db.execute('SELECT attempts FROM jobs WHERE id=5').fetchone()[0] == 0
        expect_rejected("INSERT INTO jobs VALUES(6,'a','null','six',NULL)")
        expect_rejected("INSERT INTO jobs VALUES(7,'a','negative','seven',-1)")
        info = {r[1]: r for r in db.execute('PRAGMA table_info(jobs)')}
        assert info['attempts'][2].upper() == 'INTEGER'
        assert info['attempts'][3] == 1

    def references():
        expect_rejected("INSERT INTO job_events VALUES(30,999,'orphan')")
        expect_rejected('DELETE FROM jobs WHERE id=1')

    def transaction():
        normalized = [s.strip().upper() for s in migration_trace]
        begin = next(i for i, s in enumerate(normalized) if s.startswith('BEGIN'))
        commit = next(i for i, s in enumerate(normalized) if s.startswith(('COMMIT', 'END')))
        writes = [i for i, s in enumerate(normalized)
                  if any(word in s for word in ('CREATE TABLE', 'DROP TABLE', 'ALTER TABLE', 'INSERT INTO'))]
        assert writes and all(begin < i < commit for i in writes)

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
