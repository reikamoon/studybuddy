# Generated by Django 3.0.2 on 2020-07-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20200629_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='time',
            field=models.CharField(default='12:00pm-1:30pm', help_text='Enter a time', max_length=20),
        ),
    ]