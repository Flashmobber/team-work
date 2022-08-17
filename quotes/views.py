from django.views import generic
from models import Quote


class QuoteListView(generic.ListView):
    model = Quote
    queryset = Quote.objects.all()
    context_object_name = "quote_list"
    template_name = "quotes/quote_list.html"
