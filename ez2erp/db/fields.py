class BaseField():
    def __init__(self, label=None):
        self.label = label
        self._value = None
    
    def __get__(self, instance, value):
        if instance is None:
            return self.label
        return self._value
    
    def __set__(self, instance, value):
        self._value = value


class IdField(BaseField):
    def __get__(self, instance, value):
        if instance is None:
            return 'ID'
        return instance._id
    
    
    def __set__(self, instance, value):
        self._value = value


class TextField(BaseField):
    pass


class NumberField(BaseField):
    pass


class DateField(BaseField):
    pass


class DateTimeField(BaseField):
    pass
