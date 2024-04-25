class DatabaseConfig:
    def __init__(self):
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database_name = None

    def __str__(self):
        return f"Database Config: Host={self.host}, Port={self.port}, Username={self.username}, Password={self.password}, Database={self.database_name}"


class DatabaseConfigBuilder:
    def __init__(self):
        self.config = DatabaseConfig()

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

    def build(self):
        return self.config


class LoggingConfig:
    def __init__(self):
        self.log_file = None
        self.log_level = None
        self.log_format = None

    def __str__(self):
        return f"Logging Config: Log File={self.log_file}, Log Level={self.log_level}, Log Format={self.log_format}"


class LoggingConfigBuilder:
    def __init__(self):
        self.config = LoggingConfig()

    def with_log_file(self, log_file):
        self.config.log_file = log_file
        return self

    def with_log_level(self, log_level):
        self.config.log_level = log_level
        return self

    def with_log_format(self, log_format):
        self.config.log_format = log_format
        return self

    def build(self):
        return self.config


class SecurityConfig:
    def __init__(self):
        self.auth_mechanism = None
        self.encryption_enabled = False
        self.access_control_enabled = False

    def __str__(self):
        return f"Security Config: Auth Mechanism={self.auth_mechanism}, Encryption Enabled={self.encryption_enabled}, Access Control Enabled={self.access_control_enabled}"


class SecurityConfigBuilder:
    def __init__(self):
        self.config = SecurityConfig()

    def with_auth_mechanism(self, auth_mechanism):
        self.config.auth_mechanism = auth_mechanism
        return self

    def enable_encryption(self):
        self.config.encryption_enabled = True
        return self

    def enable_access_control(self):
        self.config.access_control_enabled = True
        return self

    def build(self):
        return self.config


class ApiConfig:
    def __init__(self):
        self.base_url = None
        self.supported_methods = []
        self.auth_token = None

    def __str__(self):
        return f"API Config: Base URL={self.base_url}, Supported Methods={self.supported_methods}, Auth Token={self.auth_token}"


class ApiConfigBuilder:
    def __init__(self):
        self.config = ApiConfig()

    def with_base_url(self, base_url):
        self.config.base_url = base_url
        return self

    def with_supported_methods(self, methods):
        self.config.supported_methods = methods
        return self

    def with_auth_token(self, auth_token):
        self.config.auth_token = auth_token
        return self

    def build(self):
        return self.config


class AppConfigBuilder:
    def __init__(self):
        self.database_builder = DatabaseConfigBuilder()
        self.logging_builder = LoggingConfigBuilder()
        self.security_builder = SecurityConfigBuilder()
        self.api_builder = ApiConfigBuilder()

    def database(self):
        return self.database_builder

    def logging(self):
        return self.logging_builder

    def security(self):
        return self.security_builder

    def api(self):
        return self.api_builder

    def build(self):
        database_config = self.database_builder.build()
        logging_config = self.logging_builder.build()
        security_config = self.security_builder.build()
        api_config = self.api_builder.build()

        return f"Application Configuration:\n{database_config}\n{logging_config}\n{security_config}\n{api_config}"


if __name__ == "__main__":
    app_builder = AppConfigBuilder()

    app_config = app_builder\
        .database()\
            .with_host("localhost")\
            .with_port(5432)\
            .with_credentials("admin", "password")\
            .with_database("my_database")\
        .logging()\
            .with_log_file("/var/log/app.log")\
            .with_log_level("DEBUG")\
            .with_log_format("TEXT")\
        .security()\
            .with_auth_mechanism("OAUTH2")\
            .enable_encryption()\
            .enable_access_control()\
        .api()\
            .with_base_url("https://api.example.com")\
            .with_supported_methods(["GET", "POST", "PUT", "DELETE"])\
            .with_auth_token("my_api_token")\
        .build()

    print(app_config)
