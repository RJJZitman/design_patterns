from abc_factory import TestingEnvironmentFactory
from env_selector import RegisterEnvironment


@RegisterEnvironment("development")
class DevelopmentEnvironmentFactory(TestingEnvironmentFactory):
    def create_database_connection(self):
        # Create a connection to a development database
        return "Development Database Connection"

    def create_mock_services(self):
        # Create mock services for development environment
        return "Mock Services for Development"


@RegisterEnvironment("staging")
class StagingEnvironmentFactory(TestingEnvironmentFactory):
    def create_database_connection(self):
        # Create a connection to a staging database
        return "Staging Database Connection"

    def create_mock_services(self):
        # Create mock services for staging environment
        return "Mock Services for Staging"


@RegisterEnvironment("production")
class ProductionEnvironmentFactory(TestingEnvironmentFactory):
    def create_database_connection(self):
        # Create a connection to a production database
        return "Production Database Connection"

    def create_mock_services(self):
        # No mock services in production environment
        return None
