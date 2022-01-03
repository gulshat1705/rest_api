from django.db import models

class AbstractComment(models.Model):
    """ Abstract model of comments"""
    text = models.TextField(max_length=500)
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        abstract = True    