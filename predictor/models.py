from django.db import models

class SkinImage(models.Model):
    image = models.ImageField(upload_to='skin_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SkinImage {self.id}"
