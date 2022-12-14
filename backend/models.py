from django.db import models

class Colour(models.Model) :
    name = models.CharField(max_length=30)

    def __str__(self) -> str :
        return self.nomi
class Car(models.Model) :
    name = models.CharField(max_length=20)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)

    def __str__(self) -> str :
        return self.nomi







