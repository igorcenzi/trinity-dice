# Generated by Django 4.0.6 on 2022-07-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='type',
            field=models.CharField(choices=[('Buff', 'Buff'), ('Debuff', 'Debuff')], default='Buff', max_length=50),
        ),
    ]
