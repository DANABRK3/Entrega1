# Generated by Django 4.1.3 on 2022-12-31 00:28

import datetime
from django.db import migrations, models


# Generated by Django 4.1.3 on 2022-12-31 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_vendedores_alter_curso_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2022, 12, 30, 21, 28, 48, 610287)),
        ),
    ]
