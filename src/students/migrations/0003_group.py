# Generated by Django 2.2.9 on 2020-01-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gr_name', models.CharField(max_length=20)),
                ('number_of_students', models.IntegerField()),
                ('curator', models.CharField(max_length=50)),
                ('faculty', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
