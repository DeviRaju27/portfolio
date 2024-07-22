from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    tech = models.TextField()
    image = models.ImageField(default = 'default.png', upload_to = 'uploads/')
    url = models.TextField(default = 'default.png')

    def __str__(self):
        return f'{self.name}'