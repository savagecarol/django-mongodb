
from django.urls import path
from .views import home, student_list,detail

urlpatterns = [
    path('serial/', home, name='home'),
    path('', student_list),
path('<int:pk>/', detail)
]
