from {{ cookiecutter.source_directory }}.example import hello_world


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"    
