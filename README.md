# **Workforce**

## TABLE OF CONTENT 
* [Introduction](#introduction)    
* [UX](#ux)
    * [UX design work overview](#ux-design-work-overview)    
* [Installation](#installation)
* [Technologies used](#technologies-used)
* [CRUD Authorisation and Security Features](#crud-authorisation-and-security-features)
* [Testing](#testing)
* [Features](#features)
    * [Staff Profile Management](#staff-profile-management)
    * [Sick and Annual Leave](#sick-and-annual-leave)
    * [Leave Data](#leave-data)
    * [Pay Management](#pay-management)
* [Contact](#contact)   


## INTRODUCTION 

This project will give employers the ability to have a centralised database of all it employees details.
The program is divided into 3 parts consisting of:
1. Staff details: name, date of birth etc..
2. Staff sick and annual leava management
3. Pay management


## UX 

By using this site as the site owner:

* be able to add, update and delete staff and their details.
* provide basic details for staff.
* be able to add record of sick and annual leave for staff.
* be able to add modify, delete record of sick and annual leave for staff.
* be able to view sick and annual leave data graphically for management purposes
* be able to generate, modify and store monthly pay for staff
* be able control access to the store management page and features.

## INSTALLATION

* clone repo 
* run ```pip install -r requirements.txt```
* run ```python manage.py makemigrate```
* run ```python manage.py migrate```
* run ```python manage.py createsuperuser```
* run ```python manage.py runserver```

## TECHNOLOGIES USED

* HTML5
* css 
* javacript (ES6)
* python (v3.8.6)
* Django framework
* SQL database
* Amazon web servives for production storage of static and media files
* Jquery to simplify DOM manipulation
* pylint, flake8 PEP8 compliancex 
* Chrome developers tools for analysing scripts and debugging
* Boostrap 4 for :
    1. page layout purposes and responsive design aspects
    2. Forms 
    3. Modals    
    4. Navbar
    5. Footer
* Chrome extension 'responsive viewer' to aid in responsive design
* Google distance matrix to calculate delivery time 

## CRUD AUTHORISATION AND SECURITY FEATURES

The site requires sign-in to access and manipulate any data. Any CRUD operations performed without sign-in will force a redirect by using django's ```if not request.user.is_superuser``` feature.

## TESTING

Unitest was done with TestCase giving a coverage of 91%.

## FEATURES

The site can be divided into 3 part consisting of staff profile management, sick and annual leave management and pay management. 

The staff management section combines the staff detail and sick and annual leave features.

### STAFF PROFILE MANAGEMENT

The main page consists of the list of current staff employed plus link to add staff. A search bar feature is also included to allow user to find staff by first and last name.

![sign-in](static/doc/main-page.jpg)

The add staff link will provide a form to add staff with several required fields.

![add-staff](static/doc/add-staff.jpg)

The staff detail page lists all the details of the staff entered into the form. This page also allows deleting of staff profile or updating any details.  Links are also provided for adding sick and annual leave taken by staff.

A confirmation modal is provided for any deletion of staff as a safety measure.

![staff-details](static/doc/staff-details.jpg)

### SICK AND ANNUAL LEAVE
 
To add sick or annual leave one must navigate to the staff details page and click on add sick/annual leave. This will open up a form requiring the relevant details.

![add-sick](static/doc/add-sick.jpg)

Logic has been put in place to prevent overlapping of dates of exsiting sick leave or annual leave. This also caters for overlapping of sick and annual leave. 

Also the date field can only over one year period. If the leave covers two year periods, then 2 inputs are required.

One can view all leave taken by the staff by navigating to staff details page and clicking on the view link. This will bring up a page listing all the leave taken by that specific staff. The resulsts can also be categorised by year.

![staff-leave](static/doc/staff-leave.jpg)

This page also provides the option to update or delete the selected leave.

### LEAVE DATA

Another useful option is the ability to view leave data for all staff in centralised page instead of navigating to each staff individually. From the main staff page one can click on sick data or leave data to open up this view.

![sick-data](static/doc/sick-data.jpg)

![leave-data](static/doc/leave-data.jpg)

The results can be further filtered down by year to allow easier viewing.

![leave-data-filter](static/doc/leave-data-filter.jpg)

Another helpful feature is the ability to view both sick and leave data graphically. 

Once a year is selected from the sick data page a graph button will appear which will allow viewing of sick data for that year month by month. The graph provides the total amount of man days taken for that month. Thus allowing valuable data analysis.

![sick-data-graph](static/doc/sick-data-graph.jpg)

For the annual leave the working is slightly different. To access leave data one must click the leave planner button on the leave data page.

![leave-planner-button](static/doc/leave-planner-button.jpg)

This will open up a new page were a year and month must be selected. This will provide data on the staff who have taken leave in that period plus provide a useful graph indicating how many staff are taking leave on a specific day. This can be helpful when one needs to have control on the amount of manpower
who are taking leave in a certain period.

![leave-days](static/doc/leave-days.jpg)

The reset sick and annual leave button will force a reset of the remaining sick/annnual leave counter. This should normally be performed on the 1st of each year to update employee details for that year.

### PAY MANAGEMENT
The main pay management page consists of a list of all staff in database with search bar.

![Main-pay](static/doc/pay-main.jpg)

Selecting a staff will bring-up a list of all salaries created for that staff. This page also provides all CRUD functionality links for deleting, updating and creating salaries for that staff.

![salary-details](static/doc/salarydetails.jpg)

Clicking on the add salary button will open up a form to create salary using the employee information entered at staff creation.

![Salary-form](static/doc/salary-form.jpg)

Clicking the view button will generate a salary slip view where one can preview the payment details.

![Salary-slip](static/doc/salary-slip.jpg)

Clicking the 'download pdf ' button will generate a pdf for that salary for distribution purposes.

![Salary-pdf](static/doc/salary-pdf.jpg)

### CONTACT
For login credential or any queries please contact me on zahurmeerun@hotmail.com. 