# Generated by Django 4.0.4 on 2022-05-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarm_diagram', '0003_state_alerts_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='alerts_count',
            new_name='alarms_count',
        ),
    ]