from django.db import models


class Staff(models.Model):

    class Meta:
        verbose_name_plural = "Staff"

    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email_address = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=254)
    birth_date = models.DateField()  
    GENDER = [
                ('Male', 'Male'),
                ('Female', 'Female'),
                ('Other', 'Other'), ]
    gender = models.CharField(max_length=6, choices=GENDER, null=False)
    management_level_choices = [
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'), 
                ('5', '5'),   
                ]
    management_level = models.CharField(max_length=26, choices=management_level_choices, null=False)
    entry_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)  
    position_held = models.CharField(max_length=254)
    basic_salary = models.IntegerField()
    transport_allowance = models.IntegerField()
    annual_leave = models.IntegerField()
    annual_leave_remaining = models.IntegerField()    
    sick_leave = models.IntegerField()
    sick_leave_remaining = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name  

  
class SickLeave(models.Model):

    class Meta:
        verbose_name_plural = "Sick leave"

    staff = models.ForeignKey(
            'Staff', null=False, blank=False, on_delete=models.CASCADE,
            related_name='sickleave')
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.IntegerField()

    def __str__(self):
        return self.staff.first_name


class AnnualLeave(models.Model):

    class Meta:
        verbose_name_plural = "Annual leave"

    staff = models.ForeignKey(
            'Staff', null=False, blank=False, on_delete=models.CASCADE,
            related_name='annuallleave')
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.IntegerField()

    def __str__(self):
        return self.staff.first_name
