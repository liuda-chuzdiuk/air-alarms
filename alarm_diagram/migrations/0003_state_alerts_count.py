# Generated by Django 4.0.4 on 2022-05-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alarm_diagram', '0002_alarm'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='alerts_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]