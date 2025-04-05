import logging
from lambda_logger import init_logger, thread_local as logger_thread_local

logger = init_logger(logging.INFO)

def lambda_handler(event, context):
    logger_thread_local.aws_request_id = context.aws_request_id
    logger.info('Hello World!')
