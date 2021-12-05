# **Workforce**

## TABLE OF CONTENT 
* [Introduction](#introduction)    
* [UX](#ux)
    * [UX design work overview](#ux-design-work-overview)    
* [Installation](#installation)
* [Testing](#testing)
* [Features](#features)
    * [Staff Management](#staff-management) 


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

## TESTING

Unitest was done with TestCase giving a coverage of 91%.

## FEATURES

The site can be divided into 3 part consisting of staff detail management, sick and annual leave management and pay management. 

The staff management section combines the staff detail and sick and annual leave features.

### STAFF MANAGEMENT

The main page consists of the list of current staff employed plus link to add staff.

![sign-in](static/doc/main-page.jpg)

The add staff link will provide a form to add staff with several required fields.

![add-staff](static/doc/add-staff.jpg)

The staff detail page lists all the details of the staff entered into the form. This page also allows deleting of staff profile or updating any details.  Links are also provided for adding sick and annual leave taken by staff.

A confirmation modal is provided for deletion of staff as safety measure.

![staff-details](static/doc/staff-details.jpg)