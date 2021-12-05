from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Staff, AnnualLeave,SickLeave
import datetime
from calendar import monthrange

# Create your tests here.
class StaffTestViews(TestCase):

    def setUp(self):
        staff = Staff.objects.create(
                    id=1, first_name="zahur", last_name='meerun', tax_number=9999, email_address='z@gmail.com', 
                    phone_number=1234565, address='vacoas', birth_date='1976-05-06',
                    gender='Male', management_level='1', entry_date='2021-01-01', 
                    position_held='Manager', basic_salary='50000', transport_allowance='5000',
                    annual_leave=30, annual_leave_remaining=15, sick_leave=20, sick_leave_remaining=10)
        self.actual_year = datetime.datetime.now().strftime("%y")        

    def test_staff_page_with_super_no_user(self):
        response = self.client.get(reverse('staff'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_staff_page_with_no_query(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        response = self.client.get(reverse('staff'), {'q': ''})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/')

    def test_staff_page_with_query(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        response = self.client.get(reverse('staff'), {'q': ''})
        response = self.client.get(reverse('staff'), {'q': 'zahur'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/staff.html')

    def test_staff_details_page_with_no_superuser(self):
        response = self.client.get(reverse('staff_details', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_staff_details_page_with_superuser(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        response = self.client.get(reverse('staff_details', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/staff_details.html')
    
    def test_add_staff_details_page_with_no_superuser(self):        
        data = {
            'username': 'new user name',
        }
        response = self.client.post(reverse('add_staff'), data)     
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_add_staff_details_page_with_superuser_and_valid_form(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')          
        data = {
                'first_name': 'zahur', 'last_name': 'meerun', 'tax_number': 9999, 'email_address':'z@gmail.com', 
                'phone_number': 1234565, 'address': 'vacoas', 'birth_date': '1976-05-06',
                'gender': 'Male', 'management_level': '1', 'entry_date': '2021-01-01', 
                'position_held': 'Manager', 'basic_salary': '50000', 'transport_allowance': '5000',
                'annual_leave': 30, 'annual_leave_remaining': 15, 'sick_leave': 20, 'sick_leave_remaining': 10,
        } 
        response = self.client.post(reverse('add_staff'), data)     
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/')
    
    def test_add_staff_details_page_with_superuser_and_invalid_form(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')          
        data = {
                'first_name': ' ', 'last_name': 'meerun', 'tax_number': 9999, 'email_address':'z@gmail.com', 
                'phone_number': 1234565, 'address': 'vacoas', 'birth_date': '1976-05-06',
                'gender': 'Male', 'management_level': '1', 'entry_date': '2021-01-01', 
                'position_held': 'Manager', 'basic_salary': '50000', 'transport_allowance': '5000',
                'annual_leave': 30, 'annual_leave_remaining': 15, 'sick_leave': 20, 'sick_leave_remaining': 10,
        } 
        response = self.client.post(reverse('add_staff'), data)     
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/add_staff')
    
    def test_update_staff_details_page_with_no_superuser(self):                
        data = {
                'id':1, 'first_name': 'zahur',                
        } 
        response = self.client.post(reverse('update_staff', args=[1]))    
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_update_staff_details_page_with_superuser_and_valid_form(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')                  
        data = {
                'first_name': 'fally', 'last_name': 'meerun', 'tax_number': 9999, 'email_address':'z@gmail.com', 
                'phone_number': 1234565, 'address': 'vacoas', 'birth_date': '1976-05-06',
                'gender': 'Male', 'management_level': '1', 'entry_date': '2021-01-01', 
                'position_held': 'Manager', 'basic_salary': '50000', 'transport_allowance': '5000',
                'annual_leave': 30, 'annual_leave_remaining': 15, 'sick_leave': 20, 'sick_leave_remaining': 10,
        } 
        response = self.client.post(reverse('update_staff', args=[1]), data)  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    
    def test_update_staff_details_page_with_superuser_and_invalid_form(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')                  
        data = {
                'first_name': ' ', 'last_name': 'meerun', 'email_address':'z@gmail.com', 
                'phone_number': 1234565, 'address': 'vacoas', 'birth_date': '1976-05-06',
                'gender': 'Male', 'management_level': '1', 'entry_date': '2021-01-01', 
                'position_held': 'Manager', 'basic_salary': '50000', 'transport_allowance': '5000',
                'annual_leave': 30, 'annual_leave_remaining': 15, 'sick_leave': 20, 'sick_leave_remaining': 10,
        } 
        response = self.client.post(reverse('update_staff', args=[1]), data)  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/update_staff/1')


    def test_delete_staff_with_superuser(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')                  
        
        response = self.client.get(reverse('delete_staff', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/')

    def test_delete_staff_with_no_superuser(self):      
        response = self.client.get(reverse('delete_staff', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_delete_staff_with_superuser(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')                  
        
        response = self.client.get(reverse('delete_staff', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/')

    def test_sick_leave_view_with_no_superuser(self):      
        response = self.client.get(reverse('sick_leave', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_sick_leave_view_with_superuser_invalid_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        data = {
            'start_date': '10/01/2021',
            'end_date': '10/01/2022',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_sick_leave_view_with_superuser_for_different_year(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        data = {
            'start_date': '10/01/2022',
            'end_date': '10/01/2022',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_sick_leave_view_with_superuser_for_incorrect_start_date(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/01/2021',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_different_year_existing_leave_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date='2022-10-5', end_date='2022-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2022',
            'end_date': '10/10/2022',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_sick_leave_view_with_superuser_for_different_year_existing_sick_dates_with_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2022-10-5', end_date='2022-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2022',
            'end_date': '10/10/2022',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_different_year_existing_sick_dates_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2022-10-5', end_date='2022-10-6', 
                    days=5)
        data = {
            'start_date': '9/03/2022',
            'end_date': '9/06/2022',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_different_with_no_existing_leave(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        data = {
            'start_date': '10/05/2022',
            'end_date': '10/10/2022',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_actual_year_existing_leave_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date='2021-10-5', end_date='2021-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/10/2021',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_actual_year_existing_sick_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2021-10-5', end_date='2021-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/10/2021',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_actual_year_existing_sick_dates_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2021-10-5', end_date='2021-10-6', 
                    days=5)
        data = {
            'start_date': '9/05/2021',
            'end_date': '9/10/2021',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser_for_actual_year_no_leave(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        data = {
            'start_date': '9/05/2021',
            'end_date': '9/10/2021',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_sick_leave_view_with_superuser_invalid_form(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        data = {
            'start_date': ' ',
            'end_date': '9/10/2021',
        }        
        response = self.client.post(reverse('sick_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_sick_leave_view_with_superuser(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur') 
        response = self.client.get(reverse('sick_leave', args=[1]))
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response, 'staff/sick_leave.html')    
    
    def test_annual_leave_view_with_no_superuser(self):      
        response = self.client.get(reverse('annual_leave', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_annual_leave_view_with_superuser_invalid_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        data = {
            'start_date': '10/01/2021',
            'end_date': '10/01/2022',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_annual_leave_view_with_superuser_for_different_year(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        data = {
            'start_date': '10/01/2022',
            'end_date': '10/01/2022',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_annual_leave_view_with_superuser_for_incorrect_start_date(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/01/2021',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_different_year_existing_leave_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date='2022-10-5', end_date='2022-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2022',
            'end_date': '10/10/2022',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_annual_leave_view_with_superuser_for_different_year_existing_sick_dates_with_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2022-10-5', end_date='2022-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2022',
            'end_date': '10/10/2022',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_different_year_existing_sick_dates_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2022-10-5', end_date='2022-10-6', 
                    days=5)
        data = {
            'start_date': '9/03/2022',
            'end_date': '9/06/2022',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_different_with_no_existing_leave(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        data = {
            'start_date': '10/05/2022',
            'end_date': '10/10/2022',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_actual_year_existing_leave_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date='2021-10-5', end_date='2021-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/10/2021',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_actual_year_existing_sick_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2021-10-5', end_date='2021-10-6', 
                    days=5)
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/10/2021',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_actual_year_existing_sick_dates_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date='2021-10-5', end_date='2021-10-6', 
                    days=5)
        data = {
            'start_date': '9/05/2021',
            'end_date': '9/10/2021',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser_for_actual_year_no_leave(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        data = {
            'start_date': '9/05/2021',
            'end_date': '9/10/2021',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')

    def test_annual_leave_view_with_superuser_invalid_form(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')        
        data = {
            'start_date': ' ',
            'end_date': '9/10/2021',
        }        
        response = self.client.post(reverse('annual_leave', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/1')
    
    def test_annual_leave_view_with_superuser(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur') 
        response = self.client.get(reverse('annual_leave', args=[1]))
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response, 'staff/annual_leave.html')
    
    def test_sick_leave_taken_view_with_no_superuser(self):        
        response = self.client.get(reverse('sick_leave_taken', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_sick_leave_taken_view_with_superuser_query_All(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')         
        response = self.client.get(reverse('sick_leave_taken', args=[1]), {'q':"All"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/sick_leave_taken.html')
    
    def test_sick_leave_taken_view_with_superuser_query_year(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')         
        response = self.client.get(reverse('sick_leave_taken', args=[1]), {'q':"2021"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/sick_leave_taken.html')
    
    def test_sick_leave_taken_view_with_superuser_no_query(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')         
        response = self.client.get(reverse('sick_leave_taken', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/sick_leave_taken.html')
    
    def test_annual_leave_taken_view_with_no_superuser(self):        
        response = self.client.get(reverse('annual_leave_taken', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_annual_leave_taken_view_with_superuser_query_All(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')         
        response = self.client.get(reverse('annual_leave_taken', args=[1]), {'q':"All"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/annual_leave_taken.html')
    
    def test_annual_leave_taken_view_with_superuser_query_year(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')         
        response = self.client.get(reverse('annual_leave_taken', args=[1]), {'q':"2021"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/annual_leave_taken.html')
    
    def test_annual_leave_taken_view_with_superuser_no_query(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')         
        response = self.client.get(reverse('annual_leave_taken', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/annual_leave_taken.html')
    
    def test_sick_leave_modify_view_with_no_superuser(self):      
        response = self.client.get(reverse('sick_modify', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_sick_leave_modify_view_with_superuser_invalid_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        data = {
            'start_date': '10/01/2021',
            'end_date': '10/01/2022',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_leave_modify_view_with_superuser_invalid_start_date(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/01/2021',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_leave_modify_view_with_superuser_different_year_with_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2022-01-01", end_date='2022-01-05', 
                    days=6)
        sick_two = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6) 
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2022',
            'end_date': '05/01/2022',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')    

    def test_sick_leave_modify_view_with_superuser_different_year_with_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2022-01-01", end_date='2022-01-05', 
                    days=6)
        sick_two = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6) 
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2023',
            'end_date': '05/01/2023',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_leave_modify_view_with_superuser_different_year_no_leave(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2022-01-01", end_date='2022-01-05', 
                    days=6)          
        data = {
            'start_date': '05/01/2023',
            'end_date': '05/01/2023',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_leave_modify_view_with_superuser_same_year_with_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        sick_two = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6) 
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2021',
            'end_date': '05/01/2021',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    

    def test_sick_leave_modify_view_with_superuser_same_year_with_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        sick_two = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6) 
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2021',
            'end_date': '05/01/2021',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_leave_modify_view_with_superuser_same_year_leave_no_overlapping(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-04-01", end_date='2021-04-05', 
                    days=6) 
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                    days=6)          
        data = {
            'start_date': '06/10/2021',
            'end_date': '06/10/2021',
        }        
        response = self.client.post(reverse('sick_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_leave_modify_view_with_superuser_same_year_no_leave(self):
            self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
            self.client.login(
                        username='superuser', password='zahur')            
            sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)          
            data = {
                'start_date': '06/10/2021',
                'end_date': '06/10/2021',
            }        
            response = self.client.post(reverse('sick_modify', args=[1]), data)         
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/staff/sick_leave_taken/1') 
    
    def test_sick_leave_modify_view_with_superuser(self):
            self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
            self.client.login(
                        username='superuser', password='zahur')            
            sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)          
                 
            response = self.client.get(reverse('sick_modify', args=[1]))         
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'staff/sick_modify.html')
    
    def test_sick_leave_modify_view_with_superuser_invalid_form(self):
            self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
            self.client.login(
                        username='superuser', password='zahur')            
            sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)          
            data = {
                'start_date': ' ',
                'end_date': '06/10/2021',
            }        
            response = self.client.post(reverse('sick_modify', args=[1]), data)         
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/staff/sick_leave_taken/1')    
    
    def test_annual_leave_modify_view_with_no_superuser(self):      
        response = self.client.get(reverse('annual_modify', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_annual_leave_modify_view_with_superuser_invalid_dates(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        data = {
            'start_date': '10/01/2021',
            'end_date': '10/01/2022',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_leave_modify_view_with_superuser_invalid_start_date(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        data = {
            'start_date': '10/05/2021',
            'end_date': '10/01/2021',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_leave_modify_view_with_superuser_different_year_with_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6) 
        leave_two = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2022',
            'end_date': '05/01/2022',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')    

    def test_annual_leave_modify_view_with_superuser_different_year_with_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6) 
        leave_two = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2022-05-01", end_date='2022-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2023',
            'end_date': '05/01/2023',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_leave_modify_view_with_superuser_different_year_no_leave(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2023',
            'end_date': '05/01/2023',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_leave_modify_view_with_superuser_same_year_with_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6) 
        leave_two = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2021',
            'end_date': '05/01/2021',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    

    def test_annual_leave_modify_view_with_superuser_same_year_with_no_overlap(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)
        sick = SickLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6) 
        leave_two = AnnualLeave.objects.create(
                    id=2, staff_id=1, start_date="2021-05-01", end_date='2021-05-05', 
                    days=6)         
        data = {
            'start_date': '05/01/2021',
            'end_date': '05/01/2021',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_leave_modify_view_with_superuser_same_year_leave_no_overlapping(self):
        self.user = User.objects.create_superuser(
                    username='superuser', password='zahur')
        self.client.login(
                    username='superuser', password='zahur')
        leave = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-04-01", end_date='2021-04-05', 
                    days=6) 
        sick = SickLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                    days=6)          
        data = {
            'start_date': '06/10/2021',
            'end_date': '06/10/2021',
        }        
        response = self.client.post(reverse('annual_modify', args=[1]), data)         
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_leave_modify_view_with_superuser_same_year_no_leave(self):
            self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
            self.client.login(
                        username='superuser', password='zahur')            
            annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)          
            data = {
                'start_date': '06/10/2021',
                'end_date': '06/10/2021',
            }        
            response = self.client.post(reverse('annual_modify', args=[1]), data)         
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/staff/annual_leave_taken/1') 
    
    def test_annual_leave_modify_view_with_superuser(self):
            self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
            self.client.login(
                        username='superuser', password='zahur')            
            annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)          
                 
            response = self.client.get(reverse('annual_modify', args=[1]))         
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'staff/annual_modify.html')
    
    def test_annual_leave_modify_view_with_superuser_invalid_form(self):
            self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
            self.client.login(
                        username='superuser', password='zahur')            
            annual = AnnualLeave.objects.create(
                    id=1, staff_id=1, start_date="2021-01-01", end_date='2021-01-05', 
                    days=6)          
            data = {
                'start_date': ' ',
                'end_date': '06/10/2021',
            }        
            response = self.client.post(reverse('annual_modify', args=[1]), data)         
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_sick_delete_view_with_no_superuser(self):      
        response = self.client.get(reverse('sick_delete', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_sick_delete_view_with_superuser_with_same_year(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur') 
        sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)         
        response = self.client.get(reverse('sick_delete', args=[1]))        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_sick_delete_view_with_superuser_with_not_same_year(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur') 
        sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2022-05-01", end_date='2022-05-01', 
                        days=6)         
        response = self.client.get(reverse('sick_delete', args=[1]))        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_leave_taken/1')
    
    def test_annual_delete_view_with_no_superuser(self):      
        response = self.client.get(reverse('annual_delete', args=[1]))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_annual_delete_view_with_superuser_with_same_year(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur') 
        annual = AnnualLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)         
        response = self.client.get(reverse('annual_delete', args=[1]))        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')
    
    def test_annual_delete_view_with_superuser_with_not_same_year(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur') 
        annual = AnnualLeave.objects.create(
                        id=1, staff_id=1, start_date="2022-05-01", end_date='2022-05-01', 
                        days=6)         
        response = self.client.get(reverse('annual_delete', args=[1]))        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_taken/1')

    def test_sick_data_view_with_no_superuser(self):      
        response = self.client.get(reverse('sick_data'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_sick_data_view_with_superuser_and_no_query(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')       
        response = self.client.get(reverse('sick_data'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/sick_data.html')
    
    def test_sick_data_view_with_superuser_and_query(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)       
        response = self.client.get(reverse('sick_data'), {'q': '2021'})  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/sick_data.html')
    
    def test_annual_data_view_with_no_superuser(self):      
        response = self.client.get(reverse('annual_leave_data'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_annual_data_view_with_superuser_and_no_query(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')       
        response = self.client.get(reverse('annual_leave_data'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/leave_data.html')
    
    def test_annual_data_view_with_superuser_and_query(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)       
        response = self.client.get(reverse('annual_leave_data'), {'q': '2021'})  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/leave_data.html')
    
    def test_annual_leave_planner_view_with_no_superuser(self):      
        response = self.client.get(reverse('leave_planner'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_annual_leave_planner_view_with_superuser_no_query(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')      
        response = self.client.get(reverse('leave_planner'))  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/leave_planner.html')
    
    def test_annual_leave_planner_view_with_superuser_with_query_no_month(self): 
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')     
        response = self.client.get(reverse('leave_planner'), { 'q': '2022'})  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/leave_planner.html')
    
    def test_annual_leave_planner_view_with_superuser_with_query_and_month(self): 
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-30", end_date='2021-06-02', 
                        days=6)      
        response = self.client.get(reverse('leave_planner'), { 'q': '2021', 'month': '5'})  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/leave_planner.html')
    
    def test_annual_leave_planner_view_with_superuser_with_query_and_same_month(self): 
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-20", end_date='2021-05-25', 
                        days=6)      
        response = self.client.get(reverse('leave_planner'), { 'q': '2021', 'month': '5'})  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/leave_planner.html')
    
    def test_sick_reset_no_superuser(self):      
        response = self.client.get(reverse('sick_reset'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_sick_reset_with_superuser(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')
        sick = SickLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-01", end_date='2021-05-01', 
                        days=6)       
        response = self.client.get(reverse('sick_reset'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/sick_data')

    def test_annual_reset_no_superuser(self):      
        response = self.client.get(reverse('leave_reset'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_annual_reset_with_superuser(self):
        self.user = User.objects.create_superuser(
                        username='superuser', password='zahur')
        self.client.login(
                        username='superuser', password='zahur')
        annual = AnnualLeave.objects.create(
                        id=1, staff_id=1, start_date="2021-05-20", end_date='2021-05-25', 
                        days=6)      
        response = self.client.get(reverse('leave_reset'))  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/staff/annual_leave_data')
    