from django.urls import path
from . import views
urlpatterns = [

   path('',views.index,name='index'),
   path('home',views.home,name='home'),
   path('delete/<int:id>/', views.delete, name='delete'),
   path('update/<int:id>/', views.update, name='update'),
   path('cdvListView/',views.TaskListView.as_view(),name='cdvListView'),
   path('cdvDetailView/<int:pk>/', views.TaskDetailView.as_view(), name='cdvDetailView'),
   path('cdvUpdateView/<int:pk>/', views.TaskUpdateView.as_view(), name='cdvUpdateView'),
   path('cdvDeleteView/<int:pk>/', views.TaskDeleteView.as_view(), name='cdvDeleteView')
]