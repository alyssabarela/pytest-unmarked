from _pytest.mark import matchmark
import py


def pytest_addoption(parser):
    group = parser.getgroup('Unmarked', 'Unmarked')
    group._addoption('--unmarked',
                     action="store_true", dest="unmarked", default=False,
                     help="Run unmarked tests.")


def pytest_cmdline_main(config):
    if config.option.markers:
        config.do_configure()
        tw = py.io.TerminalWriter()
        for line in config.getini("markers"):
            name, rest = line.split(":", 1)
            tw.write("@pytest.mark.%s:" % name, bold=True)
            tw.line(rest)
            tw.line()
        config.do_unconfigure()
        return 0
pytest_cmdline_main.tryfirst = True


def pytest_collection_modifyitems(items, config):
    matchexpr = config.option.markers
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
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining
