from django.shortcuts import render
from logging import getLogger

logger = getLogger(__name__)


# Create your views here.
def autoescape(request):
    context = {"param": "<script>alert('日本一平凡なクロスサイトスクリプティング');</script>"}

    return render(request, 'tag_samples/autoescape.html', context)


def extends_block(request):
    context = {"param": "日本一平凡"}

    return render(request, 'tag_samples/child.html', context)


def tagfor(request):
    context = {}
    list = []
    list.append({"name": "一郎", "age": 30})
    list.append({"name": "次郎", "age": 32})
    list.append({"name": "三郎", "age": 31})

    context["person_list"] = list

    parent_list = []
    parent_list.append(list)
    parent_list.append(list)
    parent_list.append(list)

    context["parent_list"] = parent_list

    cities = [
        {'name': 'ムンバイ', 'population': '19,000,000', 'country': 'インド'},
        {'name': 'カルカッタ', 'population': '15,000,000', 'country': 'インド'},
        {'name': 'ニューヨーク', 'population': '20,000,000', 'country': 'アメリカ'},
        {'name': 'シカゴ', 'population': '7,000,000', 'country': 'アメリカ'},
        {'name': '東京', 'population': '33,000,000', 'country': '日本'},
    ]
    context["cities"] = cities

    return render(request, 'tag_samples/tagfor.html', context)


def tagif(request):
    context = {}
    list = []
    list.append({"department": "技術課", "name": "Ａさん"})
    list.append({"department": "技術課", "name": "Ｂさん"})
    list.append({"department": "営業課", "name": "Ｃさん"})
    list.append({"department": "営業課", "name": "Ｄさん"})
    list.append({"department": "営業課", "name": "Ｅさん"})
    list.append({"department": "総務課", "name": "Ｆさん"})
    list.append({"department": "総務課", "name": "Ｇさん"})

    context["person_list"] = list

    return render(request, 'tag_samples/tagif.html', context)


def taginclude(request):
    context = {}

    context["name"] = "ウズマスター"
    context["age"] = 35
    context["hoby"] = "ブログ執筆"

    return render(request, 'tag_samples/tagincludebody.html', context)
