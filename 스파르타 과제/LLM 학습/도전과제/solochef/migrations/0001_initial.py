# Generated by Django 4.2 on 2025-01-24 12:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Conversation",
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
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("user_input", models.TextField(verbose_name="사용자 입력")),
                ("ai_response", models.TextField(verbose_name="AI 응답")),
            ],
            options={
                "verbose_name": "대화",
                "verbose_name_plural": "대화 기록",
                "ordering": ["-timestamp"],
            },
        ),
    ]
