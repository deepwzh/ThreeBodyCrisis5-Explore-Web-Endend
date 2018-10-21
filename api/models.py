# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archives(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    lv = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    snapshot = models.TextField(blank=True, null=True)  # This field type is a guess.
    save_time = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField(blank=True, null=True)
    config = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'archives'

class ExpRank(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'user_best_exp'


class LvRank(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    lv = models.IntegerField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'user_best_lv'


class LdeRank(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    lde = models.FloatField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'user_best_lde'

class HpRank(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'user_best_hp'



class User(models.Model):
    user_id = models.CharField(unique=True, max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Article(models.Model):
    title = models.CharField(max_length=45)
    user = models.ForeignKey('User', models.DO_NOTHING)
    publish_time = models.DateTimeField()
    content = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'
