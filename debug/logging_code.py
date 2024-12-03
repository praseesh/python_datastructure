import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")

logging.debug("debug")
logging.info("info")
logging.warning("Warning")
logging.error("error")
logging.critical("critical")
