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
        """Custom string representation for prettiness"""
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
        """Static method to get a builder for this specific class"""
        return AppConfigBuilder(config=AppConfig())


class AppConfigBuilder:
    """
    Builder for Config objects by utilising sub-builders. Note that the sub-builders are dynamically registered in
    the 'components' attribute when the file is read and added as properties when an AppConfigBuilder instance is
    created.
    """
    components = {}

    def __init__(self, config: AppConfig | None = AppConfig()):
        self.config = config

    def __new__(cls, **kwargs):
        """Set get properties to the created instance of AppConfigBuilder for all sub-builders."""
        def _get(self):
            return cls.components[prop_name](config=self.config)
        prop_name = cls.__name__.lower()
        print(prop_name)

        # Assign property to the parent class
        obj = object.__new__(cls)
        # print(prop_name, obj.__class__.__name__)
        # TODO: make the statement below generic such that it can work on any 'parent' builder. maybe in decorator and provide name or something to make it dynamically checkable
        setattr(AppConfigBuilder, prop_name, property(fget=_get))
        return obj

    def __init_subclass__(cls, **kwargs):
        """Register the names of all defined sub-builders. Sub-builders must inherit from AppConfigBuilder."""
        prop_name = cls.__name__.lower()
        AppConfigBuilder.components[prop_name] = cls

    def build(self):
        """Returns the AppConfig"""
        return self.config
