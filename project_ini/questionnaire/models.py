from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType


from comments.models import Comment


class PostQuestionManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostQuestionManager, self).filter(draft=False).filter(publish__lte = timezone.now())

class questions_info(models.Model):
    question = models.CharField(max_length=500)
    detail = models.TextField(max_length=2000, blank=True, null=True, default=None)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    slug = models.SlugField(unique=True)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False,auto_now_add=False, default=timezone.now())

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostQuestionManager()

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("qna:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.question)
    if new_slug is not None:
        slug = new_slug
    qs = questions_info.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_jd_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_jd_receiver, sender=questions_info)