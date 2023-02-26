from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения new_app")

def caption(request):
    return HttpResponse("еще одна страница из new_app")

def blog(request):
    return HttpResponse("тут будет что-то про блог")
