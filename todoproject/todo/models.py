from django.db import models

# Create your models here.
# database er table create kora hoise task name a, er moddhe column hocche title,desciption,completed ,created date

class Task(models.Model):
    title = models.CharField(max_length=200)
    desciption = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
