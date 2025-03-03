# Employee Shift Management System

## Overview
This Django-based application allows users to:
- Sign up and log in to the system.
- Upload employee details via CSV.
- Process and assign work shifts to employees.
- Generate and download a CSV file containing employee shift schedules.

## Features
- **User Authentication**: Users can sign up, log in, and log out securely.
- **CSV Upload**: Upload employee details to store in the database.
- **Automatic Shift Assignment**: Assigns shifts to employees in a rotating pattern.
- **CSV Download**: Generates and downloads shift schedules for employees.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (3.x)
- Django (latest version)
- Virtual environment (recommended)

### Setup
1. **Clone the repository**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment and activate it**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin user.

6. **Start the Django development server**
   ```sh
   python manage.py runserver
   ```

## Usage
### 1. User Authentication
- Visit `http://127.0.0.1:8000/signup/` to create an account.
- Log in to access features.

### 2. Upload Employee CSV
- Navigate to `http://127.0.0.1:8000/upload_csv/`.
- Upload a CSV file with employee details (`Employee ID`, `Name`).
- The system will process and store the data.

### 3. Download Shift Schedule
- Navigate to `http://127.0.0.1:8000/download_schedule/`.
- Select the month and year.
- Download the generated shift schedule in CSV format.

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/signup/` | GET, POST | User registration |
| `/upload_csv/` | GET, POST | Upload employee CSV |
| `/download_schedule/` | GET, POST | Generate and download schedule |

## File Structure
```
project_root/
│── roster/
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── views.py        # Application logic
│   ├── models.py       # Database models
│   ├── forms.py        # Form handling
│   ├── urls.py         # URL routing
│── static/             # Static files (CSS, JS)
│── manage.py           # Django management script
│── db.sqlite3          # SQLite database
│── requirements.txt    # Project dependencies
```

## Technologies Used
- Django (Python)
- HTML/CSS (Frontend templates)
- JavaScript (Frontend enhancements)
- SQLite (Database)

## Future Enhancements
- Improve UI/UX for shift schedule visualization.
- Add email notifications for assigned shifts.
- Implement role-based access control.



