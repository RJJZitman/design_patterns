from abc import ABCMeta, abstractmethod


class TestingEnvironmentFactory(metaclass=ABCMeta):
    """Abstract factory for Testing envs"""
    @abstractmethod
    def create_database_connection(self):
        pass

    @abstractmethod
    def create_mock_services(self):
        pass

