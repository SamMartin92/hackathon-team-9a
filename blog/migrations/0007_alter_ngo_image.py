# Generated by Django 3.2.18 on 2023-02-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_ngo_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='image',
            field=models.ImageField(default='media/ngo_images/default.jpg', upload_to='ngo_images/'),
        ),
    ]
