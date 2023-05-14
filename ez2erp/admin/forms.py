""" Admin form """
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms import widgets



class Form:
    def __init__(self, inputs):
        self.inputs = inputs
        self.sizes = None
        self._compute_sizes()
    
    
    def set_form_data(self, data):
        for row in self.inputs:
            for input in row:
                try:
                    value = getattr(data, input.field)
                except AttributeError:
                    value = None
                input.set_value(value)                
    
    
    @classmethod
    def edit(cls, inputs):
        return cls(
            inputs
        )
        
    
    def _compute_sizes(self):
        """Convert row inputs count to bootstrap classes (eg. col-md-<n of row inputs>)
        """
        sizes = []
        for row in self.inputs:
            count = len(row)
            if count == 1:
                sizes.append("md-12")
            elif count == 2:
                sizes.append("md-6")
            elif count == 3:
                sizes.append("md-4")
            elif count == 4:
                sizes.append("md-3")
            else:
                sizes.append("md-2")
        self.sizes = sizes


class Input:
    def __init__(self, type, field, label, required):
        self.type = type
        self.field = field
        self.label = label
        self.required = required
        self.value = None

    def set_value(self, value):
        self.value = value


    @classmethod
    def text(cls, field, label=None, required=False):
        return cls(
            'text',
            field,
            label,
            required
        )


# class Input:
#     widget = widgets.TextInput()
#     # if no validators argument then make required = False
#     def __init__(self,type="text",placeholder='',model=None,required=True,readonly=False,*args, **kwargs):
#         super(AdminField,self).__init__(*args,**kwargs)
#         self.label = kwargs.get('label')
#         self.model = model
#         self.required = required
#         self.readonly = readonly
#         self.auto_generated = ""

#         if placeholder == '':
#             self.placeholder = self.label.upper()
#         else:
#             self.placeholder = placeholder

#         if self.model:
#             self.type = 'select'
#             self.select_data = model.objects
#         else:
#             self.type = type

#     def process_formdata(self, valuelist):
#         if valuelist:
#             self.data = valuelist[0]
#         elif self.data is None:
#             self.data = ''


class AdminTableForm(FlaskForm):
    
    @property
    def __table_columns__(self):
        raise NotImplementedError('Must implement table_columns')

    @property
    def __heading__(self):
        raise NotImplementedError('Must implement heading')

    @property
    def fields(self):
        raise NotImplementedError('Must implement fields')

    @property
    def inlines(self):
        pass
    
    def __init__(self, *args, **kwargs):
        super(AdminTableForm,self).__init__(*args,**kwargs)
        self.__title__ = self.__heading__
        self.__subheading__ = "List of " + self.__heading__


class AdminEditForm(FlaskForm):

    @property
    def __heading__(self):
        raise NotImplementedError('Must implement heading')

    @property
    def fields(self):
        raise NotImplementedError('Must implement fields')

    @property
    def inlines(self):
        pass
    
    def __init__(self, *args, **kwargs):
        super(AdminEditForm,self).__init__(*args,**kwargs)
        self.__title__ = self.__heading__
        self.__subheading__ = "Update existing data"


class AdminInlineForm(object):
    data = None

    @property
    def __table_id__(self):
        raise NotImplementedError('Must implement table_id')

    @property
    def __table_columns__(self):
        raise NotImplementedError('Must implement table_columns')

    @property
    def __title__(self):
        raise NotImplementedError('Must implement title')

    @property
    def __html__(self):
        raise NotImplementedError('Must implement html')

    @property
    def buttons(self):
        pass


class AdminField(Field):

    widget = widgets.TextInput()
    # if no validators argument then make required = False
    def __init__(self,type="text",placeholder='',model=None,required=True,readonly=False,*args, **kwargs):
        super(AdminField,self).__init__(*args,**kwargs)
        self.label = kwargs.get('label')
        self.model = model
        self.required = required
        self.readonly = readonly
        self.auto_generated = ""

        if placeholder == '':
            self.placeholder = self.label.upper()
        else:
            self.placeholder = placeholder

        if self.model:
            self.type = 'select'
            self.select_data = model.objects
        else:
            self.type = type

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0]
        elif self.data is None:
            self.data = ''

    def _value(self):
        return text_type(self.data) if self.data is not None else ''

