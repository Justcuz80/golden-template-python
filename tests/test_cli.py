from app.cli import main


def test_main_prints_greeting(capsys) -> None:
    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "Hello, Justin!"
