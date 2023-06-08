import sys
import inspect



class BaseField(object):
    def __new__(cls, *_args, **_kwargs):
        # Background: http://eli.thegreenplace.net/2012/04/16/python-object-creation-sequence
        obj = super().__new__(cls)
        obj.module = obj._get_init_module()  # pylint: disable=protected-access
        return obj


    @staticmethod
    def _get_init_module():
        # Background: https://stackoverflow.com/a/42653524/
        frame = inspect.currentframe()
        while frame:
            if frame.f_code.co_name == '<module>':
                # return {'module': frame.f_globals['__name__'], 'line': frame.f_lineno}
                return frame.f_globals['__name__']
            frame = frame.f_back

    def __init__(self, label=None):
        self._label = label
        self._value = None
        self.field_name = None

    def __get__(self, instance, value):
        if instance is None:
            return self
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


class ReferenceField(BaseField):
    def __init__(self, model_name):
        super(ReferenceField, self).__init__(model_name)
        self.model_name = model_name
        self.model = None


    def get_model(self):
        return getattr(sys.modules[self.module], self.model_name)
