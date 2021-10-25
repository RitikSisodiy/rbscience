# Generated by Django 3.2.8 on 2021-10-24 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_wp_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='issue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.issue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artical',
            name='vol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.vol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artical',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.year'),
            preserve_default=False,
        ),
    ]
