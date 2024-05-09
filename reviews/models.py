from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'A avaliação minínma é de 0 estrelas!'),
            MaxValueValidator(5, 'A avaliação máxima é de 5 estrelas!')
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie
