import time
import logging

logging.basicConfig(
    level=logging.INFO,
    filename=time.strftime("nlp_%Y_%m_%d.log"),
    format='%(asctime)s %(levelname)-10s %(name)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_info(msg):
    logging.info(msg)
