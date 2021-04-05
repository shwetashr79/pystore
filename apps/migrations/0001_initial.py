# Generated by Django 3.1.7 on 2021-04-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=100)),
                ('version', models.FloatField()),
                ('developer', models.CharField(max_length=100)),
                ('app_py', models.FileField(upload_to=models.CharField(max_length=100))),
                ('app_exe', models.FileField(upload_to=models.CharField(max_length=100))),
                ('icon', models.ImageField(upload_to=models.CharField(max_length=100))),
            ],
        ),
    ]