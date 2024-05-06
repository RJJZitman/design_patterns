class BuilderMeta(type):
    """
    Metaclass for builders to register and dynamically create properties for subclasses. This metaclass is designed
    to enable for Builder design patterns with underlying sub-builders. By implementing this metaclass, all sub-builders
    (those that inherit from a parent-builder) are available as properties within the parent-builder instance.
    Therefore, these properties also exist within the sub-builders. This allows for direct chaining of the methods from
    the sub-builders.
    """

    def __init__(cls, name, bases, clsdict):
        super().__init__(name, bases, clsdict)

        # retrieve the base builder class dynamically
        base_builder_cls = next((base for base in bases if isinstance(base, BuilderMeta)), None)

        # set a property for each sub-builder in the parent-builder class
        if base_builder_cls and cls is not base_builder_cls:
            setattr(base_builder_cls, name.lower(), property(lambda self, cls=cls: cls(self.cls_to_build)))
