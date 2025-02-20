import logging

# ログの設定
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# ログの設定 (ファイルに記録)
# logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# ログメッセージ
logging.debug('デバッグ情報')
logging.info('情報')
logging.warning('警告')
logging.error('エラー')
logging.critical('致命的なエラー')
