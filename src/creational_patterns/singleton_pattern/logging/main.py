from logger import Logger

# Initialize and get the logger
log = Logger(name="MyLogger")
logger = log.get_logger()

# test for other logger
logger2 = Logger(name="number2").get_logger()

if __name__ == "__main__":
    # Test logging
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

    print(logger == logger2)
