from django.db import models

#クラス名：テーブル名、配下は列名
class Article(models.Model):
    title = models.CharField(default="",max_length=30)
    text = models.TextField(default="",)    

    author = models.CharField(default="",max_length=30)    
    created_at = models.DateField(auto_now_add=True) 
    updateed_at = models.DateField(auto_now=True) 
