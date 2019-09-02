from django.shortcuts import render
from django.http import HttpResponse
from review.models import Review
from django.views.decorators.csrf import csrf_exempt 
import json
import random

# length = len (Review.objects.all())

# Create your views here.
def index (request):
    return render (request, 'review/index.html');

# count = 0

# def write_log (text):
    # with open("/tmp/app.log", "at") as file:
        # file.write (text + "\n");

try:
    second = random.sample (list(Review.objects.filter (sentiment=200)), 2);
except ValueError:
    second = list(Review.objects.filter (sentiment=200))

try:
    first = random.sample (list(Review.objects.filter (sentiment=100)), 5 + 2 - len(second));
except ValueError:
    first = list(Review.objects.filter (sentiment=100))


target_list = first + second

# target_list = random.sample (list(Review.objects.filter(sentiment=100)), 3);
random.shuffle (target_list)

iterator = iter (target_list)

@csrf_exempt
def submit (request):
    global iterator, target_list, first, second
    sentiment = request.POST.get ('sentiment');
    id = request.POST.get ('id');

    # Accessing that review
    r = Review.objects.get (pk = id);
    r.sentiment = sentiment
    r.save ()

    try:
        review = iterator.__next__()
        return HttpResponse (json.dumps ({'text': review.review_text, 'id': review.id, 'sent': review.sentiment}), content_type='application/json')
    except StopIteration:
        try:
            second = random.sample (list(Review.objects.filter (sentiment=200)), 2);
        except ValueError:
            second = list(Review.objects.filter (sentiment=200))

        try:
            first = random.sample (list(Review.objects.filter (sentiment=100)), 5 + 2 - len(second));
        except ValueError:
            first = list(Review.objects.filter (sentiment=100))

        target_list = first + second
        random.shuffle (target_list)
        iterator = iter (target_list)
        return HttpResponse (json.dumps ({'id': -1}), content_type='application/json')
    
# @csrf_exempt
# def submit (request):
    # global count
    # sentiment = request.POST.get ('sentiment');
    # id = request.POST.get ('id')
    # r = Review.objects.get (pk = id);
    # r.sentiment = sentiment
    # r.save()
    # flag = True
# 
    # if count > 2:
        # count = 0
        # review = Review.objects.filter (sentiment = 200).first()
        # flag = False if review is not None else True
        # write_log (f" TRIGGERED Count: {count}  review.id = {review.id}  review.sentiment = {review.sentiment} FLAG = {flag}")
    # if flag:
        # review = Review.objects.filter(sentiment = 100).first()
    # count += 1;
# 
    # write_log (f"NORMAL Count: {count}  review.id = {review.id}  review.sentiment = {review.sentimet}")
    # return HttpResponse(json.dumps({'text': review.review_text, 'id': review.id, 'sent': review.sentiment}), content_type='application/json');

@csrf_exempt
def thankyou (request):
    return render (request, 'review/thankyou.html');

count = 0;
@csrf_exempt
def start (request):
    global iterator
    try:
        review = iterator.__next__()
        return render (request, 'review/start.html', {'review': review})
    except StopIteration:
        return HttpResponse (json.dumps ({'id': -1}), content_type='application/json')
    # return render (request, 'review/start.html')
