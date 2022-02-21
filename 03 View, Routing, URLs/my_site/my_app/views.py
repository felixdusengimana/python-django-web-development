from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# articles = {
#     "sports": "Sport page",
#     "finance": "finance page",
#     "politics": "politics page",
# }
#
#
# def news_view(request, topic):
#     try:
#         return HttpResponse(articles[topic])
#     except:
#         raise Http404("Page not found.")
#
#
# def add_view(request, num1, num2):
#     result = f"{num1} + {num2} =  {num1 + num2}"
#     return HttpResponse(str(result))
#
#
# def num_page_view(request, num_page):  # Redirecting
#     topics_list = list(articles.keys())
#     try:
#         topic_name = topics_list[num_page]
#         webpage = reverse("topic_page", args=[topic_name])  # Reverse URL
#         return HttpResponseRedirect(webpage)
#     except:
#         raise Http404("Not founddd")

def simple_view(request):
    return render(request, 'my_app/example.html')  # .html
