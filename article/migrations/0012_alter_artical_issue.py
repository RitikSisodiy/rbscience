# Generated by Django 3.2 on 2021-10-24 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20211024_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yearbyissue', to='article.issue'),
        ),
    ]
