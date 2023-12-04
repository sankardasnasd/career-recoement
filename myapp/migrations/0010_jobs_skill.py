# Generated by Django 4.2.5 on 2023-10-25 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobs')),
                ('SKILL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.skill')),
            ],
        ),
    ]
