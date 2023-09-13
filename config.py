import os
import logging
from dotenv import load_dotenv
from pathlib import Path


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a logger with the given name and level.

    :param name: Name of the logger.
    :param level: Level of the logger.
    :return: Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

logger = get_logger(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# Check file exists
if not os.path.exists(dotenv_path):
    raise ValueError("No .env file found")

load_dotenv(dotenv_path)
logger.info(f"SO_KEY: {os.getenv('SO_KEY')}")
    
# Set the stackoverflow key
os.environ['SO_KEY'] = os.getenv('SO_KEY')

# Set the root directory
ROOT_DIR = Path(os.getenv('ROOT_DIR'))
DATA_DIR = ROOT_DIR / "data"

# Make sure the data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)