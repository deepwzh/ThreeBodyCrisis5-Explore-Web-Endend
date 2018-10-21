import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import ExpRank, HpRank, LdeRank, LvRank, Article, User
import json
# Create your views here.

def exp_rank_view(request):
    res = ExpRank.objects.all()
    u = list()
    index = 1
    for r in res:
        u.append({
            'rank': index,
            'name': r.user_id,
            'value': r.exp
        })
        index += 1
    json_str = json.dumps(u)
    return HttpResponse(json_str)

def hp_rank_view(request):
    res = HpRank.objects.all()
    u = list()
    index = 1
    for r in res:
        u.append({
            'rank': index,
            'name': r.user_id,
            'value': r.hp
        })
        index += 1
    json_str = json.dumps(u)
    return HttpResponse(json_str)

def lde_rank_view(request):
    res = LdeRank.objects.all()
    u = list()
    index = 1
    for r in res:
        if not r.lde:
            continue
        u.append({
            'rank': index,
            'name': r.user_id,
            'value': float(r.lde)
        })
        index += 1
    json_str = json.dumps(u)
    return HttpResponse(json_str)

def lv_rank_view(request):
    res = LvRank.objects.all()
    u = list()
    index = 1
    for r in res:
        u.append({
            'rank': index,
            'name': r.user_id,
            'value': r.lv
        })
        index += 1
    json_str = json.dumps(u)
    return HttpResponse(json_str)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


def article_view(request):
    res = Article.objects.all()
    u = list()
    index = 1
    for r in res:
        u.append({
            'id': r.id,
            'title': r.title,
            'content': r.content,
            'publish_time': r.publish_time,
            'user_id': r.user_id
        })
        index += 1
    json_str = json.dumps(u, cls=DateEncoder)
    return HttpResponse(json_str)

def register_view(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        user_id = data['user_id']
        username = data['username']
        password = data['password']
        try:
            user = User.objects.create(user_id = user_id, username=username, password=password)
            return HttpResponse("Register Success.")
        except Exception as e:
            return HttpResponse("Register Fail.", status=403)
    else:
        return HttpResponse("Only Post Method is allowed.")