# Generated by Django 4.2.4 on 2023-09-30 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disability_type', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('event_type', models.CharField(max_length=50)),
                ('attendees', models.ManyToManyField(blank=True, related_name='events_attending', to='association.member')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_organized', to='association.member')),
            ],
        ),
    ]
