from django.contrib import admin
from django.urls import path
from association import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage  URLs
    path('', views.index, name='index'),
    
    # Members URLs
    path('members/', views.member_list, name='member_list'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/<int:member_id>/update/', views.member_update, name='member_update'),
    path('members/<int:member_id>/delete/', views.member_delete, name='member_delete'),

    # Events URLs
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:event_id>/update/', views.event_update, name='event_update'),
    path('events/<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),
    path('faire-un-don/', views.faire_un_don, name='faire_un_don'),
    path('contact/', views.nous_contacter, name='nous_contacter'),
    path('carriere/', views.carriere, name='carriere'),
    path('register/', views.register_event, name='register_event'),
    path('actualites/', views.actualites, name='actualites'),
    path('evenements/', views.evenements, name='evenements'),

]

