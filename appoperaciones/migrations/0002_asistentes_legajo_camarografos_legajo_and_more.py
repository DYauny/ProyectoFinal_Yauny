# Generated by Django 5.0.6 on 2024-08-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoperaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistentes',
            name='legajo',
            field=models.IntegerField(default=1234),
        ),
        migrations.AddField(
            model_name='camarografos',
            name='legajo',
            field=models.IntegerField(default=1234),
        ),
        migrations.AddField(
            model_name='microfonistas',
            name='legajo',
            field=models.IntegerField(default=1234),
        ),
        migrations.AlterField(
            model_name='asistentes',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='asistentes',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='camarografos',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='camarografos',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='microfonistas',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='microfonistas',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
