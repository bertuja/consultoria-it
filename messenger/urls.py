from django.urls import path
from .views import inbox, conversation, send_message, new_message

urlpatterns = [
    path('', inbox, name='inbox'),
    path('<int:user_id>/', conversation, name='conversation'),
    path('send/<int:user_id>/', send_message, name='send_message'),
    path('new/<int:receiver_id>/', new_message, name='new_message'),
]
