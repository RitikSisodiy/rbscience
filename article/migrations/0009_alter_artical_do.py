# Generated by Django 3.2.8 on 2021-10-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20211024_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='do',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
