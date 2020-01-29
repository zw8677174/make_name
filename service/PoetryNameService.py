from model.db import *
from random import *
from service.SystemService import SystemService


class PoetryNameService:

    @classmethod
    def get(cls):
        while 1:
            poetry = Poetry.select().where(Poetry.id == randint(1, 31182)).first()
            sentences = str(poetry.content).split('|')
            sentence_base = choice(sentences)
            sentence = sentence_base.replace(',', '').replace('。', '').replace('，', '')
            sentence = cls.check_sentence(sentence)
            if len(sentence) > 3:
                break
        return dict(
            name=cls.make_name(sentence),
            sentence=sentence_base,
            content=poetry.content.replace('|', '\n</br>')
        )

    @classmethod
    def make_name(cls, sentence):
        len1 = len(sentence)
        target = []
        for i in range(3):
            target.append(randint(0, len1 - 1))
        target = sorted(target)
        return sentence[target[0]] + sentence[target[1]] +sentence[target[2]]

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
