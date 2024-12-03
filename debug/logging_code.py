import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="log.log",
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s ",
                    )

x = 2
logging.debug(f"here the x is {x}")
try:
    a = 2/2
    logging.info(f"answer is {a}" )
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError")
logging.info(f"2. answer is {a}" )
name = 'GFG'
logging.error('%s raised an error', name)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

logging.debug("debug")
logging.info("info")
logging.warning("Warning")
logging.error("error")
logging.critical("critical")
