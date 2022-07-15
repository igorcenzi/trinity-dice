# Generated by Django 4.0.6 on 2022-07-14 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('journeys', '0001_initial'),
        ('systems', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='creator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journeys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='journey',
            name='system_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journeys', to='systems.system'),
        ),
    ]
