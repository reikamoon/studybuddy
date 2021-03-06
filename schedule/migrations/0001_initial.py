# Generated by Django 3.0.2 on 2020-06-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(help_text='Enter class name.', max_length=200)),
                ('class_link', models.URLField(help_text='Add a link to class sessions (ex: Zoom)')),
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
