# Generated by Django 5.1.6 on 2025-02-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_customuser_credits_customuser_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_request_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
