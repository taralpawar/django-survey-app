# Generated by Django 2.2.5 on 2020-07-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodquality', models.CharField(max_length=50)),
                ('servicequality', models.CharField(max_length=50)),
                ('speed', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
