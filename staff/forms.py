from django import forms
from .models import Staff, SickLeave, AnnualLeave
from bootstrap_datepicker_plus import DatePickerInput

class add_staffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'tax_number': 'Tax number',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'address': 'Home address',
            'birth_date': 'Birthday',
            'gender': 'Gender',
            'management_level': 'Management Level',
            'entry_date': 'Date of entry',
            'termination_date': 'Date of termination',
            'position_held': 'Position held',
            'basic_salary': 'Basic Salary',
            'transport_allowance': 'Transport allowance',
            'annual_leave': 'Annual Leave',
            'annual_leave_remaining': 'Annual Leave Remaining',
            'sick_leave': 'Sick Leave',
            'sick_leave_remaining': 'Sick Leave Remaining',
            'image': 'Image',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'gender' and field != 'management_level':
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholders[field]

            if field in ['birth_date', 'entry_date', 'termination_date']:
                self.fields[field].widget = DatePickerInput()
                self.fields[field].widget.attrs[
                'class'] = 'border-dark rounded-0 mx-auto add_staff-form-input m-1'
            else:
                self.fields[field].widget.attrs[
                'class'] = 'border-dark m-1 rounded-0 mx-auto add_staff-form-input'

            if field == 'image':
                self.fields['image'].label = 'Upload Image'
            else:
                self.fields[field].label = False


class add_sick_leaveForm(forms.ModelForm):
    class Meta:
        model = SickLeave
        exclude = ('staff', 'days', 'sick_reset',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'start_date': 'Start date',
            'end_date': 'End date',
        }

        self.fields['start_date'].widget.attrs['autofocus'] = True
        for field in self.fields:                          
            self.fields[field].widget = DatePickerInput()
            self.fields[field].widget.attrs[
            'class'] = 'border-dark rounded-0 mx-auto add_leave-form-input m-1'

            self.fields[field].label = False


class add_annual_leaveForm(forms.ModelForm):
    class Meta:
        model = AnnualLeave
        exclude = ('staff', 'days',)
            
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {            
            'start_date': 'Start date',
            'end_date': 'End date',                         
        }

        self.fields['start_date'].widget.attrs['autofocus'] = True
        for field in self.fields:                          
            self.fields[field].widget = DatePickerInput()
            self.fields[field].widget.attrs[
            'class'] = 'border-dark rounded-0 mx-auto add_leave-form-input m-1' 
                              
            self.fields[field].label = False


