# Generated by Django 3.1.6 on 2021-02-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('message', models.CharField(max_length=255)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploaded_images')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
    ]
