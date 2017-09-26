from django.db import models
from django.db.models import Q
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self, query):
        if query :
            query = query.strip()
            return self.filter(
                Q(location__icontains=query)|
                Q(category__icontains=query)|
                Q(item__name__icontains=query)|
                Q(item__contents__icontains=query)
    
            ).distinct()
        return self


class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RestaurantLocation(models.Model) :
    owner           = models.ForeignKey(User)  # django models unleashed joincfe
    name            = models.CharField(max_length = 120)
    location        = models.CharField(max_length = 120, null = True, blank = True)
    category        = models.CharField(max_length = 120, null = True, blank = True, validators=[validate_category])
    timestamp       = models.DateTimeField(auto_now_add = True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(unique=True, null=True, blank=True)

    objects = RestaurantLocationManager() # add Model.objects.all()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    def get_absolute_url_update(self):
        return reverse('restaurants:edit', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

def restaurantLocationPreSaveReceiver(sender, instance, *args, **kwargs) :
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def restaurantLocationPostSaveReceiver(sender, instance, created, *args, **kwargs) :
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()


pre_save.connect(restaurantLocationPreSaveReceiver, sender=RestaurantLocation)

# post_save.connect(restaurantLocationPostSaveReceiver, sender=RestaurantLocation)
