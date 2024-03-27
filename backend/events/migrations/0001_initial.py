# Generated by Django 5.0.3 on 2024-03-27 20:00

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('is_public', models.BooleanField(default=False)),
                ('color', models.CharField(default='#ffffff', max_length=7)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'events',
                'verbose_name_plural': 'events',
                'db_table': 'events',
                'ordering': ('-pk',),
            },
        ),
    ]
