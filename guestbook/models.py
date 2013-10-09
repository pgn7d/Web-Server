from django.db import models
import datetime

# Create your models here.
class GueatBookNew(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    Date_Sign_In=models.DateTimeField(editable=False)

    def save(self,*args,**kwargs):
        if not self.id:
            self.Date_Sign_In = datetime.datetime.today()
        return super(GueatBookNew,self).save(*args,**kwargs)
    
    def __unicode__(self):
        return self.First_Name+" "+self.Last_Name
