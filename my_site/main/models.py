from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Slide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='slides/')
    background_color = models.CharField(max_length=50, default='blue')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Counter(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

class CompanyInfo(models.Model):
    about_text = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed_code = models.TextField(blank=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)


# class HomeSection(models.Model):
#     SECTION_CHOICES = [
#         ('section2', 'بخش دوم (عکس + متن)'),
#         ('section4', 'بخش چهارم (مشابه بخش دوم)'),
#         ('section6', 'بخش ششم (مشابه بخش دوم)'),
#     ]
#
#     section_type = models.CharField(max_length=20, choices=SECTION_CHOICES)
#     title = models.CharField(max_length=200, verbose_name="تیتر")
#     content = RichTextField(verbose_name="محتوا")
#     image = models.ImageField(upload_to='home_sections/', verbose_name="تصویر")
#     button_text = models.CharField(max_length=50, default="اطلاعات بیشتر", verbose_name="متن دکمه")
#     button_link = models.CharField(max_length=200, blank=True, verbose_name="لینک دکمه")
#     is_active = models.BooleanField(default=True, verbose_name="فعال")
#     order = models.PositiveIntegerField(default=0, verbose_name="ترتیب نمایش")
#
#     class Meta:
#         verbose_name = "بخش صفحه اصلی"
#         verbose_name_plural = "بخش‌های صفحه اصلی"
#         ordering = ['order']
#
#     def __str__(self):
#         return f"{self.get_section_type_display()} - {self.title}"


class HomeSection(models.Model):
    SECTION_TYPES = (
        ('section2', 'بخش دوم'),
        ('section4', 'بخش چهارم'),
        ('section6', 'بخش ششم'),
    )

    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    title = models.CharField(max_length=200, verbose_name="تیتر")
    description = models.TextField(verbose_name="توضیحات")  # متن ساده
    image = models.ImageField(upload_to='home_sections/', verbose_name="تصویر")
    button_text = models.CharField(max_length=50, default="اطلاعات بیشتر")
    button_url = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Logo(models.Model):
    image = models.ImageField(upload_to='site_logo/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "لوگوی سایت"