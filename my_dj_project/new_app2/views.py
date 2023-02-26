from django.http import HttpResponse


def index2(request):
    return HttpResponse("Страница приложения new_app")

def caption2(request):
    return HttpResponse("еще одна страница из new_app")

def blog2(request):
    return HttpResponse("тут будет что-то про блог")
