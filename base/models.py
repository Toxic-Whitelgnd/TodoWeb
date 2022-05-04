
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Todolist(models.Model):
#     name = models.CharField(max_length=200)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todolist",null=True)

#     def __str__(self):
#         return self.name

# class tasks(models.Model):
#     text = models.CharField(max_length=300, blank=True)
#     todolist = models.ForeignKey(Todolist,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text
class Task(models.Model):
    user = models.ForeignKey(User,
    on_delete=models.CASCADE,null=True,blank = True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
