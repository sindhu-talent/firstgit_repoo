# Generated by Django 4.0.2 on 2022-02-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother', models.CharField(max_length=20)),
                ('father', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]
