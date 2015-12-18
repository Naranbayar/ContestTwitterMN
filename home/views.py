# -*- coding: utf-8 -*-
import json
import random
from datetime import datetime

from django.conf import settings
from django.shortcuts import render

import feedparser
from twitter import Twitter, OAuth

from django import http

def home(request):
    # Tweets
    twitter = Twitter(auth=OAuth(settings.TOKEN,
                                 settings.TOKEN_KEY,
                                 settings.SECRET,
                                 settings.SECRET_KEY))

    tweets = twitter.statuses.user_timeline(screen_name='NaranbayarU', count=5)

    utcnow = datetime.utcnow()
    datetime_format = '%Y-%m-%d %H:%M:%S UTC'
    hackerrank_url = 'http://www.hackerrank.com/calendar/feed.rss'

    # Contests
    active_contests, upcoming_contests = [], []
    feeds = feedparser.parse(hackerrank_url)
    for feed in reversed(feeds['entries']):
        start_time = datetime.strptime(feed['starttime'], datetime_format)
        end_time = datetime.strptime(feed['endtime'], datetime_format)

        # Active contests
        if start_time <= utcnow <= end_time:
            active_contests.append({
                'url': feed['url'],
                'title': feed['title'],
                'start_time': feed['starttime'],
                'end_time': feed['endtime'],
            })

        # Upcoming contests
        if start_time > utcnow:
            upcoming_contests.append({
                'url': feed['url'],
                'title': feed['title'],
                'start_time': feed['starttime'],
                'end_time': feed['endtime'],
            })

    return render(request, 'index.html', {
        'current_time': utcnow.strftime('%Y-%m-%d %H:%M:%S UTC'),
        'active_contests': active_contests,
        'upcoming_contests': upcoming_contests,
        'tweets': tweets,
    })

def tweetEvening(request):
    animals = []
    animals.append("Манж гэдэг нь нас гүйцсэн хандгайн эр нь юм.")
    animals.append("Сүндэс гэдэг нь Хандгайн эм нь юм.")
    animals.append("Тохь гэдэг нь Шүдлэн хандгай юм.")
    animals.append("Тозуул гэдэг нь Хязаалан хандгай юм.")
    animals.append("Дайр гэдэг нь Бугын эр юм.")
    animals.append("Марал гэдэг нь Бугын эм нь согоо ч гэдэг юм.")
    animals.append("Цөх гэдэг нь Бугын гурван настай нь юм.")
    animals.append("Шармаахай гэдэг нь Нас гүйцсэн баавгайн эр нь юм.")
    animals.append("Өтөр гэдэг нь Баавгайн өөр нэр юм.")
    animals.append("Эвш гэдэг нь Баавгайн эм нь юм.")
    animals.append("Цагаан хүзүүт гэдэг нь Идэр баавгай юм.")
    animals.append("Эрслэн гэдэг нь Арслангийн эм юм.")
    animals.append("Гирээ гэдэг нь Хүдрийн эр нь юм.")
    animals.append("Гирэгчин гэдэг нь Хүдрийн эм нь юм.")
    animals.append("Гангис гэдэг нь Доргоны эр нь юм.")
    animals.append("Мангис гэдэг нь Доргоны эм нь юм.")
    animals.append("Мий гэдэг нь Муурын эр нь юм.")
    animals.append("Мигуй гэдэг нь Муурын эм нь юм.")
    animals.append("Монди гэдэг нь Сармагчны эр нь юм.")
    animals.append("Монш гэдэг нь Сармагчны эм нь юм.")
    animals.append("Эрхис гэдэг нь Булгын эр нь юм.")
    animals.append("Эвшхис гэдэг нь Булгын эм нь юм.")
    animals.append("Эвь эвий гэдэг нь Халиуны эм нь юм.")
    animals.append("Хаван гэдэг нь Их азарган гахай юм.")
    animals.append("Зарь гэдэг нь Цааны эр нь гэдэг нь агталсан юм.")
    animals.append("Мянжиг гэдэг нь Цааны эм нь гэдэг нь үнээ юм.")
    animals.append("Этэр гэдэг нь Цааны бух юм.")
    animals.append("Засбан гэдэг нь Цааны бяруу юм.")
    animals.append("Атуух гэдэг нь Загасны эр нь юм.")
    animals.append("Атуу гэдэг нь Загасны эм нь юм.")
    animals.append("Бойр гэдэг нь Халиуны эр нь юм.")
    animals.append("Арьяад гэдэг нь Бөхөнгийн эм нь юм.")
    animals.append("Шавж гэдэг нь Давжаа хурга юм.")
    animals.append("Азаргана гэдэг нь Зөгийн эр нь юм.")
    animals.append("Хатанз гэдэг нь Зөгийн эм нь юм.")
    animals.append("Нагай гэдэг нь тарч гэдэг нь Хөхүүл тарвага юм.")
    animals.append("Хотоль гэдэг нь 2 настай тарвага болзлог юм.")
    animals.append("Асмаг гэдэг нь Агтлуулсан гахай юм.")
    animals.append("Тарчин гэдэг нь Минжний эм нь Минжүүхэй юм.")
    animals.append("Соёохой гэдэг нь Хоёр настай ооно зээр юм.")
    animals.append("Соёндой гэдэг нь Бугын 2 настай нь юм.")
    # Tweets
    twitter = Twitter(auth=OAuth(settings.TOKEN,
                                 settings.TOKEN_KEY,
                                 settings.SECRET,
                                 settings.SECRET_KEY))

    ss = "Бүгд Монголчууд минь сайхан амраарай. " + random.choice(animals)
    twitter.statuses.update(status=ss)
    return http.HttpResponse("")

