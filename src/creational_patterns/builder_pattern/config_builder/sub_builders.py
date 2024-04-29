from config import AppConfig, AppConfigBuilder


class DatabaseConfigBuilder(AppConfigBuilder):
    """Sub-builder for DB config information"""
    def __init__(self, config: AppConfig | None = None):
        super().__init__(config)

    def with_host(self, host):
        self.config.host = host
        return self

    def with_port(self, port):
        self.config.port = port
        return self

    def with_credentials(self, username, password):
        self.config.username = username
        self.config.password = password
        return self

    def with_database(self, database_name):
        self.config.database_name = database_name
        return self


class ApiConfigBuilder(AppConfigBuilder):
    """Sub-builder for API config information"""
    def __init__(self, config: AppConfig | None = None):
        super().__init__(config)

    def with_base_url(self, base_url):
        self.config.base_url = base_url
        return self

    def with_supported_methods(self, methods):
        self.config.supported_methods = methods
        return self

    def with_auth_token(self, auth_token):
        self.config.auth_token = auth_token
        return self
