from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('user.urls')),

    path('', include('leave.urls')),

    path('', include('salary.urls')),

    # path('', include('telegram.urls')),
    
    path('', include('recruitment.urls')),

    path('', include('attendance.urls')),
    
    path('', include('document.urls')),
    
    path('', include('reports.urls')),
    
    path('', include('feedback.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)