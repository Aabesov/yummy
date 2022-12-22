# Generated by Django 4.1.4 on 2022-12-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=250)),
                ('pictures', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
            ],
        ),
    ]