class Singleton:
    _instances: dict[str, callable] = {}

    def __init__(self, cls: callable):
        """
        Initialize the Singleton instance.

        Args:
            cls: The class that is to be created comform the Singleton pattern
        """
        self.cls = cls

    def __call__(self, *args, **kwargs):

        def singleton(cls, *args, **kwargs):
            if cls.__name__ not in self._instances:
                self._instances[cls.__name__] = cls(*args, **kwargs)
            return self._instances[cls.__name__]

        return singleton(cls=self.cls, *args, **kwargs)
