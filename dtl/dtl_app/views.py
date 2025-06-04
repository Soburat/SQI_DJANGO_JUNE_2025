from django.shortcuts import render

# Create your views here.
def practice_dtl(request):
    context = {
        'username': 'Soburat',
        'no_of_messages': 5,
        'messages':['Hello', 'feel free to chat?', 'when can we talk?'],
        'is_logged_in': 'True',

    }

    return render (request, "dtl/practice-dtl.html", context)
