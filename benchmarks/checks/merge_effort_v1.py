"""Five predeclared merge-effort-v1 groups. Execute only in the isolated grader."""
import copy
import unittest

from candidate import merge


def mutable_ids(value):
    """Enumerate reachable mutable containers without conflating immutable IDs."""
    found = set()
    pending = [value]
    while pending:
        item = pending.pop()
        if isinstance(item, (dict, list)) and id(item) not in found:
            found.add(id(item))
            pending.extend(item.values() if isinstance(item, dict) else item)
    return found


class ContractTests(unittest.TestCase):
    """Adapt the existing router's first five groups to this simpler prompt."""

    def test_nested_defaults_and_unknown_keys(self):
        base = {'a': {'b': {'keep': 1, 'replace': 2}}, 'keep': [3]}
        patch = {'a': {'b': {'replace': 4, 'new': 5}}, 'new': {'x': [6]}}
        expected = {'a': {'b': {'keep': 1, 'replace': 4, 'new': 5}},
                    'keep': [3], 'new': {'x': [6]}}
        self.assertEqual(merge(base, patch), expected)
        self.assertEqual(merge({}, {'new': []}), {'new': []})
        self.assertEqual(merge({'keep': 7}, {}), {'keep': 7})

    def test_false_and_empty_values(self):
        for value in [False, None, 0, '', [], {}]:
            with self.subTest(value=value):
                result = merge({'x': 'old'}, {'x': value})
                self.assertEqual(result, {'x': value})
                self.assertIs(type(result['x']), type(value))
        self.assertEqual(merge({'x': {'keep': 1}}, {'x': {}}),
                         {'x': {'keep': 1}})

    def test_dictionary_scalar_conflicts(self):
        for before, after in [({'a': 1}, None), ({'a': 1}, [2]),
                              ({'a': 1}, False), (3, {'b': [4]}),
                              ([1], {'b': 2}), ('old', 0)]:
            with self.subTest(before=before, after=after):
                self.assertEqual(merge({'x': before}, {'x': after}), {'x': after})

    def test_deep_mutable_isolation(self):
        base = {'keep': [{'d': [1]}], 'replace': [{'d': [2]}],
                'nested': {'keep': [{'d': [3]}]}}
        patch = {'replace': [{'o': [4]}], 'new': [{'o': [5]}],
                 'nested': {'new': [{'o': [6]}]}}
        originals = copy.deepcopy((base, patch))
        result = merge(base, patch)
        self.assertEqual((base, patch), originals)
        self.assertTrue(mutable_ids(result).isdisjoint(mutable_ids(base)))
        self.assertTrue(mutable_ids(result).isdisjoint(mutable_ids(patch)))
        result['keep'][0]['d'].append(99)
        result['replace'][0]['o'].append(99)
        result['nested']['new'][0]['o'].append(99)
        self.assertEqual((base, patch), originals)

    def test_repeated_calls(self):
        base = {'a': [{'b': [1]}]}
        patch = {'new': [{'c': [2]}]}
        first = merge(base, patch)
        second = merge(base, patch)
        self.assertTrue(mutable_ids(first).isdisjoint(mutable_ids(second)))
        first['new'][0]['c'].append(99)
        self.assertEqual(second, {'a': [{'b': [1]}], 'new': [{'c': [2]}]})


if __name__ == '__main__':
    unittest.main(verbosity=2)
