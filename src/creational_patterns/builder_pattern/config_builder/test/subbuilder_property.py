class EnsurePropertyExists:
    def __init__(self, prop_name):
        self.prop_name = prop_name

    def __call__(self, cls):
        def wrapper(*args, **kwargs):
            instance = cls(*args, **kwargs)
            if not hasattr(instance, self.prop_name):
                setattr(instance, self.prop_name, None)
            return instance
        return wrapper
