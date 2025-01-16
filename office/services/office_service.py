
class OfficeService():
    def get_html_input_type(field):
            """
            Map Django serializer field types to HTML input types.
            """
            field_type = str(field.__class__.__name__)

            # Map field types to HTML input types
            field_mapping = {
                'CharField': 'text',
                'IntegerField': 'number',
                'FloatField': 'number',
                'DecimalField': 'number',  # You can add `step` attribute for precision
                'DateTimeField': 'datetime-local',
                'DateField': 'date',
                'TimeField': 'time',
                'BooleanField': 'checkbox',
                'EmailField': 'email',
                'URLField': 'url',
                'ChoiceField': 'select',  # For choices, use a <select> input
                'FileField': 'file',
                'ImageField': 'file',
            }

            # Return corresponding HTML input type or 'text' as default
            return field_mapping.get(field_type, 'text')