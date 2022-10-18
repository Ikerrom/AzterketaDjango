from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('kotxeak/', views.kotxeak, name='kotxeak'),
    path('pertsonak/', views.pertsonak, name='pertsonak'),

    path('delpertsona/<int:id>', views.delpertsona, name='delpertsona'),
    path('delkotxea/<int:id>', views.delkotxea, name='delkotxea'),

    path('addpertsona/', views.addpertsona, name='addpertsona'),

    path('addpertsona/addpertsonatodb/', views.addpertsonatodb, name='addpertsonatodb'),
    path('addkotxeatodb/', views.addkotxeatodb, name='addkotxeatodb'),

    path('updatepertsona/<int:id>', views.updatepertsona, name='updatepertsona'),
    path('updatepertsona/updatepertsonaondb/<int:id>', views.updatepertsonaondb, name='updatepertsonaondb'),

    path('updatekotxea/<int:id>', views.updatekotxea, name='updatekotxea'),
    path('updatekotxea/updatekotxeaondb/<int:id>', views.updatekotxeaondb, name='updatekotxeaondb'),

    path('alokatu/<int:id>', views.alokatu, name='alokatu'),
    path('alokatu/alokatuondb/<int:id>', views.alokatuondb, name='alokatuondb'),
]