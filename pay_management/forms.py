from django import forms
from .models import SalarySlip


class add_salaryForm(forms.ModelForm):
    class Meta:
        model = SalarySlip
        exclude = ( 'staff',
                    'created_at',
                    'total_deduction',
                    'tax_number',
                    'gross_salary',
                    'net_salary',
                    'json_salary',
                )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'non_taxable_additional_allowances': 'non taxable additional allowance',
            'taxable_additional_allowances': 'taxable additional allowance',
            'tax_deduction': 'Tax rate deduction',
        }

        self.fields['non_taxable_additional_allowances'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field not in ['basic_salary', 'transport_allowance']:
                self.fields[field].widget.attrs[
                        'placeholder'] = placeholders[field]
            self.fields[field].widget.attrs[
            'class'] = 'border-dark rounded-0 mx-auto add_salary-form-input m-1'
            if field in ['basic_salary', 'transport_allowance', 'tax_deduction']:
                self.fields['basic_salary'].label = 'Basic Salary'
                self.fields['transport_allowance'].label = 'Transport Allowance'
                self.fields['tax_deduction'].label = '% Tax Deduction'
            else:
                self.fields[field].label = False
