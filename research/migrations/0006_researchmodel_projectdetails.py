# Generated by Django 3.2.8 on 2021-10-27 11:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_auto_20211027_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchmodel',
            name='projectDetails',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]