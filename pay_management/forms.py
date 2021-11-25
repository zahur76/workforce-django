from django import forms
from .models import SalarySlip


class add_salaryForm(forms.ModelForm):
    class Meta:
        model = SalarySlip
        exclude = ('created_at',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)        

        self.fields['staff'].widget.attrs['autofocus'] = True
        for field in self.fields:          
            self.fields[field].widget.attrs[
            'class'] = 'border-dark rounded-0 mx-auto add_salary-form-input m-1' 

            self.fields[field].label = False
