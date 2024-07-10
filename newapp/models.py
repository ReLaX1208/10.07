from django.db import models


class MyNewModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    KINDS = (
        (None, 'Выберите тип'),
        ('b', 'er'),
        ('s', 'ter'),
        ('c', 'ber'),
    )
    tip = models.CharField(max_length=1, choices=KINDS, default='s')
