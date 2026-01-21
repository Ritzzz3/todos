from django.urls import path
from .views import*

urlpatterns = [
    path('', add_task, name='home'),
    path('update/<int:task_id>/', update_task , name='update'),
    path('delete/<int:task_id>/', delete , name='delete')
]
