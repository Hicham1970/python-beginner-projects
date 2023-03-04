# Generated by Django 3.2.7 on 2022-05-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Item_name", models.CharField(max_length=100)),
                ("Image", models.ImageField(default="", upload_to="menu/images")),
                ("Category", models.CharField(max_length=50)),
                ("Price", models.FloatField()),
                ("Discount", models.FloatField()),
                ("Plate_size", models.IntegerField()),
            ],
        ),
    ]
