from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings

class PostJobManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostJobManager, self).filter(draft = False).filter(publish__lte = timezone.now())

def upload_location(job_database, filename):
    return "%s/%s/%s" %(job_database.app_name, job_database.id, filename)

class job_database(models.Model):
    app_name = "Job"
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=300)
    detail = models.TextField(max_length=2300)

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field"
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

    contact_number = models.IntegerField()
    contact_email = models.EmailField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    objects = PostJobManager()


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = job_database.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_jd_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_jd_receiver, sender=job_database)