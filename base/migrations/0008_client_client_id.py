# Generated by Django 4.1.3 on 2023-10-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_client_assignee"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="client_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
