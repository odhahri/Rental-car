
class OfficeService():
    def get_html_input_type(field):
            """
            Map Django serializer field types to HTML input types.
            """
            field_type = str(field.__class__.__name__)

            field_mapping = {
                'CharField': 'text',
                'IntegerField': 'number',
                'FloatField': 'number',
                'DecimalField': 'number',  
                'DateTimeField': 'datetime-local',
                'DateField': 'date',
                'TimeField': 'time',
                'BooleanField': 'checkbox',
                'EmailField': 'email',
                'URLField': 'url',
                'ChoiceField': 'select', 
                'FileField': 'file',
                'ImageField': 'file',
            }

            return field_mapping.get(field_type, 'text')