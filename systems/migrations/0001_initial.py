# Generated by Django 4.0.6 on 2022-07-20 04:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dice', models.IntegerField()),
                ('version', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ManyToManyField(related_name='systems', to='classes.class')),
            ],
        ),
    ]
