# Generated by Django 4.1.7 on 2023-03-02 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0008_alter_item_seller'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
