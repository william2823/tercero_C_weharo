from django.urls import path
from . import views

urlpatterns = [
    path('', views.homedef),

    path('edicioncine/<codigo>', views.edicioncine),
    path('editarcine/', views.editarcine),
    path('eliminarcine/<codigo>', views.eliminarcine),
]