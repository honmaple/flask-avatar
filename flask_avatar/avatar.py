#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: avatar.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-07-02 16:12:53 (CST)
# Last Update: Saturday 2018-03-03 21:31:59 (CST)
#          By:
# Description:
# **************************************************************************
import os
from random import randint, seed
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from flask import make_response, abort, current_app


class Avatar(object):
    def __init__(self, app=None, cache=None):
        '''
        cache must be a decorator
        example:

        def cache(func):
            @wrap(func)
            def _cache(*args, **kwargs):
                r = cacheclient.get("cache key")
                if r is not None:
                    return r
                return func(*args, **kwargs)
            return _cache
        '''
        self.app = app
        self.cache = cache
        if app is not None:
            self.init_app(self.app)

    def init_app(self, app):
        avatar_url = app.config.get('AVATAR_URL', '/avatar')
        view = self.avatar
        if self.cache is not None:
            view = self.cache(view)
        app.add_url_rule(
            avatar_url + '/<text>', 'avatar', view, defaults={
                'width': 128
            })
        app.add_url_rule(avatar_url + '/<text>/<int:width>', 'avatar', view)

    def avatar(self, text, width):
        width_range = current_app.config.get('AVATAR_RANGE', [0, 512])
        if width < width_range[0] or width > width_range[1]:
            abort(404)
        stream = GenAvatar.generate(width, text)
        buf_value = stream.getvalue()
        response = make_response(buf_value)
        response.headers['Content-Type'] = 'image/jpeg'
        return response


class GenAvatar(object):
    FONT_COLOR = (255, 255, 255)
    MAX_RENDER_SIZE = 512

    @classmethod
    def generate(cls, size, string, filetype="JPEG"):
        """
            Generates a squared avatar with random background color.
            :param size: size of the avatar, in pixels
            :param string: string to be used to print text and seed the random
            :param filetype: the file format of the image (i.e. JPEG, PNG)
        """
        render_size = max(size, GenAvatar.MAX_RENDER_SIZE)
        image = Image.new('RGB', (render_size, render_size),
                          cls._background_color(string))
        draw = ImageDraw.Draw(image)
        font = cls._font(render_size)
        text = cls._text(string)
        draw.text(
            cls._text_position(render_size, text, font),
            text,
            fill=cls.FONT_COLOR,
            font=font)
        stream = BytesIO()
        image = image.resize((size, size), Image.ANTIALIAS)
        image.save(stream, format=filetype, optimize=True)
        # return stream.getvalue()
        return stream

    @staticmethod
    def _background_color(s):
        """
            Generate a random background color.
            Brighter colors are dropped, because the text is white.
            :param s: Seed used by the random generator
            (same seed will produce the same color).
        """
        seed(s)
        r = v = b = 255
        while r + v + b > 255 * 2:
            r = randint(0, 255)
            v = randint(0, 255)
            b = randint(0, 255)
        return (r, v, b)

    @staticmethod
    def _font(size):
        """
            Returns a PIL ImageFont instance.
            :param size: size of the avatar, in pixels
        """
        # path = '/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc'
        path = os.path.join(
            os.path.dirname(__file__), 'data', "wqy-microhei.ttc")
        return ImageFont.truetype(path, size=int(0.65 * size), index=0)

    @staticmethod
    def _text(string):
        """
            Returns the text to draw.
        """
        if len(string) == 0:
            return "H"
        else:
            return string[0].upper()

    @staticmethod
    def _text_position(size, text, font):
        """
            Returns the left-top point where the text should be positioned.
        """
        width, height = font.getsize(text)
        left = (size - width) / 2.0
        top = (size - height) / 3.0
        return left, top
