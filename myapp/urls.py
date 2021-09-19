from django.urls import path
from myapp import views

urlpatterns = [
    path('devices/', views.get_data),

]
