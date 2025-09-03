import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0, w1, w2, etc (Time)
handler = TimedRotatingFileHandler('timed_test.log', when='s',
                                   interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, World!')
    time.sleep(5)