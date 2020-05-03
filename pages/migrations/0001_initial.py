# Generated by Django 3.0.5 on 2020-05-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, verbose_name='текст')),
                ('slug', models.SlugField(unique=True, verbose_name='чпу')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, verbose_name='текст')),
                ('slug', models.SlugField(unique=True, verbose_name='чпу')),
                ('category', models.ManyToManyField(to='pages.Category')),
                ('menu', models.ManyToManyField(to='pages.Menu')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страници',
            },
        ),
    ]
