SECRET_KEY = 'superset'
# SQLALCHEMY_DATABASE_URI = 'postgresql://superset:superset@postgres/superset'
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False
BABEL_DEFAULT_LOCALE = "en"
LANGUAGES = {
    "zh": {"flag": "cn", "name": "简体中文1"},
    "en": {"flag": "us", "name": "English"},
}
PUBLIC_ROLE_LIKE = "Gamma"
FEATURE_FLAGS = {"EMBEDDED_SUPERSET": True}
# Dashboard embedding
GUEST_ROLE_NAME = "Public"
GUEST_TOKEN_JWT_SECRET = "test-guest-secret-change-me"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 300

# 允许跨域访问的域名
ALLOW_ORIGINS = ['localhost:8088']

# CSRF Config
WTF_CSRF_ENABLED = False
# WTF_CSRF_TIME_LIMIT = 300

# Talisman Config
TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "frame-ancestors": ALLOW_ORIGINS
    },
    "force_https": False,
    "force_https_permanent": False,
    "frame_options": "ALLOWFROM",
    "frame_options_allow_from": "*"
}


ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ALLOW_ORIGINS
}
