import logging

# INFO
__version__ = "1.0.0"

logger = logging.getLogger("tuftest")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] %(name)s | %(levelname)s - %(message)s')

# File Handler
handler = logging.FileHandler("tuftest.log", encoding="utf-8")
handler.setFormatter(formatter)

# Only add if not already added
if not logger.hasHandlers():
    logger.addHandler(handler)


logger.info("Initializing TUFtest")
