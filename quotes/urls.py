from django.urls import path

from quotes.views import QuoteListView

urlpatterns = [
    path("", QuoteListView.as_view(), name="quote_list")
]

app_name = "quotes"
