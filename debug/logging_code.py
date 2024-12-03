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

logging.debug("debug")
logging.info("info")
logging.warning("Warning")
logging.error("error")
logging.critical("critical")
