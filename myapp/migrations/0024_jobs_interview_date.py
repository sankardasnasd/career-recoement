# Generated by Django 4.2.5 on 2023-11-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_refference_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='interview_date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
