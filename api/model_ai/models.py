from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "user"

    fullName = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName


class UserEmbedding(models.Model):
    user = models.ForeignKey(User, related_name="embeddings", on_delete=models.CASCADE)
    embdding = models.JSONField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Embedding for {self.user.fullName} at {self.createdAt}"
