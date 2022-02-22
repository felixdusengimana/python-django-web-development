from django.shortcuts import render


# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')


def variable_view(request):
    dicty = {
        "fist_name": "Felix",
        "last_name": "Wazekwa",
        "some_list": [1, 2, 3],
        "some_dict": {"inside_key": "inside_value"},
        "logged_in": True
    }
    return render(request=request, template_name="my_app/variable.html", context=dicty)
