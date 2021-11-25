from django.db import models

# Create your models here.
class salarySlip(models.Model):

    class Meta:
        verbose_name_plural = "Salary slip"

    staff = models.ForeignKey(
            'staff.Staff', null=False, blank=False, on_delete=models.CASCADE,
            related_name='salaryslip')
    created_at = models.DateTimeField(auto_now_add = True)
    basic_salary = models.IntegerField()
    transport_allowance = models.IntegerField()
    non_taxable_additional_allowances = models.IntegerField()
    taxable_additional_allowances = models.IntegerField()
    tax_deduction = models.IntegerField()
    gross_salary = models.IntegerField()
    net_salary = models.IntegerField()
    json_salary = models.CharField(max_length=1000)

    def __str__(self):
        return self.staff.first_name
