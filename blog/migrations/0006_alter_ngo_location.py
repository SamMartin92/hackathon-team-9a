# Generated by Django 3.2.18 on 2023-02-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_ngo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='location',
            field=models.CharField(max_length=60),
        ),
    ]
