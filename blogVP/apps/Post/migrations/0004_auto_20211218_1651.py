# Generated by Django 3.0 on 2021-12-18 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='post/portada'),
        ),
    ]
