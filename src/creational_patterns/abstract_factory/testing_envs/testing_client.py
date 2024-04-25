from abc_factory import TestingEnvironmentFactory


class TestingClient:
    def __init__(self, factory: TestingEnvironmentFactory):
        self.factory = factory

    def get_database_connection(self):
        return self.factory.create_database_connection()

    def get_mock_services(self):
        return self.factory.create_mock_services()
