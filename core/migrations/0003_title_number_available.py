# Generated by Django 4.0.6 on 2022-08-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_title_options_role_name_alter_role_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="title",
            name="number_available",
            field=models.IntegerField(
                default=0, verbose_name="Number of available book"
            ),
        ),
    ]