from config_components import DatabaseConfig, ApiConfig
from subbuilder_property import EnsurePropertyExists
from app_config import AppConfigBuilder


# @EnsurePropertyExists('database_builder')
class DatabaseConfigBuilder(AppConfigBuilder):
    def __init__(self):
        self.database_builder = DatabaseConfig()

    def with_host(self, host):
        self.database_builder.host = host
        return self

    def with_port(self, port):
        self.database_builder.port = port
        return self

    def with_credentials(self, username, password):
        self.database_builder.username = username
        self.database_builder.password = password
        return self

    def with_database(self, database_name):
        self.database_builder.database_name = database_name
        return self

    def build(self):
        return self.database_builder


# @EnsurePropertyExists('api_builder')
class ApiConfigBuilder(AppConfigBuilder):
    def __init__(self):
        self.api_builder = ApiConfig()

    def with_base_url(self, base_url):
        self.api_builder.base_url = base_url
        return self

    def with_supported_methods(self, methods):
        self.api_builder.supported_methods = methods
        return self

    def with_auth_token(self, auth_token):
        self.api_builder.auth_token = auth_token
        return self

    def build(self):
        return self.api_builder
