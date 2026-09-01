from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete 
from django.dispatch import receiver
from datetime import datetime
import os

# Create your models here.

def get_cover_path(obj, fn):
    path = datetime.now().strftime(f"covers/%Y/%m/%d/{fn}")
    return path

def get_image_path(obj, fn):
    path = datetime.now().strftime(f"images/%Y/%m/%d/{fn}")
    return path


class BaseModel(models.Model):
    user_modified = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="%(class)s_user_modified",
        null=True,
        blank=True,
        verbose_name="Created User"
        )
    user_created = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="%(class)s_user_created",
        null=True,
        blank=True,
        verbose_name="Modified User"
        )
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)

    class Meta:
        abstract = True


class FashionCategoryModel(BaseModel):
    title = models.CharField(verbose_name="Title", max_length=200, unique=True)
    cover = models.ImageField(verbose_name="Cover Photo", upload_to=get_cover_path, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.title}"
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Fashion Category"
        verbose_name_plural = "Fashion Categories"


class TextileCategoryModel(BaseModel):
    title = models.CharField(verbose_name="Title", max_length=200, unique=True)
    cover = models.ImageField(verbose_name="Cover Photo", upload_to=get_cover_path, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.title}"
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Textile Category"
        verbose_name_plural = "Textile Categories"


class FashionModel(BaseModel):
    product_category = models.ForeignKey(FashionCategoryModel, on_delete=models.CASCADE, verbose_name="Product's Category")
    product_code = models.CharField(verbose_name="Product's code", max_length=200, unique=True, null=True, blank=True)
    product_name = models.CharField(verbose_name="Product's Name", max_length=200)
    product_cover = models.ImageField(verbose_name="Cover Image", upload_to=get_cover_path)
    product_date = models.DateField(verbose_name="Product's Date", auto_now_add=True)
    product_slogan = models.TextField(verbose_name="Product's slogan", null=True, blank=True)
    product_inspiration = models.TextField(verbose_name="Product's Inspiration", null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.product_name}"
    
    class Meta:
        ordering = ["product_name"]
        verbose_name = "Fashion Product"
        verbose_name_plural = "Fashion Products"


class TextileModel(BaseModel):
    product_category = models.ForeignKey(FashionCategoryModel, on_delete=models.CASCADE, verbose_name="Product's Category")
    product_code = models.CharField(verbose_name="Product's code", max_length=200, unique=True, null=True, blank=True)
    product_name = models.CharField(verbose_name="Product's Name", max_length=200)
    product_cover = models.ImageField(verbose_name="Cover Image", upload_to=get_cover_path)
    product_date = models.DateField(verbose_name="Product's Date", auto_now_add=True)
    product_slogan = models.TextField(verbose_name="Product's slogan", null=True, blank=True)
    product_inspiration = models.TextField(verbose_name="Product's Inspiration", null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.product_name}"
    
    class Meta:
        ordering = ["product_name"]
        verbose_name = "Textile Product"
        verbose_name_plural = "Textile Products"


class FashionImageModel(BaseModel):
    product = models.ForeignKey(FashionModel, on_delete=models.CASCADE, verbose_name="Fashion Product")
    image = models.ImageField(verbose_name="Image", upload_to=get_image_path)
    
    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = "Fashion's Product Image"
        verbose_name_plural = "Fashion's Product Images"
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path): 
            if os.path.isfile(self.image.path): 
                os.remove(self.image.path)
        super(FashionImageModel, self).delete(*args, **kwargs)


@receiver(post_delete, sender=FashionImageModel)
def auto_delete_file_fashion(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)


class TextileImageModel(BaseModel):
    product = models.ForeignKey(TextileModel, on_delete=models.CASCADE, verbose_name="Textile Product")
    image = models.ImageField(verbose_name="Image", upload_to=get_image_path)
    
    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = "Textile's Product Image"
        verbose_name_plural = "Textile's Product Images"
    
    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path): 
            if os.path.isfile(self.image.path): 
                os.remove(self.image.path)
        super(TextileImageModel, self).delete(*args, **kwargs)


@receiver(post_delete, sender=TextileImageModel)
def auto_delete_file_textile(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)


class ContactModel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=250)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Subject", max_length=250)
    message = models.TextField(verbose_name="Message")
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    
    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Message"
        verbose_name_plural = "Messages"