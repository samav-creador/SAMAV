# Generated by Django 3.1 on 2021-03-22 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noAbandono', '0006_problematica_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problematica',
            name='grupo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='noAbandono.grupo'),
        ),
    ]
