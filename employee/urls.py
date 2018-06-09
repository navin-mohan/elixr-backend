from django.urls import path
from . import views

urlpatterns = [
    path('<int:emp_type>/',views.get_emp_list),
    path('dev/<int:emp_id>/',views.get_dev),
    # path('pm/<int:pm_id>/',views.get_pm)
]