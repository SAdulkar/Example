# Generated by Django 3.1 on 2024-03-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
