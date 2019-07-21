from django.db import models

# Create your models here.
from django.utils import timezone
from master.models import *

class Regist(models.Model): # 登録
    class Meta:
        db_table = 'Regists' # tweetsテーブル
        verbose_name = '登録データ'
        verbose_name_plural = '受付登録'
    id = models.AutoField(primary_key=True)
    shikakebi = models.DateField( verbose_name='仕掛け開始日', blank=True, null=True, default=timezone.now)
    kiboubi = models.DateField( verbose_name='希望納期', blank=True, null=True, default=timezone.now)
    hinban = models.CharField(verbose_name='品番', max_length=140) # textカラム
    kataban = models.CharField(verbose_name='型番', max_length=140) # textカラム
    kubun = models.ForeignKey(Division, verbose_name='区分', on_delete=models.CASCADE) # Userモデルとリレーション
    naiyo = models.ForeignKey(Content, verbose_name='内容', on_delete=models.CASCADE) # Userモデルとリレーション
    mitsumorikosu = models.DecimalField(verbose_name='見積工数(Ｈ)',max_digits=3,decimal_places=1,blank=True,null=True,default=0.0)
    minaoshikosu = models.IntegerField(verbose_name='見直し工数(直)',blank=True,null=True,default=0)
    user = models.ForeignKey(User, verbose_name='受付担当', on_delete=models.CASCADE) # Userモデルとリレーション
    def __str__(self): # adminサイトで作られるオブジェクトに可読性を持たせる
        return self.hinban



'''
shikakebi 仕掛け開始日
kiboubi 希望納期
hinban 品番
katashiki 型番
kubun 区分
naiyo 内容
mitsumorikosu 見積工数(H)
minaoshikosu 見直し工数(直)
user 受付担当
'''
