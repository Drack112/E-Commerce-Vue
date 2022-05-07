# Generated by Django 4.0.4 on 2022-05-07 18:19

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=cloudinary_storage.storage.MediaCloudinaryStorage(),
                upload_to="uploads/",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=cloudinary_storage.storage.MediaCloudinaryStorage(),
                upload_to="uploads/",
            ),
        ),
    ]
