# Generated by Django 4.0.4 on 2022-05-12 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_applicationmodel_tie_breaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='tie_breaker',
            field=models.IntegerField(verbose_name=404),
        ),
    ]
