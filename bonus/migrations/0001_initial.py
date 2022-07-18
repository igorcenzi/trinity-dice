# Generated by Django 4.0.6 on 2022-07-18 20:56

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('precision', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('type', models.CharField(choices=[('Buff', 'Buff'), ('Debuff', 'Debuff')], default='Buff', max_length=50)),
            ],
        ),
    ]
