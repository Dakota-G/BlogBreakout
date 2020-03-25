from django.db import models

class User(models.Model):
    Username = models.CharField(max_length = 35)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    Title = models.CharField(max_length=25)
    Text = models.TextField(max_length=150)
    Creator = models.ForeignKey(User, related_name="Blog_Entry", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
