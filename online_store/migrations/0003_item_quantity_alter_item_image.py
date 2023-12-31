# Generated by Django 4.2.5 on 2023-09-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_store", "0002_item_description_item_image_alter_item_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="uploads/"
            ),
        ),
    ]
