from django.urls import path
from . import views
from schedule.views import *
from assignments.views import AssignmentDetailView, CreateAssignment, DeleteAssignment, UpdateAssignment

urlpatterns = [
    path('', views.index, name="home"),
    path('new-assignment/', CreateAssignment.as_view(),name='new'),
    path('<str:slug>/', AssignmentDetailView.as_view(), name='assignment-details-page'),
    path('<str:slug>/edit', UpdateAssignment.as_view(), name='edit-assignment'),
    path('<str:slug>/delete/', DeleteAssignment.as_view(), name='delete-assignment'),
]
