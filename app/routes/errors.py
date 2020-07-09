from app.utils.validator.exceptions import InvalidRequest


def init_app(app):
    @app.errorhandler(404)
    def error(e):
        return '您请求的页面不存在了，请确认后再次访问！\n错误信息:%s' % e

    @app.errorhandler(401)
    def server_error(error):
        return '暂未登录 %s' % error.name

    @app.errorhandler(500)
    def server_error(error):
        return '我们正在升级 %s' % error.name

    @app.errorhandler(InvalidRequest) # 参数校验失败
    def invalid_request_error(error):
        return '参数校验失败 %s' % error