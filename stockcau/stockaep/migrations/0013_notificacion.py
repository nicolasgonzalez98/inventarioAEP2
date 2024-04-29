# Generated by Django 4.0.2 on 2023-08-24 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockaep', '0012_estado_alter_hardware_options_alter_marca_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizado', models.BooleanField(default=False)),
                ('hardware', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stockaep.hardware')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]