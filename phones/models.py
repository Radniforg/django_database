from django.db import models


class Phone(models.Model):
    objects = models.Manager()
    id = models.TextField(primary_key=True)
    name = models.TextField()
    price = models.TextField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exist = models.TextField()
    slug = models.TextField()

    def __str(self):
        return self.name
    # TODO: Добавьте требуемые поля
