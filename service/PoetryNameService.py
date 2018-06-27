from model.db import *
from random import choice
from service.SystemService import SystemService


class PoetryNameService:

    @classmethod
    def get(cls):
        while 1:
            poetry = Poetry.select().order_by(fn.Rand()).first()
            sentences = str(poetry.content).split('|')
            sentence_base = choice(sentences)
            sentence = sentence_base.replace(',', '').replace('。', '').replace('，', '')
            sentence = cls.check_sentence(sentence)
            if len(sentence) > 3:
                break
        return dict(
            name=cls.make_name(sentence),
            sentence=sentence_base,
            content=poetry.content
        )

    @classmethod
    def make_name(cls, sentence):
        name1 = choice(sentence)
        name2 = choice(sentence)
        return name1 + name2

    @classmethod
    def check_sentence(cls, sentence):
        ret = []
        for word in sentence:
            if word not in cls.default_useless_word():
                ret.append(word)
        return ret

    @classmethod
    def default_useless_word(cls):
        return SystemService.get_useless_word()
