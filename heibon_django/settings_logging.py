import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s a',
        },
        'heibon': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "%(asctime)s",
                "%(name)s:%(lineno)d",
                "%(message)s",
                "%(threadName)s",
            ])
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',  # ログレベル
            'class': 'logging.FileHandler',  # ハンドラー名
            'filename': os.path.join(BASE_DIR, 'heibon-django.log'),  # 出力先
            'formatter': 'heibon',  # フォーマット
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'heibon'
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console","file"
        ]
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
