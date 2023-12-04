# Generated by Django 4.2.5 on 2023-10-25 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_jobs_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('JOB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobs')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
