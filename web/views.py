import json
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from web.models import Subscribe, Customer, Feature, VideoBlog, Testimonial, MarketingFeature, Product, Blog
from web.forms import ContactForm


def index(request):
    customer = Customer.objects.all()
    latest_customer = Customer.objects.all()[:4]
    feature = Feature.objects.all()
    videoblog = VideoBlog.objects.all()
    featured_testimonial = Testimonial.objects.filter(is_featured=True)
    non_featured_testimonial = Testimonial.objects.filter(is_featured=False)
    marketing = MarketingFeature.objects.all()
    product = Product.objects.all()
    blog = Blog.objects.all()

    form = ContactForm()

    context = {
        "customers" : customer,
        "latest_customers" : latest_customer,
        "features" : feature,
        "videoblogs" : videoblog,
        "featured_testimonials" : featured_testimonial,
        "non_featured_testimonials" : non_featured_testimonial,
        "marketings" : marketing,
        "products" : product,
        "blogs" : blog,
        "form" : form

    }
    return render(request, "index.html", context = context)
    
def subscribe(request):
    email = request.POST.get("email")
    if not Subscribe.objects.filter(email = email).exists():
        Subscribe.objects.create(
            email = email
        )
        response_data = {
            "status" : "success",
            "title" : "subscription was successfull",
            "message" : "Email registration was succesfull"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "subscription has failed",
            "message" : "Email registration was NOT succesfull"
        }
    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()

        response_data = {
        "status" : "success",
        "title" : "subscription was successfull",
        "message" : "Email registration was succesfull"
    }
    else:
        response_data = {
            "status" : "error",
            "title" : "subscription has failed",
            "message" : "Email registration was NOT succesfull"
        }
    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")
    

def product(request,pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    customers = Customer.objects.filter(product=product)
    context = {
        "product":product,
        "customers":customers
    }
    return render(request,"product.html",context=context)