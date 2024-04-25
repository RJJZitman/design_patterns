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
        # TODO: must create dynamically from subbuilder __str__ methods
        config_text = (f"DB:\n"
                       f"host: {self.host}, port: {self.port}, username: {self.username}, password: {self.password}, "
                       f"database_name: {self.database_name}\n"
                       f"API\n"
                       f"base_url: {self.base_url}, supported_methods: {self.supported_methods}, "
                       f"auth_token: {self.auth_token}")
        return config_text

    @staticmethod
    def get_app_config_builder():
        return AppConfigBuilder(config=AppConfig())


class AppConfigBuilder:
    components = {}

    def __init__(self, config: AppConfig | None = None):
        self.config = config if config is not None else AppConfig()

    def __new__(cls, **kwargs):
        def _get(self):
            return cls.components[prop_name](config=self.config)
        prop_name = cls.__name__.lower()

        # Assign property to the parent class
        obj = object.__new__(cls)
        # TODO: make the statement below generic such that it can work on any 'parent' builder. maybe in decorator and provide name or something to make it dynamically checkable
        setattr(AppConfigBuilder, prop_name, property(fget=_get))
        return obj

    def __init_subclass__(cls, **kwargs):
        prop_name = cls.__name__.lower()
        AppConfigBuilder.components[prop_name] = cls

    def build(self):
        return self.config


class DatabaseConfigBuilder(AppConfigBuilder):
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


if __name__ == "__main__":
    app_builder = AppConfig.get_app_config_builder()
    api = ApiConfigBuilder(config=AppConfig())
    db = DatabaseConfigBuilder(config=AppConfig())

    app_config = app_builder\
        .databaseconfigbuilder\
            .with_host("localhost")\
            .with_port(5432)\
            .with_credentials("admin", "password")\
            .with_database("my_database")\
        .apiconfigbuilder\
            .with_base_url("https://api.example.com")\
            .with_supported_methods(["GET", "POST", "PUT", "DELETE"])\
            .with_auth_token("my_api_token")\
        .build()

    print(f"config template: \n{AppConfig.get_app_config_builder().build()}")
    print(75*"-")
    print(f"app_config: \n{app_config}")
