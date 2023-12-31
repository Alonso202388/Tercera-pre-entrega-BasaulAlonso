# Generated by Django 4.2.4 on 2023-08-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAlonso', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaDeEntrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profesion', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
