# Django Registration & Login System

**Project Completed By:** Safir Ahmad  
**Email:** pellowdeveloper@gmail.com  
**Phone Number:** 03497290988  

---

## Project Overview

This is a fully functional **User Registration and Login system** built using **Django**, The system implements secure authentication and allows users to:

- Register with **Email OTP verification**
- Login securely
- Update their **profile details** including:
  - First Name
  - Last Name
  - Email
  - Password
  - Mobile Number
  - Profile Picture
- View all personal information on a **dashboard**
- Upload and display profile images dynamically

---

## Key Features

### **Authentication**
- Secure password hashing via Django’s built-in user model
- OTP verification for email during registration
- Login and logout functionality
- User sessions managed securely

### **Profile Management**
- Dashboard for logged-in users
- Upload and display **profile picture**
- Update personal information (name, email, phone, password)
- Information is rendered dynamically per user


## User Registration & Validation
The registration system ensures secure and consistent user data. It includes the following validations:
Unique Username – Each username must be unique; users cannot register with a username that already exists in the database.
Unique Email – Each email must be unique; duplicate email addresses are not allowed.
Password Confirmation – Users must enter the password twice, and both entries must match to ensure accuracy.
These validations provide a robust and user-friendly registration process, preventing duplicate accounts and minimizing input errors. Combined with email OTP verification, this ensures that only legitimate users can create accounts and access the system.

⚠️ Note: Although the original project specification mentioned Next.js and FastAPI, this implementation leverages Django along with HTML, CSS, and JavaScript to create a fully functional authentication and dashboard system. This project highlights my solid understanding of user management, secure authentication, and dynamic interface development. I am confident in working with Django REST Framework, FastAPI, or other modern technologies, and I am ready to quickly adapt and contribute to delivering high-quality solutions for your team.


### **Frontend**
- Clean and responsive UI with **HTML, CSS, and JavaScript**
- Form validation and user-friendly messages
- Circular profile picture display

### **Backend**
- Django framework for robust backend and authentication
- SQLite database for data storage (can be switched to PostgreSQL/MySQL)
- REST-like design pattern in views
- Ready for integration with **Django REST Framework** if needed

---

## Technologies Used
- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (Django default)  
- **Email:** Django email backend for OTP  
- **Version Control:** Git & GitHub  


---

## How to Run 
⚠️ Note: You must install python , django , django rest framework in your computer

1. Clone the repository:  
   git clone https://github.com/YourUsername/RepositoryName.git
   

2. Open the  the repository :
  python manage.py makemigrations
  python manage.py migrate


3.i have already createsuperuser if you want can delete the complete database and from start makemigrations , and after create createsuperuser otherwise username='ahmad' & password=khan1122
python manage.py createsuperuser 

4.python manage.py runserver
 

   
