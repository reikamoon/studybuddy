# Generated by Django 3.0.2 on 2020-07-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_auto_20200617_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(help_text='Enter class name.', max_length=200)),
                ('class_link', models.URLField(help_text='Add a link to class sessions (ex: Zoom)')),
                ('days', models.CharField(default='Mondays', help_text='What Days of the Week do I need to attend?', max_length=200)),
                ('time', models.CharField(default='12:00pm-1:30pm', help_text='Enter a time', max_length=20)),
                ('syllabus', models.URLField(blank=True, help_text='[Optional]Add a link to the Syllabus.', null=True)),
                ('tracker', models.URLField(blank=True, help_text='[Optional]Add a link to class tracker.', null=True)),
                ('grades', models.URLField(blank=True, help_text='[Optional]Add a link to grades for this class.', null=True)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL Path to access this page.', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
    ]
