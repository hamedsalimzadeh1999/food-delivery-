from django.views.generic import View , TemplateView , ListView
from .models import Food
class MainPage(ListView):
    model= Food
    template_name = "index.html"
    context_object_name = "food"