# Generated by Django 3.1.7 on 2021-05-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20210523_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmodel',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appmodel',
            name='description',
            field=models.TextField(default='No description by publisher', null=True),
        ),
        migrations.AddField(
            model_name='appmodel',
            name='requirement',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appmodel',
            name='screenshots',
            field=models.ImageField(null=True, upload_to='main/screenshots'),
        ),
        migrations.AddField(
            model_name='appmodel',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
