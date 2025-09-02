import logging
from . import logger, __version__

logger = logging.getLogger(f"crypt.{__name__}") # Name of module (for easier debugging!!!)

print(f"Current Version: {__version__}")
logger.info(f"Current Version: {__version__}")
input("Press ENTER to continue: ")

[...]