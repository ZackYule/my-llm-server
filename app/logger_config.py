import logging


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format=
        '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        # )
        filename='myapp.log',  # 日志文件名)
        filemode='w')  # 'w' 为覆盖模式，'a' 为追加模式


setup_logging()
