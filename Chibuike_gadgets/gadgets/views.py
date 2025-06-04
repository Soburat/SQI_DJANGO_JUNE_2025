from django.shortcuts import render, HttpResponse

# Create your views here.
def items(request):
    return HttpResponse('<ol> <li>Television</li>'
    '<li>GOTV</li>'
    '<li>Home Theatre</li>'
    '<li>DSTV</li>'
    '</ol>',)