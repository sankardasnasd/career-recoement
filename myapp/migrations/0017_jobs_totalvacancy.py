# Generated by Django 4.2.5 on 2023-10-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_experinece'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='totalvacancy',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]