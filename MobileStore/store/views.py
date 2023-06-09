from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView
from .models import Products
from .forms import *
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


#==== Decorator ====#
def signin_required(fn):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect ("Homepage")
    return wrapper


# Create your views here.

# Home Page
@method_decorator(signin_required,name='dispatch')
class DealerHome(TemplateView):
    template_name="dealerpage.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.all()
        return context
    
# Add product

class AddProduct(CreateView):
    form_class=ProductForm
    model=Products
    template_name='addproduct.html'
    success_url=reverse_lazy('Dealer')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        return super().form_valid(form)

#View Profile

class Profile(TemplateView):
    template_name="profile.html"

#View My PRoducts

class MyProduct(TemplateView):
    template_name="myproduct.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.filter(user=self.request.user)
        return context
    
class UpdateProduct(UpdateView):
    form_class=ProductForm
    model=Products
    template_name='addproduct.html'
    success_url=reverse_lazy('MyPro')


class RemoveProduct(DeleteView):
    model=Products
    template_name='delproduct.html'
    success_url=reverse_lazy('MyPro')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Products.objects.filter(user=self.request.user)
        return context