import logging
from pathlib import Path


def configure_logging(log_level: str = "INFO", log_file: str = "logs/app.log") -> None:
    """Configure application logging for console and file output."""
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    if root_logger.handlers:
        root_logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(numeric_level)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
