
from .field import Field

class StringField(Field):
    supported_strategies = ('value', 'ordered_choice', 'random_choice')

    supported_types = ('string',)

    def __init__(self, name, typ, strategy='value', arguments=[]):
        super(StringField, self).__init__(name, typ, strategy, arguments)

    def __str__(self):
        return 'StringField(strategy={}, arguments={})'.format(
            self.strategy, self.arguments)

    def cast(self, item):
        return str(item)

    def format(self, item, output_format='txt'):
        if output_format == 'csv' or output_format == 'txt':
            return item
        elif output_format == 'hex':
            return item.encode().hex()
        elif output_format == 'bin':
            return item.encode() # defaults to utf-8
        else:
            raise NotImplementedError(
                'Output format {} is not implemented for this {}.'.format(
                    output_format, type(self)))