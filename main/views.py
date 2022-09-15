from django.shortcuts import render

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


def error_page(request, message):
    response = render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response