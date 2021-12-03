from django.contrib import admin
from django.urls import path

from common.views import HomePageView, HelpView
from centers.views import CenterView, CenterDoneView
from rooms.views import RoomView, RoomDoneView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('chci-pomoci/', HelpView.as_view(), name='help'),
    path('mam-ordinaci/', RoomView.as_view(), name='room'),
    path('mam-ordinaci/hotovo/', RoomDoneView.as_view(), name='room-done'),
    path('existujici-misto/', CenterView.as_view(), name='center'),
    path('existujici-misto/hotovo/', CenterDoneView.as_view(), name='center-done'),
    path('admin/', admin.site.urls),
]
