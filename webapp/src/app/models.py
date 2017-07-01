# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from datetime import datetime

from . import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    image = db.Column(db.String(100))
    create_at = db.Column(db.DateTime)

    def __init__(self, id=None, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content
        self.create_at = datetime.utcnow()
        self.image = ''

    def __repr__(self):
        return '<Article %r>' % self.title


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    comment = db.Column(db.Text)
    create_at = db.Column(db.DateTime)
    article_id = db.Column(db.Integer)

    def __init__(self, id=None, name=None, comment=None, article_id=None):
        self.id = id
        self.name = name
        self.comment = comment
        self.create_at = datetime.utcnow()
        self.article_id = article_id

    def __repr__(self):
        return '<Comment %r>' % self.comment
