from django.urls import path
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,  # 👈 nuevo import
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('nuevo/', ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/editar/', ServiceUpdateView.as_view(), name='service_update'),
    path('<int:pk>/eliminar/', ServiceDeleteView.as_view(), name='service_delete'),  
]
