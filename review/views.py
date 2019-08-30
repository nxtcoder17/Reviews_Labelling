from django.shortcuts import render
from django.http import HttpResponse
from review.models import Review
import sqlite3
from django.views.decorators.csrf import csrf_exempt
import json

# Path to YELP Reviews

length = len (Review.objects.all())

# Create your views here.
def index (request):
    return render (request, 'review/index.html');

count = 1
@csrf_exempt
def submit (request):
    sentiment = request.POST.get ('sentiment');
    id = request.POST.get ('id')
    r = Review.objects.get (pk = id);
    r.sentiment = sentiment
    r.save()
    flag = True

    global count
    if count > 2:
        count = 0
        review = Review.objects.filter (sentiment = 200).first()
        flag = False if review is not None else True
    if flag:
        review = Review.objects.filter(sentiment = 100).first()
    count += 1;

    # review = Review.objects.filter (sentiment=100).first()
    return HttpResponse(json.dumps({'text': review.review_text, 'id': review.id, 'sent': review.sentiment}), content_type='application/json');

@csrf_exempt
def thankyou (request):
    return render (request, 'review/thankyou.html');

count = 0;
@csrf_exempt
def start (request):
    review = Review.objects.filter (sentiment=100).first()
    if review is None:
        return render (request, 'review/start.html', {'review': "Thank You, But survey is complete now."})
    return render (request, 'review/start.html', {'review': review})
    # return render (request, 'review/start.html')
