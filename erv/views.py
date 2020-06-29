from django.http import HttpResponse
from django.shortcuts import render
import erv.models as models
import erv.forms as forms
import erv.clsfr.art_mapping_proposal as art_map

def home(request):
    return render(request, "erv/home.html")

def login(request):
    return render(request, "erv/login.html")

def about(request):
    return render(request, "erv/about.html")

def contact(request):
    return render(request, "erv/contact.html")

def cust_index(request):

    cust = models.get_customers()

    return render(
        request,
        'erv/cust_index.html',
        {
            'customers': cust
        }
    )


def cust_view(request, id):

    cust = models.get_customer(int(id))
    sales = models.get_sales(int(id))

    return render(
        request,
        'erv/cust_view.html',
        {
            'customer': cust
            ,'sales': sales
        }
    )


def requ_index(request):

    requests = models.get_requests()

    return render(
        request,
        'erv/requ_index.html',
        {
            'requests': requests
        }
    )

def art_class(request):
    
    art_map_prop = ""
    rnd_articles = models.get_article_rnd(5)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.ArticleMappingForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            art_map_prop = art_map.get_article_mapping_proposal(form.cleaned_data['article'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.ArticleMappingForm()

    return render(
        request,
        'erv/art_class.html',
        {
            'art_map_prop': art_map_prop,
            'form': form,
            'rnd_articles': rnd_articles
        }
    )