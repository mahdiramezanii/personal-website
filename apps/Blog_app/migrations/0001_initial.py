# Generated by Django 4.1.6 on 2023-02-04 18:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther', models.CharField(default='مهدی رمضانی', max_length=50)),
                ('titel', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/mag/image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor.fields.RichTextField()),
                ('tag', models.ManyToManyField(related_name='Article', to='Blog_app.tag')),
            ],
        ),
    ]