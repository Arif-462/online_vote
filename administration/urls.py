from django.urls import path
from . import views
urlpatterns = [
    path('dashborad/',views.dashboard,name='dashboard'),
    path('myprofile/',views.voters_home,name='myprofile'),


    path('position/',views.position, name='position'),
    path('add_position/',views.add_position, name='add_position'),
    path('edit_position/<int:id>/',views.edit_position, name='edit_position'),
    path('delete_position/<int:id>/',views.delete_position, name='delete_position'),

    path('voters/',views.voters, name='voters'),
    path('edit_voter/<int:id>/',views.edit_voter, name='edit_voter'),
    path('delete_voter/<int:id>/',views.delete_voter, name='delete_voter'),
    
    
    path('candidate/',views.show_candidate, name='candidate'),
    path('create_candidate/',views.create_candidate, name='create_candidate'),
    path('edit_candidate/<int:id>/',views.edit_candidate, name='edit_candidate'),
    path('delete_candidate/<int:id>/',views.delete_candidate, name='delete_candidate'),
    
    
]
