from django.urls import path

from .views import SnackDetailView,SnackListView,SnackCreateView,SnackUpdateView,SnackDeleteView
urlpatterns = [

    path('',SnackListView.as_view(),name='snack-list'),
    path('<int:pk>',SnackDetailView.as_view(),name='snack-detail'),
    path('snack-create',SnackCreateView.as_view(),name='snack-create'),
    path('<int:pk>/update',SnackUpdateView.as_view(),name='snack-update'),
    path('<int:pk>/delete',SnackDeleteView.as_view(),name='snack-delete'),
]