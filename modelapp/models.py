from django.db import models
class product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=10)
    pcost=models.DecimalField(max_digits=10,decimal_places=2)
    pmfdt=models.DateField()
    pexpdt=models.DateField()
    def __str__(self):
        return self.pname
# Create your models here.
