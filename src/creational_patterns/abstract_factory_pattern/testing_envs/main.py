from env_factories import *
from testing_client import TestingClient
from env_selector import EnvironmentFactorySelector


if __name__ == "__main__":
    # Example usage
    environment = "development"  # Change this to "staging" or "production" for different environments

    factory = EnvironmentFactorySelector.select_factory(environment=environment)
    client = TestingClient(factory=factory)

    # Get database connection
    database_connection = client.get_database_connection()
    print("Database Connection:", database_connection)

    # Get mock services
    mock_services = client.get_mock_services()
    print("Mock Services:", mock_services)
