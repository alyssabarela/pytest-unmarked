from _pytest.mark import matchmark
import pytest
import py


def pytest_addoption(parser):
    group = parser.getgroup('Unmarked', 'Unmarked')
    group._addoption('--unmarked',
                     action="store_true", dest="unmarked", default=False,
                     help="Run unmarked tests.")


def pytest_collection_modifyitems(items, config):
    if (not pytest.config.option.unmarked):
        return

    names_list = []
    for line in config.getini("markers"):
        names, rest = line.split(":", 1)
        if '(' in names:
            names, rest = names.split("(", 1)

        names_list.append(names)

    matchexpr = ' or '.join(names_list)
    if not matchexpr:
        return

    remaining = []
    deselected = []
    for colitem in items:
        if matchexpr:
            if matchmark(colitem, matchexpr):
                deselected.append(colitem)
                continue
        remaining.append(colitem)

    if deselected:
        config.hook.pytest_deselected(items=list(set(deselected) - set(remaining)))
        items[:] = remaining
