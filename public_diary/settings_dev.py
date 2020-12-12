from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
# Trueにしておくとエラー発生時にデバッグ情報が画面に表示される。
# 本番運用時にはセキュリティの観点からFalseにしておく必要がある！！
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガー設定(ログのエントリーポイント)
    'loggers': {
        # Djangoが利用するロガー
        # ハンドラーとの紐づけ
        # ログレベルの設定
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },

        # yourdiaryアプリケーションが利用するロガー
        # ハンドラーとの紐づけ
        # ログレベルの設定
        'yourdiary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定(ログ出力先の設定)
    # フォーマッタとの紐づけ
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定(ログ出力先の設定)
    # ログをタブ区切りで出力するよう設定している。
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    },
}

#開発時にはメール送信先をコンソールに設定するための記載
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'