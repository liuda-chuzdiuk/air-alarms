from django.db import models


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    alarms_count = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.state_id}: {self.name_en}"


class Alarm(models.Model):
    id = models.IntegerField(primary_key=True)
    state_id = models.ForeignKey(to=State, on_delete=models.CASCADE)
    alert = models.BooleanField()

    def __str__(self):
        return f"{self.id} - {self.state_id} ({self.alert})"
