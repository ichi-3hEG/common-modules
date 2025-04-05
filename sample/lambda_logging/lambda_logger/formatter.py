import json
import logging
from datetime import datetime, date

class JsonFormatter(logging.Formatter):
  """ログを JSON 形式で出力するフォーマッタ"""
  # 標準のログレコード属性（extra で追加する場合はこれらの名前は避ける）
  # https://docs.python.org/3.13/library/logging.html#logrecord-attributes
  STANDARD_ATTRS = {
    'args',  'asctime', 'created', 'exc_info', 'filename', 'funcName',
    'levelname', 'levelno', 'lineno', 'message', 'module', 'msecs', 'msg',
    'name', 'pathname', 'process', 'processName', 'relativeCreated',
    'stack_info', 'thread', 'threadName', 'taskName',
  }

  def json_serial(self, obj):
    """日付型は dump できないので置換"""
    
    if isinstance(obj, (datetime, date)):
      return obj.isoformat()
    else:
      return str(obj)

  def format(self, record):
    try:
      log_record = {
        'timestamp': self.formatTime(record, self.datefmt),
        'level': record.levelname,
        'message': record.getMessage(),
        'name': record.name,
        'funcName': record.funcName,
        'lineno': record.lineno,
      }
      # TODO: リクエスト ID を追加
      # if aws_request_id:
      #     record_dict['aws_request_id'] = aws_request_id

      # 例外が発生した場合は、例外情報を追加
      # https://qiita.com/hoto17296/items/fa840823245fa4e7517d
      if record.exc_info:
        log_record['exc_traceback'] = self.formatException(record.exc_info).splitlines()

      # record.__dict__ に存在するキーのうち、STANDARD_ATTRS に含まれていないものを extra として追加
      for key, value in record.__dict__.items():
        if (key not in self.STANDARD_ATTRS) and (key not in log_record):
          log_record[key] = value

      return json.dumps(log_record, ensure_ascii=False, default=self.json_serial)

    except Exception as e:
      # json.dumps が何らかの理由で失敗したときなどにログをロストしないように値を返す
      logging.error("JsonFormatter の format 処理でエラーが発生しました: %s", e)
      return super().format(record)
