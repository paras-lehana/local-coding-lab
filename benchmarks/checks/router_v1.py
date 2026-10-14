"""Human-authored router-v1 checks. Run only inside the grading sandbox."""
import copy
import unittest

from candidate import merge_config


def mutable_ids(value):
    """Collect mutable objects reachable through JSON-like containers."""
    found = set()
    pending = [value]
    while pending:
        item = pending.pop()
        if isinstance(item, (dict, list)) and id(item) not in found:
            found.add(id(item))
            pending.extend(item.values() if isinstance(item, dict) else item)
    return found


class ContractTests(unittest.TestCase):
    """Six rubric groups, worth 2+2+2+3+1+2 points respectively."""

    def test_nested_defaults_and_unknown_keys(self):
        defaults = {'a': {'b': {'keep': 1, 'replace': 2}}, 'keep': [3]}
        overrides = {'a': {'b': {'replace': 4, 'new': 5}}, 'new': {'x': [6]}}
        expected = {'a': {'b': {'keep': 1, 'replace': 4, 'new': 5}},
                    'keep': [3], 'new': {'x': [6]}}
        self.assertEqual(merge_config(defaults, overrides), expected)
        self.assertEqual(merge_config({}, {'new': []}), {'new': []})
        self.assertEqual(merge_config({'keep': 7}, {}), {'keep': 7})

    def test_false_and_empty_values(self):
        for value in [False, None, 0, '', [], {}]:
            with self.subTest(value=value):
                result = merge_config({'x': 'old'}, {'x': value})
                self.assertEqual(result, {'x': value})
                self.assertIs(type(result['x']), type(value))
        # Both dictionaries recurse: an empty override preserves defaults.
        self.assertEqual(merge_config({'x': {'keep': 1}}, {'x': {}}),
                         {'x': {'keep': 1}})

    def test_dictionary_scalar_conflicts(self):
        for before, after in [({'a': 1}, None), ({'a': 1}, [2]),
                              ({'a': 1}, False), (3, {'b': [4]}),
                              ([1], {'b': 2}), ('old', 0)]:
            with self.subTest(before=before, after=after):
                self.assertEqual(merge_config({'x': before}, {'x': after}),
                                 {'x': after})

    def test_deep_mutable_isolation(self):
        defaults = {'keep': [{'d': [1]}], 'replace': [{'d': [2]}],
                    'nested': {'keep': [{'d': [3]}]}}
        overrides = {'replace': [{'o': [4]}], 'new': [{'o': [5]}],
                     'nested': {'new': [{'o': [6]}]}}
        originals = copy.deepcopy((defaults, overrides))
        result = merge_config(defaults, overrides)
        self.assertEqual((defaults, overrides), originals)
        self.assertTrue(mutable_ids(result).isdisjoint(mutable_ids(defaults)))
        self.assertTrue(mutable_ids(result).isdisjoint(mutable_ids(overrides)))
        result['keep'][0]['d'].append(99)
        result['replace'][0]['o'].append(99)
        result['nested']['new'][0]['o'].append(99)
        self.assertEqual((defaults, overrides), originals)

    def test_repeated_calls(self):
        defaults = {'a': [{'b': [1]}]}
        overrides = {'new': [{'c': [2]}]}
        first = merge_config(defaults, overrides)
        second = merge_config(defaults, overrides)
        self.assertTrue(mutable_ids(first).isdisjoint(mutable_ids(second)))
        first['new'][0]['c'].append(99)
        self.assertEqual(second, {'a': [{'b': [1]}], 'new': [{'c': [2]}]})

    def test_invalid_roots(self):
        for invalid in [None, [], (), 'text', 0, False]:
            for defaults, overrides in [(invalid, {}), ({}, invalid)]:
                with self.subTest(defaults=defaults, overrides=overrides):
                    with self.assertRaises(TypeError):
                        merge_config(defaults, overrides)


if __name__ == '__main__':
    unittest.main(verbosity=2)
