from . import parser,models
from django import forms


class PerserForm(forms.Form):
    MEDIA_CHOICE = (
        ('Watchs','Watchs'),
        ('Lalafo','Lalafo')
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            'media_type',
        ]


    def parse_data(self):
        if self.data['media_type'] == "Watchs":
            watchs_parser = parser.parser_func_watch()
            for data in watchs_parser:
                models.Watchs.objects.create(**data)
        elif self.data['media_type'] == 'Lalafo':
            lalafo_parser = parser.parser_func_lalafo()
            for data in lalafo_parser:
                models.Lalafo.objects.create(**data)

