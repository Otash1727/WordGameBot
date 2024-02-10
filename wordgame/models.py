from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import Now


class MatchList(models.Model):
    channel_name=models.CharField(max_length=200)
    channel_ID=models.IntegerField()  
    match_ID=models.AutoField(primary_key=True)
    players_count=models.IntegerField(null=True,blank=True)
    word_count=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    DisplyFields=['match_ID','channel_name','channel_ID']
    SearchFilds=['channel_ID','channel_name','match_ID','players_count','word_count']
    FiltersFields=['channel_name']

class GamersList(models.Model):
    match_ID=models.IntegerField(null=True,blank=True)
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=200)
    found_word_count=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,db_index=True)
    Match_List=models.ForeignKey(to=MatchList,on_delete=models.CASCADE,null=True,blank=True)  
    DisplayFields=['match_ID','user_name']
    SearchFields=['match_ID','user_id','user_name','found_word_count']
    FiltersFields=['found_word_count']

class ChempionsList(models.Model):
    match_ID=models.IntegerField(null=True,blank=True)
    channel_name=models.CharField(max_length=200)
    channel_ID=models.IntegerField()
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=100)
    results=models.IntegerField()
    MatchList=models.ForeignKey(to=MatchList,on_delete=models.CASCADE,null=True,blank=True)  
    DisplayFields=['match_ID','user_name']
    SearchFields=['match_ID','channel_ID','channel_name','user_id','user_name','results']
    FiltersFields=['channel_name']
    








