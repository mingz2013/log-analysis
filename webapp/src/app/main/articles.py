# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import render_template, redirect, url_for, request, make_response, current_app

from app import db
from . import main
from ..models import Article, Comment
from app.dbredis import RedisClient

import json, re, os
from uploader import Uploader


@main.route('/', methods=['GET'])
@main.route('/<int:page>', methods=['GET'])
def index(page=1):
    pagination = Article.query.order_by(Article.create_at.desc()).paginate(page, per_page=10, error_out=False)
    articles = pagination.items
    print articles
    return render_template('articles/index.html', articles=articles, pagination=pagination)


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = Article.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(article_id=id)
    return render_template('articles/detail.html', article=article, comments=comments)


@main.route('/article/post', methods=['GET', 'POST'])
def post():
    id = request.args.get('id', '')
    if request.method == "GET":
        if id:
            article = Article.query.filter_by(id=id).first()
            return render_template('articles/edit.html', article=article)
        else:
            return render_template('articles/new.html')
    else:
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        if id:
            article = Article.query.filter_by(id=id).first()
            article.title = title
            article.content = content
            db.session.commit()
        else:
            id = RedisClient.get_article_id()
            article = Article(title=title, content=content, id=id)
            db.session.add(article)
            db.session.commit()

        return redirect(url_for('main.article', id=id))


@main.route('/article/comment/<int:article_id>', methods=['POST'])
def comment(article_id):
    name = request.form.get('name', '')
    comment = request.form.get('comment', '')
    id = RedisClient.get_comment_id()
    c = Comment(id=id, name=name, comment=comment, article_id=article_id)
    db.session.add(c)
    db.session.commit()
    return redirect(url_for('main.article', id=article_id))


@main.route('/upload/', methods=['GET', 'POST', 'OPTIONS'])
def upload():
    """UEditor文件上传接口
    config 配置文件
    result 返回结果
    """
    mimetype = 'application/json'
    result = {}
    action = request.args.get('action')
    # 解析JSON格式的配置文件
    with open(os.path.join(current_app.static_folder, 'ueditor', 'php',
                           'config.json')) as fp:
        try:
            # 删除 `/**/` 之间的注释
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        except:
            CONFIG = {}
    if action == 'config':
        # 初始化时，返回配置文件给客户端
        result = CONFIG
    elif action in ('uploadimage', 'uploadfile', 'uploadvideo'):
        # 图片、文件、视频上传
        if action == 'uploadimage':
            fieldName = CONFIG.get('imageFieldName')
            config = {
                "pathFormat": CONFIG['imagePathFormat'],
                "maxSize": CONFIG['imageMaxSize'],
                "allowFiles": CONFIG['imageAllowFiles']
            }
        elif action == 'uploadvideo':
            fieldName = CONFIG.get('videoFieldName')
            config = {
                "pathFormat": CONFIG['videoPathFormat'],
                "maxSize": CONFIG['videoMaxSize'],
                "allowFiles": CONFIG['videoAllowFiles']
            }
        else:
            fieldName = CONFIG.get('fileFieldName')
            config = {
                "pathFormat": CONFIG['filePathFormat'],
                "maxSize": CONFIG['fileMaxSize'],
                "allowFiles": CONFIG['fileAllowFiles']
            }
        if fieldName in request.files:
            field = request.files[fieldName]
            uploader = Uploader(field, config, current_app.static_folder)
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口出错'
    elif action in ('uploadscrawl'):
        # 涂鸦上传
        fieldName = CONFIG.get('scrawlFieldName')
        config = {
            "pathFormat": CONFIG.get('scrawlPathFormat'),
            "maxSize": CONFIG.get('scrawlMaxSize'),
            "allowFiles": CONFIG.get('scrawlAllowFiles'),
            "oriName": "scrawl.png"
        }
        if fieldName in request.form:
            field = request.form[fieldName]
            uploader = Uploader(field, config, current_app.static_folder, 'base64')
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口出错'
    elif action in ('catchimage'):
        config = {
            "pathFormat": CONFIG['catcherPathFormat'],
            "maxSize": CONFIG['catcherMaxSize'],
            "allowFiles": CONFIG['catcherAllowFiles'],
            "oriName": "remote.png"
        }
        fieldName = CONFIG['catcherFieldName']
        if fieldName in request.form:
            # 这里比较奇怪，远程抓图提交的表单名称不是这个
            source = []
        elif '%s[]' % fieldName in request.form:
            # 而是这个
            source = request.form.getlist('%s[]' % fieldName)
        _list = []
        for imgurl in source:
            uploader = Uploader(imgurl, config, current_app.static_folder, 'remote')
            info = uploader.getFileInfo()
            _list.append({
                'state': info['state'],
                'url': info['url'],
                'original': info['original'],
                'source': imgurl,
            })
        result['state'] = 'SUCCESS' if len(_list) > 0 else 'ERROR'
        result['list'] = _list
    else:
        result['state'] = '请求地址出错'
    result = json.dumps(result)
    if 'callback' in request.args:
        callback = request.args.get('callback')
        if re.match(r'^[\w_]+$', callback):
            result = '%s(%s)' % (callback, result)
            mimetype = 'application/javascript'
        else:
            result = json.dumps({'state': 'callback参数不合法'})
    res = make_response(result)
    res.mimetype = mimetype
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
    return res
