from abc_factory import TestingEnvironmentFactory


class TestingClient:
    """Testing client that utilises the TestingEnvironmentFactory to provide the desired environments"""
    def __init__(self, factory: TestingEnvironmentFactory):
        self.factory = factory

    def get_database_connection(self):
        return self.factory.create_database_connection()

    def get_mock_services(self):
        return self.factory.create_mock_services()
