from django.shortcuts import render_to_response
from django.views.generic import View
from django.http.response import HttpResponse
from django.template import RequestContext
# Create your views here.


class MyViews(View):
    def get(self, request):
        context_token = RequestContext(request)
        return render_to_response('gen_template.html', context_token)

    def post(self,request):
        return HttpResponse('<html>working</html>')

