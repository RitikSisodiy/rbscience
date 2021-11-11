# Generated by Django 3.2.8 on 2021-11-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(upload_to='sliders')),
                ('title', models.CharField(max_length=50)),
                ('keys', models.CharField(default='-,-,-', max_length=200)),
                ('learnMoreurl', models.CharField(max_length=500)),
            ],
        ),
    ]
