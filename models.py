from django.db import models


class State(models.Model):
    id=models.IntegerField(default=50,primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    city_id=models.IntegerField(default=50,primary_key=True)
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    city_name=models.ForeignKey(City,on_delete=models.CASCADE)
    emailid=models.EmailField()
    password=models.CharField(max_length=50)
    date=models.DateField()

    def __str__(self):
        return self.emailid

class Jobs(models.Model):
    job_id=models.IntegerField(default=50,primary_key=True)
    job_name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    company_city=models.ForeignKey(City,on_delete=models.CASCADE)
    skills=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=10,decimal_places=2)

    def  __str__(self):
        return '{}@{}-{}'.format(self.job_name,self.company_name,self.company_city)

class UserProfile(models.Model):
    my_name=models.CharField(max_length=50)
    contact_no=models.IntegerField(default=10)
    my_email=models.EmailField()
    myskills=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)
    experiance=models.DecimalField(max_digits=2,decimal_places=1)
    compnany=models.CharField(max_length=50)

    def __str__(self):
        return self.name

