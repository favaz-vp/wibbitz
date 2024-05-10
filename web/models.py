from django.db import models


CONTENT_TYPE = (
    ("blog_post", "Blog Post"),
    ("webinar", "Webinar"),
    ("report", "Report")
)

COMPANY_SIZE = (
    ("1", "1-10"),
    ("2", "11-50"),
    ("3", "51-200"),
    ("4", "201-500")
)

INDUSTRY = (
    ("1", "Agriculture"),
    ("2", "Banking & Finance"),
    ("1", "Business Services & Software")
)

JOB_ROLE = (
    ("1", "C-Suite"),
    ("2", "VP")
)

COUNTRY = (
    ("us", "United States"),
    ("albania", "Albania")
)
class Subscribe(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email


class Customer(models.Model):
    product = models.ForeignKey("web.Product", on_delete=models.CASCADE)
    logo = models.FileField(upload_to = "customers/")
    white_logo = models.FileField(upload_to="customers/", blank=True, null=True)

    class Meta:
        ordering = ["id"]


class Feature(models.Model):
    image = models.ImageField(upload_to = "features/")
    icon = models.FileField(upload_to = "features/")
    icon_background = models.CharField(max_length = 128 )
    title = models.CharField(max_length = 128)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length = 128)
    author_designation = models.CharField(max_length = 128)
    testimonial_logo = models.FileField()

    def __str__(self):
        return self.title


class VideoBlog(models.Model):
    image = models.ImageField(upload_to = "VideoBlog/image/")
    title = models.CharField(max_length = 128)
    logo = models.FileField(upload_to = "VideoBlog/logo/")

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/image")
    logo = models.FileField(upload_to="testimonial/logo", null = True, blank = True)
    description = models.CharField(max_length=252)
    name = models.CharField(max_length=128) 
    designation = models.CharField(max_length=128) 
    company_name = models.CharField(max_length=128) 
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MarketingFeature(models.Model):
    image = models.FileField(upload_to="marketing/")
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to="product/image/")
    hero_image = models.ImageField(upload_to="product/image/")
    name = models.CharField(max_length=148)
    title = models.CharField(max_length=148)
    description = models.TextField()
    background_color = models.CharField(max_length=148)
    logo = models.FileField(upload_to="product/logo/")

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=128)
    content_type = models.CharField(max_length=128, choices=CONTENT_TYPE)

    def __str__(self):
        return self.content_type


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size = models.CharField(max_length=128, choices=COMPANY_SIZE)
    industry = models.CharField(max_length=128, choices=INDUSTRY)
    job_role = models.CharField(max_length=128, choices=JOB_ROLE)
    country = models.CharField(max_length=128, choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.email