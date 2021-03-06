# Generated by Django 2.2.3 on 2019-07-19 07:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shikakebi', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='仕掛け開始日')),
                ('kiboubi', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='希望納期')),
                ('hinban', models.CharField(max_length=140, verbose_name='品番')),
                ('kataban', models.CharField(max_length=140, verbose_name='型番')),
                ('mitsumorikosu', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=3, null=True, verbose_name='見積工数(Ｈ)')),
                ('minaoshikosu', models.IntegerField(blank=True, default=0, null=True, verbose_name='見直し工数(直)')),
                ('kubun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Division', verbose_name='区分')),
                ('naiyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Content', verbose_name='内容')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.User', verbose_name='受付担当')),
            ],
            options={
                'verbose_name': '登録データ',
                'verbose_name_plural': '受付登録',
                'db_table': 'Regists',
            },
        ),
    ]
