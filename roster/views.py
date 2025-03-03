import csv
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Employee
from .forms import CSVUploadForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import calendar



from .models import Csv
import csv
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'roster/signup.html', {'form': form})

def logout(request):
    return render(request, 'roster/logout.html')


def home_view(request):
    return render(request, 'roster/home.html')

@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            csv_data = csv_file.read().decode('UTF-8')
            lines = csv_data.splitlines()
            reader = csv.DictReader(lines)
            
            employees = []
            for row in reader:
                employee_id = row.get('Employee ID')
                name = row.get('Name')
                
                # Check if the employee already exists
                employee, created = Employee.objects.get_or_create(
                    employee_id=employee_id,
                    defaults={'name': name}
                )
                
                if not created:
                    # If the employee already exists, update the name or handle duplicates
                    employee.name = name
                    employee.save()
                
                employees.append(employee)
            
            # Process the shift schedule for the uploaded employees
            process_schedule(employees)

            # Return JSON response with a success message
            return JsonResponse({'message': 'CSV uploaded and processed successfully.'})
    else:
        form = CSVUploadForm()
    
    return render(request, 'roster/upload_csv.html', {'form': form})

def process_schedule(employees):
    # Assign shifts and week off for each employee
    shifts = ['9am-5pm', '1pm-9pm', '5am-1pm']
    week_off_rotation = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i, employee in enumerate(employees):
        employee_shift = {
            'Monday': shifts[i % len(shifts)],
            'Tuesday': shifts[i % len(shifts)],
            'Wednesday': shifts[i % len(shifts)],
            'Thursday': shifts[i % len(shifts)],
            'Friday': shifts[i % len(shifts)],
            'Saturday': shifts[i % len(shifts)],
            'Sunday': shifts[i % len(shifts)],
            'Week Off': week_off_rotation[i % len(week_off_rotation)],
        }
        
        # Save the shift schedule to the database or any other storage
        # Here you might want to create a new model or update the Employee model to include shift information
        # For example:
        # employee.monday_shift = employee_shift['Monday']
        # employee.week_off = employee_shift['Week Off']
        # employee.save()

        print(f"Processed schedule for {employee.name}: {employee_shift}")
        

# def download_schedule(request):
#     # Fetch all employees from the database
#     employees = Employee.objects.all()

#     # Define shifts and week off rotation
#     shifts = ['shift1', 'shift2', 'shift3']
#     week_off_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#     # Get the current month and year
#     current_year = datetime.now().year
#     current_month = datetime.now().month

#     # Find out the number of days in the current month
#     _, num_days = calendar.monthrange(current_year, current_month)

#     # Create the HttpResponse object with the appropriate CSV header
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = f'attachment; filename="employee_schedule_{current_year}_{current_month}.csv"'

#     writer = csv.writer(response)
    
#     # Define the header for the CSV file
#     header = ['Employee ID', 'Name'] + [f'{current_month}/{day}' for day in range(1, num_days + 1)]
#     writer.writerow(header)

#     for i, employee in enumerate(employees):
#         # Initialize the row with employee ID and name
#         employee_shift = [
#             employee.employee_id,
#             employee.name,
#         ]

#         # Determine the specific week off day for the employee
#         week_off_day = week_off_days[i % len(week_off_days)]

#         # Loop through each day of the month and assign shifts
#         for day in range(1, num_days + 1):
#             current_date = datetime(current_year, current_month, day)
#             shift = shifts[(i + day) % len(shifts)]  # Assign shift based on the day

#             # Check if this day matches the employee's week off day
#             if current_date.strftime('%A') == week_off_day:
#                 employee_shift.append('OFF')  # Mark the day as OFF
#             else:
#                 employee_shift.append(shift)  # Assign the regular shift

#         # Write the shift schedule to the CSV file
#         writer.writerow(employee_shift)

#     return response


def download_schedule(request):
    if request.method == 'POST':
        # Get the month and year from the user's input
        current_year = int(request.POST.get('year'))
        current_month = int(request.POST.get('month'))
        
        # Fetch all employees from the database
        employees = Employee.objects.all()

        # Define shifts and week off rotation
        shifts = ['shift1', 'shift2', 'shift3']
        week_off_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        # Find out the number of days in the specified month
        _, num_days = calendar.monthrange(current_year, current_month)

        # Create the HttpResponse object with the appropriate CSV header
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="employee_schedule_{current_year}_{current_month}.csv"'

        writer = csv.writer(response)
        
        # Define the header for the CSV file
        header = ['Employee ID', 'Name'] + [f'{current_month}/{day}' for day in range(1, num_days + 1)]
        writer.writerow(header)

        for i, employee in enumerate(employees):
            # Convert employee ID to integer (if it's not already an integer)
            employee_id = int(employee.employee_id)

            # Initialize the row with employee ID and name
            employee_shift = [
                employee_id,
                employee.name,
            ]

            # Determine the specific shift for this employee based on their ID
            shift = shifts[(employee_id - 1) % len(shifts)]

            # Determine the specific week off day for the employee
            week_off_day = week_off_days[i % len(week_off_days)]

            # Loop through each day of the month and assign shifts
            for day in range(1, num_days + 1):
                current_date = datetime(current_year, current_month, day)

                # Check if this day matches the employee's week off day
                if current_date.strftime('%A') == week_off_day:
                    employee_shift.append('OFF')  # Mark the day as OFF
                else:
                    employee_shift.append(shift)  # Assign the specific shift for the employee

            # Write the shift schedule to the CSV file
            writer.writerow(employee_shift)

        return response

    # Render a form to get the month and year from the user
    return render(request, 'roster/download.html')
