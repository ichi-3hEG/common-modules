import threading

# スレッドローカル変数は Lambda の各リクエストで個別の情報を保持するために利用
thread_local = threading.local()

class RequestIdFilter:
  """ログ出力に aws_request_id を含める。"""
  
  def filter(self, record):
    record.aws_request_id = getattr(thread_local, 'aws_request_id', None)
    return True
