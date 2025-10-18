import logging
import os

LOG_DIR = "var/log"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(module_name: str) -> logging.Logger:
    """Return a logger that writes to its own file (based on module name)."""
    log_file = os.path.join(LOG_DIR, f"{module_name}.log")

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if logger already configured
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

