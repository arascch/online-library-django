from django import forms

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="enter a date between now and 4 weeks (default 3).")