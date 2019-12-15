# Generated by Django 2.2.7 on 2019-12-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='latest_status',
        ),
        migrations.RemoveField(
            model_name='status',
            name='latest_update',
        ),
        migrations.AddField(
            model_name='status',
            name='latest_power_state',
            field=models.CharField(choices=[('600', 'Device on'), ('610', 'Device in hibernation'), ('620', 'Device off')], default='620', max_length=3),
        ),
        migrations.AddField(
            model_name='status',
            name='latest_power_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='status',
            name='latest_status_code',
            field=models.CharField(choices=[('200', 'OK'), ('202', 'Received and accepted'), ('400', 'Bad request'), ('404', 'Not found'), ('405', 'Method not allowed'), ('500', 'Internal error on device')], default='200', max_length=3),
        ),
        migrations.AddField(
            model_name='status',
            name='latest_status_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
