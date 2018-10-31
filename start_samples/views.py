from django.http import HttpResponse

from logging import getLogger
from django.template.loader import get_template
from django.shortcuts import render

logger = getLogger(__name__)


def index(request):
    logger.debug("デバッグ")
    logger.info("インフォ")
    logger.warning("ワーニング")
    logger.error("エラー")
    logger.critical("クリティカル")

    return HttpResponse("日本一平凡なDjango")


def render_index(request):
    return render(request, 'start_samples/index.html')


def hensu_render_index(request):
    # テンプレートに挿入する変数をセットアップ
    context = {
        "name": "ウズマスター",
        "age": "35",
    }

    return render(request, 'start_samples/hensu.html', context)


def hensu_render_index2(request):
    # テンプレートに挿入する変数をセットアップ
    person = {
        "name": "ウズマスター",
        "age": "35",
    }

    context = {"person": person}

    return render(request, 'start_samples/hensu2.html', context)


from django.template.loader import render_to_string


def string_render_index(request):
    # テンプレートに挿入する変数をセットアップ
    context = {
        "name": "ウズマスター",
        "age": "35",
    }

    # レンダリング
    text = render_to_string('start_samples/message.txt', context)

    # こんにちは。ウズマスターです。年齢は35歳です。
    logger.info(text)

    return HttpResponse(text)
