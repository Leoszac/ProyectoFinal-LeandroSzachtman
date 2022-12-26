# Generated by Django 4.1.4 on 2022-12-14 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('sub_titulo', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=3000)),
                ('publicado_el', models.DateField()),
            ],
        ),
    ]
