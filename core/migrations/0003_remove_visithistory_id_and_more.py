# Generated by Django 4.0 on 2022-01-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_visithistory_userprofile_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visithistory',
            name='id',
        ),
        migrations.AlterField(
            model_name='visithistory',
            name='visited_date',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]
