from django.db import models
from django.contrib.auth.models import User
import uuid




def generate_uuid():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    reference_id=models.CharField(max_length=32,unique=True,primary_key=True,default=generate_uuid)
    is_delete=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,db_column='created_by',on_delete=models.PROTECT,related_name='+',null=True)
    created_at=models.DateTimeField(null=True)
    updated_by=models.ForeignKey(User,db_column='updated_by',on_delete=models.PROTECT,null=True)
    updated_at=models.DateTimeField(null=True)
    class Meta:
        abstract=True
    


class StudentDetails(BaseModel):
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=10)
    class Meta:
        db_table='student'
        
    def __str__(self):
        return self.email
  

