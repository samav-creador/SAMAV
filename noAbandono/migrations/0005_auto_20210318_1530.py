# Generated by Django 3.1 on 2021-03-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noAbandono', '0004_auto_20210318_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
