from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
# from django.contrib.auth import get_user_model
#
# User = get_user_model()

class PostMatManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostMatManager, self).filter(Draft=False).filter(publish__lte = timezone.now())

    # def users(self, *args, **kwargs):
    #     return super(PostMatManager, self).filter(user= User)



def upload_location(mat_info, filename):
    return "%s/%s/%s" % (mat_info.app_name,mat_info.id, filename)

class mat_info(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    AGE_ONE = 'one'
    AGE_TWO = 'two'
    AGE_THREE = 'three'
    AGE_FOUR = 'four'
    AGE_FIVE = 'five'
    AGE_LIST = (
        (AGE_ONE, '18-23'),
        (AGE_TWO, '24-29'),
        (AGE_THREE, '30-35'),
        (AGE_FOUR, '36-41'),
        (AGE_FIVE, '41+')
    )
    app_name = "Matrimonial"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=140, default='Marriage proposal!!')
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    Draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

    description = models.TextField(help_text='Please enter the details of yourself, and the detail you would like the other party to know. You have a limit of 2300 characters')
    email_address = models.CharField(max_length=100, help_text='Enter a Valid email address for contact Purpose')
    phone_contact = models.CharField(max_length=20)
    your_gender = models.CharField(max_length=6, choices=GENDER, default=FEMALE)
    # your_gender = models.CharField(max_length=6)
    your_age = models.IntegerField(default=23)
    your_qualification = models.CharField(max_length=200)

    search_age = models.CharField(max_length=5, choices=AGE_LIST, default=AGE_ONE)
    # search_age = models.CharField(max_length=5)
    search_qualification = models.CharField(max_length=200)
    search_settled = models.CharField(max_length=200)

    detail_privacy = models.BooleanField(help_text='Your Information will be hidden')
    terms_and_conditions = models.BooleanField(help_text='Do you Agree with the terms and conditions', default=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostMatManager()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("matrimonial:detail", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = mat_info.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_jd_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_jd_receiver, sender=mat_info)