from django.contrib import admin
from web.models import Subscribe, Customer, Feature, VideoBlog, Testimonial, MarketingFeature, Product, Blog, Contact


admin.site.register(Subscribe)

admin.site.register(Customer)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'testimonial_author', 'author_designation']

admin.site.register(Feature, FeatureAdmin)

admin.site.register(VideoBlog)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'description', 'designation', 'company_name']

admin.site.register(Testimonial, TestimonialAdmin)

class MarketingFeatureAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'description']

admin.site.register(MarketingFeature, MarketingFeatureAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'title', 'description']

admin.site.register(Product, ProductAdmin)

admin.site.register(Blog)

admin.site.register(Contact)