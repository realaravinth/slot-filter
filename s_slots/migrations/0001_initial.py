# Generated by Django 2.2.7 on 2019-11-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=None, max_length=20)),
                ('Monday', models.BooleanField()),
                ('Monday_time', models.TimeField()),
                ('Tuesday', models.BooleanField()),
                ('Tuesday_time', models.TimeField()),
                ('Wednesday', models.BooleanField()),
                ('Wednesday_time', models.TimeField()),
                ('Thursday', models.BooleanField()),
                ('Thursday_time', models.TimeField()),
                ('Friday', models.BooleanField()),
                ('Friday_time', models.TimeField()),
                ('Saturday', models.BooleanField()),
                ('Saturday_time', models.TimeField()),
            ],
        ),
    ]
