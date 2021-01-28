# Generated by Django 3.1.5 on 2021-01-28 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_device', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='used_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='user_device.workers'),
        ),
    ]