# Generated by Django 3.0.2 on 2020-06-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_class_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='days',
            field=models.CharField(default='Mondays', help_text='What Days of the Week do I need to attend?', max_length=200),
        ),
    ]
