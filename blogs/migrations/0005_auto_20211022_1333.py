# Generated by Django 3.2.8 on 2021-10-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20211022_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='heading1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='heading1details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
