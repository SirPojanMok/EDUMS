# Generated by Django 4.1.7 on 2023-02-28 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='noimage.jpg', upload_to='images'),
        ),
    ]
