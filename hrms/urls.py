from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('user.urls')),

    path('', include('leave.urls')),

    path('', include('salary.urls')),

    # path('', include('telegram.urls')),

    path('', include('attendance.urls')),
]