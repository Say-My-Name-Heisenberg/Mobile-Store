# Generated by Django 4.1.7 on 2023-03-22 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("Mobile_pic", models.ImageField(null=True, upload_to="product_image")),
                ("Name", models.CharField(max_length=100)),
                ("Prize", models.IntegerField()),
                ("RAM", models.IntegerField(null=True)),
                ("ROM", models.IntegerField(null=True)),
                ("Battery", models.IntegerField(null=True)),
                ("Processer", models.CharField(max_length=100, null=True)),
                ("Camera", models.CharField(max_length=100, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="m_store",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
