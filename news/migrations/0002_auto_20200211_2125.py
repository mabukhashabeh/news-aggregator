# Generated by Django 3.0.3 on 2020-02-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
