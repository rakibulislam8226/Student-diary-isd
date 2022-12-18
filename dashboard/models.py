from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
# Create your models here.


############## notes start###########
class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    description=models.TextField(max_length=1200)

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"
    def __str__(self):
        return self.title

############## Notes start###########


############## Homework start###########
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1200)
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    @property
    def short_title(self):
        return truncatechars(self.title, 20)

############## Homework End###########


############## todo start###########
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title
############## todo end###########






