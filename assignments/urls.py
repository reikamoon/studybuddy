from django.urls import path
from . import views
from schedule.views import *
from assignments.views import AssignmentDetailView, CreateAssignment, DeleteAssignment, UpdateAssignment, ClassDetailView, AddaClass, DeleteClass, UpdateClass

urlpatterns = [
    path('', views.index, name="home"),
    path('schedule/', views.schedule_index, name="schedule"),
    path('new-assignment/', CreateAssignment.as_view(),name='new'),
    path('add-class/', AddClass.as_view(),name='addclass'),
    path('<str:slug>/', AssignmentDetailView.as_view(), name='assignment-details-page'),
    path('<str:slug>/class/', ClassDetailView.as_view(), name='class-details-page'),
    path('<str:slug>/edit', UpdateAssignment.as_view(), name='edit-assignment'),
    path('<str:slug>/class/edit/', UpdateClass.as_view(), name='edit-class'),
    path('<str:slug>/delete/', DeleteAssignment.as_view(), name='delete-assignment'),
    path('<str:slug>/class/delete/', DeleteClass.as_view(), name='delete-class'),
]
