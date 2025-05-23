from django.urls import path
from . import views
from .views import generate_ticket

urlpatterns = [
    #path('home/', views.home, name='home'),
    #path('ce/', views.liste_evenements, name='home'),

    path('', views.home, name='home'),
    path('creerEvent/', views.creer_evenement, name='creerEvent'),
    path('register_evenements/<int:event_id>/', views.register_event, name='register_event'),
    path('history/', views.participation_history, name='history'),
    path('annuler/<int:participation_id>/', views.annuler_participation, name='cancel_participation'),
    path('ticket/<int:participation_id>/', generate_ticket, name='download_ticket'),
    path('my-events/', views.my_events, name='my_events'),  # Nouvelle URL pour mes événements
    path('annuler-evenement/<int:event_id>/', views.annuler_evenement, name='annuler_evenement'),
     path('list_of_part/<int:event_id>/', views.liste_participants, name='liste'),
    
    
]

