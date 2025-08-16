import os
from loguru import logger

# Setup logger
os.makedirs("logs", exist_ok=True)
logger.remove()

# Distinct log files
logger.add(
    "logs/cli.log",
    level="INFO",
    rotation="1 MB",
    compression="zip",
    filter=lambda record: record["extra"].get("mode") == "cli",
)
logger.add(
    "logs/interactive.log",
    level="INFO",
    rotation="1 MB",
    compression="zip",
    filter=lambda record: record["extra"].get("mode") == "interactive",
)


def get_logger(mode: str):
    return logger.bind(mode=mode)
