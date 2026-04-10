from app.cli import main


def test_main_prints_default_greeting(capsys, monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["prog"])

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "Hello, Justin!"


def test_main_prints_custom_greeting(capsys, monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["prog", "--name", "David"])

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "Hello, David!"
