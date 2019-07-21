# Generated by Django 2.2.3 on 2019-07-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naiyo', models.CharField(max_length=30, verbose_name='内容名')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容リスト',
                'db_table': 'contents',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kubun', models.CharField(max_length=30, verbose_name='区分名')),
            ],
            options={
                'verbose_name': '区分',
                'verbose_name_plural': '区分リスト',
                'db_table': 'divisions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ユーザー名')),
            ],
            options={
                'verbose_name': 'ユーザー名',
                'verbose_name_plural': 'ユーザーリスト',
                'db_table': 'users',
            },
        ),
    ]
