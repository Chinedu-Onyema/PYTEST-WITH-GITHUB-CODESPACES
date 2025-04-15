from click.testing import CliRunner
from cli import make_change
from mlib.mchange import change

def test_change():
    assert [{5: "quarters"}, {1: 'nickels'}, {4: "pennies"}] == change(1.34)


def test_cli_change():
  runner = CliRunner()
  result = runner.invoke(make_change, ['--amount', "1.34"])
  assert result.exit_code == 0
  assert "5" in result.output