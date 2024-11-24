INSTALLED_APPS = [  
    'django.contrib.sites', 
    'allauth',  
    'allauth.account',  
    'allauth.socialaccount',  
    'allauth.socialaccount.providers.yandex',  
]  

SITE_ID = 1  


ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True  # Параметр для перенаправления после входа  
LOGIN_URL = '/accounts/login/'  # URL для входа  
LOGIN_REDIRECT_URL = '/success/'  # URL для перенаправления после входа  
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'  # URL для возврата после выхода  

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'your_email@gmail.com'  
EMAIL_HOST_PASSWORD = 'your_password'  # Лучше всего использовать переменные окружения  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True  
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'

# Настройки для Yandex  
SOCIALACCOUNT_PROVIDERS = {  
    'yandex': {  
        'APP': {  
            'client_id': 'YOUR_CLIENT_ID',  
            'secret': 'YOUR_SECRET',  
            'key': ''  
        }  
    }  
}