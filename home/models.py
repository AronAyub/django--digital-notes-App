from django.db import models

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=100)  # Change 'name' to 'full_name'
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, default='')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name  # Update the return statement to use 'full_name'
