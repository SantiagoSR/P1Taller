# Generated by Django 3.0.4 on 2020-03-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminosity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='luminosity',
            name='type',
            field=models.CharField(default='lux', max_length=20, verbose_name='Tipo'),
            preserve_default=False,
        ),
    ]