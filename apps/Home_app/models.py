from django.db import models

class Information(models.Model):
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media/user/image")
    addres=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    instagram=models.CharField(max_length=150)
    telegram=models.CharField(max_length=150)
    resumeh=models.FileField(upload_to="media/resume")

class Eduction(models.Model):
    university_name=models.CharField(max_length=100)
    position = models.CharField(max_length=50, default="کارشناسی کامپیوتر")
    data=models.CharField(max_length=50)
    text=models.TextField()

    def __str__(self):

        return self.university_name

class Working(models.Model):
    job_name=models.CharField(max_length=100)
    position=models.CharField(max_length=50,default="توسعه دهنده بک اند")
    data=models.CharField(max_length=50)
    text=models.TextField()

    def __str__(self):

        return self.job_name


class Maharat(models.Model):
    name=models.CharField(max_length=100)
    level=models.IntegerField(default=0)


    def __str__(self):

        return self.name


class Coutact_us(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    text=models.TextField()

    def __str__(self):

        return self.name

class work_samples(models.Model):
    image=models.ImageField(upload_to="media/work/image/")
    project_name=models.CharField(max_length=100)
    project_type=models.CharField(max_length=100)
    price=models.CharField(max_length=50)
    technology=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    url=models.CharField(max_length=200)


    def __str__(self):

        return self.project_name