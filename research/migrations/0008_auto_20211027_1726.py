# Generated by Django 3.2.8 on 2021-10-27 11:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0007_alter_researchmodel_projectdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchmodel',
            name='processOverview',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='researchmodel',
            name='projectDetails',
            field=ckeditor.fields.RichTextField(default='<p><strong>RESEARCH NAME</strong> : enter here..</p><p><strong>CLIENT </strong>: enter here..</p><p><strong>CATEGORY :</strong>enter here..</p><p><strong>DELIVERY MODE :</strong>enter here..</p><p><strong>LOCATION :</strong>enter here..</p>'),
        ),
    ]
