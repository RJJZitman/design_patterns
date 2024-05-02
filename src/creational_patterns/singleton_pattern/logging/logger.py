import logging

from src.creational_patterns.singleton_pattern.singleton_metaclass import SingletonMeta


class Logger(metaclass=SingletonMeta):
    """ Singleton Logger class using the SingletonMeta metaclass. """

    def __init__(self, name='singleton_logger', level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # create console handler and set level to debug
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)

        # add console handler to logger
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """ Return the singleton logger instance. """
        return self.logger
