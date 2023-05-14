class BaseField(object):
    def __init__(self, label=None):
        self._label = label
        self._value = None
        self.field_name = None

    def __get__(self, instance, value):
        if instance is None:
            return self
        print('value:', value)
        # print("instance:", instance)
        return self._value
        # return getattr(instance, self.field_name)

    # def __set__(self, instance, value):
    #     print("instance:", instance)
    #     print('value:', value)
    #     setattr(instance, self.field_name, value)

    def __set_name__(self, owner, name):
        self.field_name = name

    @property
    def label(self):
        if self._label:
            return self._label
        else:
            return self.field_name


class IdField(BaseField):
    def __get__(self, instance, value):
        if instance is None:
            return self
        return instance._id

    def __set__(self, instance, value):
        self._value = value


class TextField(BaseField):
    pass


class BooleanField(BaseField):
    default = False


class NumberField(BaseField):
    pass


class DateField(BaseField):
    pass


class DateTimeField(BaseField):
    pass
