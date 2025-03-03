from django.urls import path, include
from django.http import HttpResponseRedirect
from django.contrib import admin
from roster.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', lambda request: HttpResponseRedirect('/schedule/')),  # Redirect root URL to /schedule/
    path('login/', auth_views.LoginView.as_view(template_name='roster/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('upload/', upload_csv, name='upload_csv'),
    path('home/', home_view, name='home_view'),
    path('download/', download_schedule, name='download_schedule'),
    # path('schedule/', process_schedule, name='schedule_complete'),
]


