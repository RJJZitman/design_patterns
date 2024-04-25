from abc import ABCMeta, abstractmethod


class TestingEnvironmentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_database_connection(self):
        pass

    @abstractmethod
    def create_mock_services(self):
        pass

