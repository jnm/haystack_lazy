from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import FavoriteWord

# Create your views here.

@login_required
def favorite_word(request, word):
    fw = FavoriteWord()
    fw.user = request.user # It's a SimpleLazyObject!
    fw.word = word
    fw.save()
    return HttpResponse('So be it, {}.'.format(request.user.username))
