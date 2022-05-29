from django.urls import path

from alarm_diagram.views import index

urlpatterns = [
    path("", index, name="index")
]

app_name = "alarm_diagram"
