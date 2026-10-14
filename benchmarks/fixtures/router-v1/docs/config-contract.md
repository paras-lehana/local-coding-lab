# Merge contract

merge_config(defaults, overrides) accepts dictionaries holding JSON-like data.
Recurse only when BOTH values at a key are dictionaries. Otherwise the override
replaces the default, including lists, False, None, 0, and empty containers.
Unspecified default keys and previously unknown override keys survive.
Neither argument may change. The result must share no mutable dict/list with
either argument, even under nested lists and even across repeated calls.
Do not silently replace a non-dictionary root argument: raise TypeError.
