from app.config import Settings


def test_settings_defaults(monkeypatch) -> None:
    monkeypatch.delenv("APP_DEFAULT_NAME", raising=False)
    monkeypatch.delenv("APP_LOG_LEVEL", raising=False)
    monkeypatch.delenv("APP_ENV", raising=False)

    settings = Settings.from_env()

    assert settings.default_name == "Justin"
    assert settings.log_level == "INFO"
    assert settings.app_env == "development"


def test_settings_from_env(monkeypatch) -> None:
    monkeypatch.setenv("APP_DEFAULT_NAME", "David")
    monkeypatch.setenv("APP_LOG_LEVEL", "debug")
    monkeypatch.setenv("APP_ENV", "production")

    settings = Settings.from_env()

    assert settings.default_name == "David"
    assert settings.log_level == "DEBUG"
    assert settings.app_env == "production"
