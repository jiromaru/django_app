from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length = 100)
    gender= models.BooleanField()
    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '>'

class index(models.Model):
    name = models.CharField(max_length = 100)
    
class M1301(models.Model):
    date = models.CharField(primary_key=True,max_length = 100)
    open = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    dekidaka = models.IntegerField(blank=True, null=True)
    close_adjust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_1301'


class M1332(models.Model):
    date = models.CharField(primary_key=True,max_length = 100)
    open = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    dekidaka = models.IntegerField(blank=True, null=True)
    close_adjust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_1332'


class M1333(models.Model):
    date = models.CharField(primary_key=True,max_length = 100)
    open = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    dekidaka = models.IntegerField(blank=True, null=True)
    close_adjust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_1333'


class M1352(models.Model):
    date = models.CharField(primary_key=True,max_length = 100)
    open = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    dekidaka = models.IntegerField(blank=True, null=True)
    close_adjust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_1352'


class M1376(models.Model):
    date = models.CharField(primary_key=True,max_length = 100)
    open = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    dekidaka = models.IntegerField(blank=True, null=True)
    close_adjust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_1376'


class M1377(models.Model):
    date = models.CharField(primary_key=True,max_length = 100)
    open = models.IntegerField(blank=True, null=True)
    top = models.IntegerField(blank=True, null=True)
    low = models.IntegerField(blank=True, null=True)
    close = models.IntegerField(blank=True, null=True)
    dekidaka = models.IntegerField(blank=True, null=True)
    close_adjust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_1377'
