# Generated by Django 4.0.2 on 2024-04-15 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('cinema_hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.cinemahall')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.movie')),
            ],
        ),
    ]