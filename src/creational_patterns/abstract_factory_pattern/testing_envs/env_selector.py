from abc_factory import TestingEnvironmentFactory


class EnvironmentFactorySelector:
    _factories = {}

    @staticmethod
    def register_factory(environment: str):
        def decorator(factory_class: TestingEnvironmentFactory):
            EnvironmentFactorySelector._factories[environment] = factory_class
            return factory_class
        return decorator

    @staticmethod
    def select_factory(environment: str):
        factory_class = EnvironmentFactorySelector._factories.get(environment)
        if factory_class:
            return factory_class()
        else:
            raise ValueError("Invalid environment")


class RegisterEnvironment:
    """Decorator for Environment factory registration"""
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self, factory_class: TestingEnvironmentFactory):
        """Register the env factory corresponding to the env name"""
        EnvironmentFactorySelector.register_factory(self.environment)(factory_class)
        return factory_class
