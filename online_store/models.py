from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    age = models.FloatField(default=70)
    status = models.CharField(max_length=250, default='Normal')

    description= models.CharField(max_length=250, default='The ' + str(name), blank=True, null= True)
    image= models.ImageField(upload_to='uploads/', default='', blank=True, null= True)

    @staticmethod
    def get_item_by_id(id):
        return Item.objects.filter (id__in=id)
    
    @staticmethod
    def get_all_items():
        return Item.objects.all()

    def __str__(self):
        return self.name

