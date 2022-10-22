from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('login/',views.userLogin),
    path('register/',views.userRegister),
    path('logout/',views.userLogout),
    path('my-notes/',views.getMyNotes),
    path('all-notes/',views.getAllNotes),
    path('note/<str:pk>/',views.getSingleNote),
    path('create/',views.createNote),
    path('update/<str:pk>/',views.updateNote),
    path('delete/<str:pk>/',views.deleteNote)
]