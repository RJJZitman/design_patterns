class EnvironmentFactorySelector:
    _factories = {}

    @staticmethod
    def register_factory(environment):
        def decorator(factory_class):
            EnvironmentFactorySelector._factories[environment] = factory_class
            return factory_class
        return decorator

    @staticmethod
    def select_factory(environment):
        factory_class = EnvironmentFactorySelector._factories.get(environment)
        if factory_class:
            return factory_class()
        else:
            raise ValueError("Invalid environment")


class RegisterEnvironment:
    def __init__(self, environment):
        self.environment = environment

    def __call__(self, factory_class):
        EnvironmentFactorySelector.register_factory(self.environment)(factory_class)
        return factory_class
