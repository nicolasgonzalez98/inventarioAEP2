# Generated by Django 4.0.2 on 2023-08-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockaep', '0020_alter_hardware_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='observaciones',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        
    ]