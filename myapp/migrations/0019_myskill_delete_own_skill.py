# Generated by Django 4.2.5 on 2023-11-01 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKILL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.skill')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Own_skill',
        ),
    ]
