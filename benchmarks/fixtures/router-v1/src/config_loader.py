"""Deliberately buggy synthetic fixture. Never import this as lab code."""


def merge_config(defaults, overrides):
    result = defaults.copy()
    for key, value in overrides.items():
        if key in result:
            if isinstance(result[key], dict):
                result[key].update(value)
            elif value:
                result[key] = value
    return result
