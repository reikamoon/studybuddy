from django.urls import path
from . import views
from schedule.views import ClassDetailView, AddClass, DeleteClass, UpdateClass

urlpatterns = [
    path('schedule/', views.schedule_index, name="schedule"),
    path('add-class/', AddClass.as_view(),name='addclass'),
    path('<str:slug>/', ClassDetailView.as_view(), name='class-details-page'),
    path('<str:slug>/edit', UpdateClass.as_view(), name='edit-class'),
    path('<str:slug>/delete/', DeleteClass.as_view(), name='delete-class'),
]
