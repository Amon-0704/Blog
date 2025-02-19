import logging

# ログの設定
logging.basicConfig(
    level=logging.DEBUG,  # ログレベルをDEBUGに設定
    format='%(asctime)s - %(levelname)s - %(message)s',  # 出力形式
)

# ログを出力する関数
def log_message(level, message):
    if level == 'debug':
        logging.debug(message)
    elif level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)
    else:
        logging.error("無効なログレベルです。")

# 使用例
log_message('debug', "デバッグメッセージ")
log_message('info', "インフォメーションメッセージ")
log_message('warning', "警告メッセージ")
log_message('error', "エラーメッセージ")
log_message('critical', "重大なエラーメッセージ")
log_message('invalid', "無効なログレベル")
