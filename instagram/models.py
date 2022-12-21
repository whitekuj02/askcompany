from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class port(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/port/%Y%m%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #java의 toString
    def __str__(self):
        # return f"Costom port object({self.id})"
        return self.message

    class Meta:
        ordering = ['-id']
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"

class Comment(models.Model):
    port_key = models.ForeignKey(port, on_delete=models.CASCADE,
                                 limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
