# Generated by Django 4.2.6 on 2023-10-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogapp',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
