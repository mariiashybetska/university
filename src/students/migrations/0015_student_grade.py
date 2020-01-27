# Generated by Django 2.2.9 on 2020-01-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20200127_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Junior'), (2, 'Middle'), (3, 'Senior')], default=2),
            preserve_default=False,
        ),
    ]
