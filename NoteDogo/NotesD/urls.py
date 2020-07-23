from django.urls import path

from NotesD import views

urlpatterns = [
    path('',views.home, name="home"),
    path('create',views.create, name="create"),
    path('delete/<int:id>/',views.dele, name="delete"),
    path('edit/<int:id>/',views.edit, name="edit"),
]