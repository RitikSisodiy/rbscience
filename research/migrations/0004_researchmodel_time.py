# Generated by Django 3.2.8 on 2021-10-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_researchmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchmodel',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
