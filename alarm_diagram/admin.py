from django.contrib import admin

from alarm_diagram.models import State, Alarm


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Alarm)
class AlarmAdmin(admin.ModelAdmin):
    pass
