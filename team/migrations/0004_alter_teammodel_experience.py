# Generated by Django 3.2.8 on 2021-11-11 07:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20211026_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammodel',
            name='experience',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
