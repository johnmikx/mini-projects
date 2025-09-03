# Python already comes with a powerful built-in logging module. So you can
# quickly add logging to your application by simply saying `import logging`.

# We will have a look at the different block levels, the different configuration
# options. 
# How to lock in different modules? 
# How to use different lock handlers?
# How to capture stack traces in your log? and
# How to use rotating file handler?

import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# They indicate the severity of the events
# Output:
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

# This is because by default, only levels of messages with level warning
# or above are printed.

# If we want to change this, we can do that by setting the basic configuration.
# And usually we want to do this right after importing them logging module.

import logging
# logging.basicConfig(level=logging.DEBUG, 
#                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:%S')

# Can be found at Python Documentation look for logging.basicConfig

# logging.debug('This is a debug message')
#logging.info('This is an info message')
# logging.warning('This is a warning message')
#logging.error('This is an error message')
# logging.critical('This is a critical message')

# Output:
# 09/03/2025 00:07:52 - root - DEBUG - This is a debug message
# 09/03/2025 00:07:52 - root - INFO - This is an info message
# 09/03/2025 00:07:52 - root - WARNING - This is a warning message     
# 09/03/2025 00:07:52 - root - ERROR - This is an error message        
# 09/03/2025 00:07:52 - root - CRITICAL - This is a critical message

# import helper # 09/03/2025 00:11:07 - helper - INFO - hello from helper

import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')
# Output: 2025-09-03 09:57:47,436 - simpleExample - DEBUG - this is a debug message

logger = logging.getLogger(__name__)

# Create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')

# Output:
# __main__ - WARNING - this is a warning
# __main__ - ERROR - this is an error