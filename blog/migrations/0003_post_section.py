# Generated by Django 3.0.5 on 2020-04-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200224_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.IntegerField(choices=[(0, 'News'), (1, 'Tips'), (2, 'DIY Projects')], default=0),
        ),
    ]