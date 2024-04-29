from abc_factory import TestingEnvironmentFactory
from env_selector import RegisterEnvironment


# Note that this implementation does not break OCP due to the dynamic registering of env factories

@RegisterEnvironment("development")
class DevelopmentEnvironmentFactory(TestingEnvironmentFactory):
    """Development env"""
    def create_database_connection(self):
        # Create a connection to a development database
        return "Development Database Connection"

    def create_mock_services(self):
        # Create mock services for development environment
        return "Mock Services for Development"


@RegisterEnvironment("staging")
class StagingEnvironmentFactory(TestingEnvironmentFactory):
    """Staging env"""
    def create_database_connection(self):
        # Create a connection to a staging database
        return "Staging Database Connection"

    def create_mock_services(self):
        # Create mock services for staging environment
        return "Mock Services for Staging"


@RegisterEnvironment("production")
class ProductionEnvironmentFactory(TestingEnvironmentFactory):
    """Production env"""
    def create_database_connection(self):
        # Create a connection to a production database
        return "Production Database Connection"

    def create_mock_services(self):
        # No mock services in production environment
        return None
