# Generated by Django 3.0.5 on 2020-04-22 09:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
