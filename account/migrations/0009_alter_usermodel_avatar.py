# Generated by Django 4.2.4 on 2023-09-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0008_alter_usermodel_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="avatar",
            field=models.ImageField(default=1, upload_to="files/covers"),
            preserve_default=False,
        ),
    ]
