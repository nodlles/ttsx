#! /usr/bin/env python
# -*- coding: utf-8 -*-


class UrlPathMiddleware:
    # 请求处理前 会在每个请求上调用下面函数，返回none或者HttpResponse对象
    def process_request(self, request):
        """使用Django预留的底层插件，介入请求和响应的处理过程"""
        if request.path not in [
            '/register/',
            '/login/',
            '/log_handle/',
            '/reg_handle/',
            '/logout/',
        ]:
            request.session['url_path'] = request.get_full_path()  # 使用session记录每次请求的URL地址
