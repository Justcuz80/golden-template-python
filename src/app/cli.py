import argparse
import logging

from app.config import Settings
from app.hello import greet
from app.logging_config import configure_logging

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the greeting application.")
    parser.add_argument(
        "--name",
        default=None,
        help="Name to use in the greeting.",
    )
    return parser.parse_args()


def main() -> int:
    """Run the application CLI."""
    settings = Settings.from_env()
    configure_logging(settings.log_level, settings.log_file)

    logger.info("Application started")
    logger.info("Loaded application settings")
    logger.info("Running in environment: %s", settings.app_env)
    logger.info("Writing logs to: %s", settings.log_file)

    args = parse_args()
    name = args.name if args.name is not None else settings.default_name
    logger.info("Using greeting target: %s", name)

    message = greet(name)
    logger.info("Greeting generated successfully")

    print(message)
    logger.info("Application finished successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
