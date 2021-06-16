# Generated by Django 3.2.3 on 2021-06-16 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0006_auto_20210616_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencia',
            name='cupos',
            field=models.SmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='conferencia',
            name='estado',
            field=models.CharField(choices=[('1', 'Pendiente'), ('2', 'En Proceso'), ('3', 'Finalizada'), ('4', 'Cancelada')], default='1', max_length=1),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmacion', models.BooleanField(default=False)),
                ('conferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_registro.conferencia')),
                ('particpante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_registro.participantes')),
            ],
        ),
    ]
