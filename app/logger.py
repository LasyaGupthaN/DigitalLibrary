import logging

logger = logging.getLogger("digital_library")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("library.log")
console_handler = logging.StreamHandler()

fmt = "%(asctime)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(fmt)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
