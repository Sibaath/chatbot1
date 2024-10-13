from django.urls import path
# from .views import chatbotResponse
from .views import upload_file
from .views import api1
from .views import chatbotResponse
urlpatterns = [
    # path('OnelifeChatbot/', chatbotResponse, name='chatBotResponse'),
    path('uploadfile/', upload_file, name='upload_file'),
    path('api1/',chatbotResponse,name='chatbotResponse'),
]