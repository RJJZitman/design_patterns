class AppConfig:
    def __init__(self):
        self.host: str | None = None
        self.port: str | None = None
        self.username: str | None = None
        self.password: str | None = None
        self.database_name: str | None = None

        self.base_url: str | None = None
        self.supported_methods: str | None = None
        self.auth_token: str | None = None

    def __str__(self):
        return self.host
        # components = '\n'.join([getattr(AppConfigBuilder, component)
        #                         for component in list(AppConfigBuilder.components)])
        # print(components)
        # return f"Application Configuration:\n{AppConfigBuilder.apiconfigbuilder.fget()}"
        # print(f"Application Configuration:\n{dir(AppConfigBuilder)}")
        # return f"Application Configuration:\n{AppConfigBuilder}"
        # return "hailo"

    @staticmethod
    def get_app_config_builder():
        return AppConfigBuilder(config=AppConfig())


class AppConfigBuilder:
    components = {}

    def __init__(self, config: AppConfig | None = None):
        self.config = config if config is not None else AppConfig()

    def __new__(cls, **kwargs):
        def _get(self):
            print(f"INT _GET, WITH KWARGS: {kwargs} AND PROPERTY NAME: {prop_name}")
            return cls.components[prop_name](config=self.config)
        prop_name = cls.__name__.lower()

        # Assign property to the parent class
        obj = object.__new__(cls)
        setattr(AppConfigBuilder, prop_name, property(fget=_get))
        return obj

    def __init_subclass__(cls, **kwargs):
        prop_name = cls.__name__.lower()
        AppConfigBuilder.components[prop_name] = cls
        # print(AppConfigBuilder.config)
        print("AppConfigBuilder __init_subclass__")
        print(AppConfigBuilder.components)

    def build(self):
        print("in build")
        print(self.config)
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

    print("main")
    print(dir(app_builder))
    # print(dir(api))
    # print(dir(db))
    # print(app_builder.databaseconfigbuilder.config)
    print("main")

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

    print(f"app_config: {app_config}")
    # print(f"app_config.config: {app_config.config}")
    # print(f"app_config.app_config.build: {app_config.config.build()}")

