import logging
from .formatter import JsonFormatter
from .filter import RequestIdFilter

def init_logger(log_level=logging.INFO) -> logging.Logger:
  """
  logger の初期設定
  """

  # http://qiita.com/smats-rd/items/c5f4345aca3a452041c7#しかし勿論こんなことをしてはいけない
  # https://qiita.com/smats-rd/items/c5f4345aca3a452041c7#%E3%81%97%E3%81%8B%E3%81%97%E5%8B%BF%E8%AB%96%E3%81%93%E3%82%93%E3%81%AA%E3%81%93%E3%81%A8%E3%82%92%E3%81%97%E3%81%A6%E3%81%AF%E3%81%84%E3%81%91%E3%81%AA%E3%81%84

  # ロガーを設定
  logger = logging.getLogger(__name__)  

  # ハンドラがあればスキップ
  if not logger.handlers:
    logger.propagate = False                # ルートロガーへの伝搬を禁止
    logger.setLevel(log_level)              # ログレベルの設定
    handler = logging.StreamHandler()       # ハンドラの設定
    handler.setLevel(log_level)             # ハンドラのログレベルを設定
    handler.setFormatter(JsonFormatter())   # カスタムフォーマッタをハンドラに設定
    logger.addHandler(handler)              # ハンドラの追加
    logger.addFilter(RequestIdFilter())     # aws_request_id を挿入するフィルタを設定
    logger.debug('Logging is initialized')

  return logger