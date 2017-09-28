from django.db import models
from django.utils import timezone

# Model
class Post(models.Model):
    # Link to another model
    author = models.ForeignKey('auth.User')
    # Text with a limited number of characters
    title = models.CharField(max_length=200)
    # Long text without a limit
    text = models.TextField()
    # Date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
