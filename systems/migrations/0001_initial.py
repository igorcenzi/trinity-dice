# Generated by Django 4.0.6 on 2022-07-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dice', models.IntegerField()),
                ('version', models.DecimalField(decimal_places=2, max_digits=16)),
                ('is_active', models.BooleanField(default=True)),
                ('classes', models.ManyToManyField(related_name='systems', to='classes.class')),
            ],
        ),
    ]
