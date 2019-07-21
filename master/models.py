from django.db import models

# Create your models here.
from django.utils import timezone

class User(models.Model): # Userモデル
    class Meta:
        db_table = 'users' # usersテーブル
        verbose_name = 'ユーザー名'
        verbose_name_plural = 'ユーザーリスト'
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='ユーザー名', max_length=30, unique = True) # nameカラム

    def __str__(self): # adminサイトで作られるオブジェクトに可読性を持たせる
        return self.name

class Division(models.Model): # 区分モデル
    class Meta:
        db_table = 'divisions' # usersテーブル
        verbose_name = '区分'
        verbose_name_plural = '区分リスト'
    id = models.AutoField(primary_key=True)
    kubun = models.CharField(verbose_name='区分名', max_length=30, unique = True) # nameカラム

    def __str__(self): # adminサイトで作られるオブジェクトに可読性を持たせる
        return self.kubun

class Content(models.Model): # 内容モデル
    class Meta:
        db_table = 'contents' # usersテーブル
        verbose_name = '内容'
        verbose_name_plural = '内容リスト'
    id = models.AutoField(primary_key=True)
    naiyo = models.CharField(verbose_name='内容名', max_length=30, unique = True) # nameカラム

    def __str__(self): # adminサイトで作られるオブジェクトに可読性を持たせる
        return self.naiyo
