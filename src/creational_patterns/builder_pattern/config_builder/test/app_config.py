class AppConfig:
    def __init__(self):
        self.database_config = None
        self.api_config = None

    def __str__(self):
        return f"Application Configuration:\n{self.database_config}\n{self.api_config}"


class AppConfigBuilder:
    implementations = {}

    def build(self):
        app_config = AppConfig()
        for subclass_name, subclass in self.implementations.items():
            setattr(app_config, subclass_name.lower(), getattr(self, subclass_name.lower()).build())
        return app_config

    def __init_subclass__(cls, **kwargs):
        # super().__init_subclass__(**kwargs)
        AppConfigBuilder.implementations[cls.__name__] = cls
