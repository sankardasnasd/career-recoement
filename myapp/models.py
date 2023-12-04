from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)



class Category(models.Model):
    category_name = models.CharField(max_length=100)



class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    logo=models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    pin = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    image=models.CharField(max_length=300)
    dob=models.CharField(max_length=20)
    place=models.CharField(max_length=300)
    pin=models.CharField(max_length=300)
    post=models.CharField(max_length=300)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)



class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    complaint=models.CharField(max_length=300)
    status = models.CharField(max_length=100, default='pending')
    reply = models.CharField(max_length=100, default='pending')

class Skill(models.Model):
    skill=models.CharField(max_length=100)



class Review(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    review=models.CharField(max_length=300)
    rating = models.CharField(max_length=100, default='pending')



class Jobs(models.Model):
    jobname = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    totalvacancy=models.CharField(max_length=100)
    interview_date=models.DateField()
    COMPANY=models.ForeignKey(Company,on_delete=models.CASCADE)
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)

class Jobs_Skill(models.Model):
    JOB = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    SKILL = models.ForeignKey(Skill, on_delete=models.CASCADE)




class Jobs_rating(models.Model):
    JOB = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    Rating = models.CharField(max_length=100)
    Review = models.CharField(max_length=300)

class Application(models.Model):
    JOB = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100)



class MySkill(models.Model):
    SKILL = models.ForeignKey(Skill, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)



class Experinece(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    joined_date = models.CharField(max_length=100)


class Qualification(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    yearofpass = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

class Refference(models.Model):
    narration = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)



