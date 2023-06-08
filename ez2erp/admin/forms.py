""" Admin form """
from flask_wtf import FlaskForm
from wtforms import Field
from wtforms import widgets



class Form:
    def __init__(self, inputs, inlines=None, **kwargs):
        self.inputs = inputs
        self.inlines = inlines
        self.cards_html = kwargs.get('cards_html')
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
    def create(cls, inputs):
        return cls(
            inputs
        )

    
    @classmethod
    def edit(cls, inputs, cards_html=None):
        return cls(
            inputs,
            cards_html=cards_html
        )
        
    
    def _compute_sizes(self):
        """Convert row inputs count to bootstrap classes (eg. col-md-<n of row inputs>)
        """
        sizes = []
        for row in self.inputs:
            count = len(row)
            if count == 1:
                sizes.append("mb-3")
            elif count == 2:
                sizes.append("mb-3")
            elif count == 3:
                sizes.append("mb-3")
            elif count == 4:
                sizes.append("mb-3")
            else:
                sizes.append("mb-3")
        self.sizes = sizes


class Input:
    def __init__(self, type, field, required=False, label=None, **kwargs):
        self.type = type
        self.field = field
        self.required = required
        self.value = None
        self.options = kwargs.get('options')

        if label:
            self.label = label
        else:
            self.label = field.label

    
    def set_value(self, value):
        self.value = value


    @classmethod
    def text(cls, field, required=False, **kwargs):
        return cls(
            'text',
            field,
            required,
            **kwargs
        )

    
    @classmethod
    def email(cls, field, required=False, **kwargs):
        return cls(
            'email',
            field,
            required,
            **kwargs
        )
        
    
    @classmethod
    def select(cls, field, required, **kwargs):
        model = field.get_model()
        options = [Option("", "Choose...")]
        query = model.query.all()

        for row in query:
            options.append(Option(row.id, row.name))
        
        return cls(
            'select',
            field,
            required,
            options=options,
            **kwargs
        )
        
    
class Option:
    def __init__(self, value, label):
        self.value = value
        self.label = label


class Table:
    def __init__(self, columns, data=None, title=None):
        self.columns = columns
        self.data = data
        self.title = title
        self.element = 'TABLE'


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

