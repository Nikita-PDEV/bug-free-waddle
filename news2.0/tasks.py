from django.core.mail import send_mail  
from django.utils import timezone  
from datetime import timedelta  
from .models import Subscription, Article  
from background_tasks import background  

@background(schedule=60)  
def schedule_weekly_newsletter():  
    send_weekly_newsletter()
    
def send_weekly_newsletter():  
    # Получаем дату недели назад  
    last_week = timezone.now() - timedelta(days=7)  

    # Получаем подписчиков  
    subscriptions = Subscription.objects.all()  

    for subscription in subscriptions:  
        new_articles = Article.objects.filter(category=subscription.category, created_at__gte=last_week)  

        if new_articles.exists():  
            article_links = '\n'.join([f"{article.title}: http://yourdomain.com/articles/{article.id}" for article in new_articles])  
            email_subject = f"Новые статьи в категории {subscription.category.name}"  
            email_message = f"Привет! Вот новые статьи в категории {subscription.category.name} за последнюю неделю:\n\n{article_links}"  

            send_mail(  
                email_subject,  
                email_message,  
                'your_email@gmail.com',   
                [subscription.user.email],  
                fail_silently=False,  
            )