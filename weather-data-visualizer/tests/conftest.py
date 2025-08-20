import sys
import os
import pytest
from loguru import logger


# Disable logging during tests
@pytest.fixture(autouse=True)
def silence_loguru():
    logger.remove()


# Add project root to sys.path dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
