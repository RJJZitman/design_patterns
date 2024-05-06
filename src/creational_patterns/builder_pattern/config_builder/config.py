from builder_meta import BuilderMeta


class AppConfig:
    def __init__(self):
        # TODO: put each sub config in a seperate (pydantic basemodel?) class whilst (preferable) allowing direct access to attributes in sub builders. config component classes should shre __str__ formatting for consistency
        # db config
        self.host: str | None = None
        self.port: str | None = None
        self.username: str | None = None
        self.password: str | None = None
        self.database_name: str | None = None

        # api config
        self.base_url: str | None = None
        self.supported_methods: str | None = None
        self.auth_token: str | None = None

    def __str__(self):
        """Custom string representation."""
        db_info = f"DB:\nhost: {self.host}, port: {self.port}, username: {self.username}, " \
                  f"password: {self.password}, database_name: {self.database_name}"
        api_info = f"API:\nbase_url: {self.base_url}, supported_methods: {self.supported_methods}, " \
                   f"auth_token: {self.auth_token}"
        return db_info + "\n" + api_info

    @staticmethod
    def get_app_config_builder():
        """Static method to get a builder for this specific class"""
        return AppConfigBuilder(config=AppConfig())


class AppConfigBuilder(metaclass=BuilderMeta):
    """Base builder for AppConfig."""
    ClassToBuild = AppConfig  # Reference to the Config class

    def __init__(self, config=None):
        self.cls_to_build = config or self._create_default_config()

    def _create_default_config(self):
        # TODO: move to metaclass with header def _create_template_class_to_build(self):
        # TODO: raise error when ClassToBuild attribute does not exist!
        """Create a default config instance using the ClassToBuild."""
        return self.ClassToBuild()

    def build(self):
        """Returns the built config."""
        return self.cls_to_build


class DatabaseConfigBuilder(AppConfigBuilder):
    """Sub-builder for DB config information."""

    def with_host(self, host):
        self.cls_to_build.host = host
        return self

    def with_port(self, port):
        self.cls_to_build.port = port
        return self

    def with_credentials(self, username, password):
        self.cls_to_build.username = username
        self.cls_to_build.password = password
        return self

    def with_database(self, database_name):
        self.cls_to_build.database_name = database_name
        return self


class ApiConfigBuilder(AppConfigBuilder):
    """Sub-builder for API config information."""

    def with_base_url(self, base_url):
        self.cls_to_build.base_url = base_url
        return self

    def with_supported_methods(self, methods):
        self.cls_to_build.supported_methods = methods
        return self

    def with_auth_token(self, auth_token):
        self.cls_to_build.auth_token = auth_token
        return self
