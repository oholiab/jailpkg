import pytest
from jailpkg import run as j

basic_yaml = "tests/unit/fixtures/test_yaml_load_fine_on_hash_load.yaml"

def test_generate_command_expected_output():
    assert j.generate_command('python27', '/some/jail') == 'pkg install python27 -c /some/jail'

def test_yaml_load_fine_on_hash_load():
    assert j.parse_yaml_packages(basic_yaml)\
            == {"somejail": ["some", "packages"],}

def test_yaml_to_commands_expected_commands():
    assert j.yaml_to_commands(basic_yaml)\
            == ["pkg install some -c somejail", "pkg install packages -c somejail"]

def test_parse_args_fails_on_mutual_exclusions():
    errormsg = "--package and --jailpath args are mutually exclusive to --config\n" 
    shouldfail = [
            "--config someconfig --package package --jailpath /some/path",
            "--config someconfig --package package",
            "--config someconfig --jailpath /some/path",
            ]
    for i in shouldfail:
        with pytest.raises(j.ArgumentError) as e:
            j.parse_args(i.split(" "))
        assert errormsg == str(e.value)

def test_parse_args_fails_on_no_config_but_no_jailpath_and_package():
    errormsg = "--package and --jailpath arguments must be specified together (or use --config)\n"
    shouldfail = [
            "--package package",
            "--jailpath /some/path",
            ]
    for i in shouldfail:
        with pytest.raises(j.ArgumentError) as e:
            j.parse_args(i.split(" "))
        assert errormsg == str(e.value)
