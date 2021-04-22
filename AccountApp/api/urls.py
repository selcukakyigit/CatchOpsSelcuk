from  django.urls import path
from AccountApp.api.views import registration_view


app_name='AccountApp_api'
urlpatterns = [
path('register/',registration_view,name='registration'),
]