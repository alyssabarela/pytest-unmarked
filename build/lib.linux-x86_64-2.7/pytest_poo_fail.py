import pytest

PILE_OF_POO = u"\U0001F4A9 "


def pytest_addoption(parser):
    group = parser.getgroup('Poo', 'Poo')
    group._addoption('--poo',
                     action="store_true", dest="poo", default=False,
                     help="Show crappy tests.")


def pytest_report_teststatus(report):
    if pytest.config.option.poo and report.failed:
        return (report.outcome, PILE_OF_POO, '%s (%s)' % (report.outcome.upper(), PILE_OF_POO))
