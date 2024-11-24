from django.apps import AppConfig  

class YourAppConfig(AppConfig):  
    name = 'your_app_name'  

    def ready(self):  
        import your_app_name.signals  