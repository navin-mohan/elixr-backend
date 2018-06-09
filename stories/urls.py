from django.urls import path

from . import views

urlpatterns = [
    # path('pm/stories/<int:pm_id>/',views.get_pm_stories),
    path('cor/',views.corelation),
]