from django.urls import path
from . import views
from assignments.views import AssignmentDetailView, CreateAssignment

urlpatterns = [
    path('', views.index, name="home"),
    path('new-assignment/', CreateAssignment.as_view(),name='new'),
    path('<str:slug>/', AssignmentDetailView.as_view(), name='assignment-details-page'),
]
