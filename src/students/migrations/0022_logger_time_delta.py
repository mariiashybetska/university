# Generated by Django 2.2.9 on 2020-02-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0021_remove_logger_time_delta'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='time_delta',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
