# Generated by Django 2.2.2 on 2019-06-23 16:57

import django.utils.timezone
from django.db import migrations, models


def add_created_on_data(apps, schema_editor):
    Issue = apps.get_model("comicsdb", "Issue")
    query = Issue.objects.all()
    for i in query:
        i.created_on = i.modified
        i.save()


def remove_created_on_data(apps, schema_editor):
    Issue = apps.get_model("comicsdb", "Issue")
    Issue.objects.update(created_on=django.utils.timezone.now)


class Migration(migrations.Migration):

    dependencies = [("comicsdb", "0002_creator_alias")]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.RunPython(add_created_on_data, reverse_code=remove_created_on_data),
        migrations.AlterField(
            model_name="issue",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