def tweetMorning(request):
    animals = []
    animals.append("Дүдэр гэдэг нь Минжний зулзага юм.")
    animals.append("Балнам гэдэг нь Ортоомын тугал юм.")
    animals.append("Цуравдай гэдэг нь Гургуулын зулзага юм.")
    animals.append("Зогой гэдэг нь Могойн зулзага юм.")
    animals.append("Үрвэл гэдэг нь Гүрвэлийн зулзага юм.")
    animals.append("Бонго гэдэг нь Алмасны үр юм.")
    animals.append("Янгуудай явгуудай гэдэг нь Бор гөрөөсний янзага юм.")
    animals.append("Ногуул гэдэг нь Шилүүсний зулзага юм.")
    animals.append("Гүег гэдэг нь Арслангийн зулзага юм.")
    animals.append("Гүен гэдэг нь Ирвэсний зулзага юм.")
    animals.append("Ганис гэдэг нь Доргоны зулзага юм.")
    animals.append("Алманцаг гэдэг нь Мазаалайн төл юм.")
    animals.append("Зоргол, Ший гэдэг нь Бугын тугал юм.")
    animals.append("Онох гэдэг нь Янгирын зулзага юм.")
    animals.append("Зөнжиг гэдэг нь Хярсны зулзага юм.")
    animals.append("Турганы гэдэг нь дудран гэдэг нь Солонгын зулзага юм.")
    animals.append("Дудран гэдэг нь Илжигний унага юм.")
    animals.append("Бөөдий гэдэг нь Зарааны зулзага юм.")
    animals.append("Ногоолой гэдэг нь Мануулын зулзага юм.")
    animals.append("Борж гэдэг нь Жирхний зулзага юм.")
    animals.append("Цурваг гэдэг нь Тахианы дэгдээхэй юм.")
    animals.append("Бөртөн гэдэг нь Зээхийн зулзага юм.")
    animals.append("Шовшоорой гэдэг нь Хүдрийн зулзага юм.")
    animals.append("Хоршдой гэдэг нь Хэрэмний зулзага юм.")
    animals.append("Хугаш гэдэг нь Цааны тугал юм.")
    animals.append("Цагцгай гэдэг нь Бүргэдийн зулзага юм.")
    animals.append("Сөдгий гэдэг нь Өмхий хүрний зулзага юм.")
    animals.append("Бамбар гэдэг нь Барын зулзага юм.")
    animals.append("Гавар гэдэг нь Үнэгний зулзага юм.")
    animals.append("Бүсрэг гэдэг нь Суусрын зулзага юм.")
    animals.append("Ялман гэдэг нь Алаг дааганы зулзага юм.")
    animals.append("Хойв гэдэг нь Булганы зулзага юм.")
    animals.append("Бор гэдэг нь Халиуны зулзага юм.")
    animals.append("Төрц гэдэг нь Загасны үр юм.")

    # Tweets
    twitter = Twitter(auth=OAuth(settings.TOKEN,
                                 settings.TOKEN_KEY,
                                 settings.SECRET,
                                 settings.SECRET_KEY))

    ss = "Гэгээн тунгалагхан өглөөний мэнд. " + random.choice(animals)
    twitter.statuses.update(status=ss)
    return http.HttpResponse("")

def page(request):

    return render(request, 'page.html', {
        'data': '',
    })
