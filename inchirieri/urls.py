from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('adauga/', views.adauga_masina, name='adauga_masina'),
    path('recenzie/<int:car_id>/', views.adauga_recenzie, name='adauga_recenzie'),
    path('editare/<int:car_id>/', views.editeaza_masina, name='editeaza_masina'),
    path('stergere/<int:car_id>/', views.sterge_masina, name='sterge_masina'),
    path('despre/', views.despre_utilizator, name='despre_utilizator'),
    path('inchiriaza/<int:masina_id>/', views.inchiriaza_masina, name='inchiriaza_masina'),
    path('elimina-inchiriere/<int:inchiriere_id>/', views.elimina_inchiriere, name='elimina_inchiriere'),
    path('sterge-recenzie/<int:recenzie_id>/', views.sterge_recenzie, name='sterge_recenzie'),
]

