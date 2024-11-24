from django.db.models.signals import post_save  
from django.dispatch import receiver  
from django.core.mail import send_mail  
from django.contrib.auth.models import User  

@receiver(post_migrate)  
def create_user_groups(sender, **kwargs):  
    if sender.name == 'your_app_name':  
        Group.objects.get_or_create(name='common')  
        Group.objects.get_or_create(name='authors')
        from django.conf import settings  

from django.contrib.auth.models import User  
from django.db.models.signals import post_save  
from django.dispatch import receiver  
from django.contrib.auth.models import Group  

@receiver(post_save, sender=User)  
def add_user_to_common(sender, instance, created, **kwargs):  
    if created:  
        common_group = Group.objects.get(name='common')  
        instance.groups.add(common_group)
        
from django.contrib.auth.models import Permission, Group  

def assign_permissions_to_authors():  
    author_group = Group.objects.get(name='authors')  
    permission_add = Permission.objects.get(codename='add_post')  
    permission_change = Permission.objects.get(codename='change_post')  
    
    author_group.permissions.add(permission_add)  
    author_group.permissions.add(permission_change)  

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  
from django.views.generic import CreateView, UpdateView  
from .models import Post  

@receiver(post_save, sender=User)  
def send_welcome_email(sender, instance, created, **kwargs):  
    if created:  
        subject = "Добро пожаловать на News Portal!"  
        message = "Спасибо за регистрацию на нашем новостном портале. Мы рады видеть вас!"  
        send_mail(  
            subject,  
            message,  
            'your_email@gmail.com',   
            [instance.email],  
            fail_silently=False,  
        )  

class AuthorRequiredMixin(UserPassesTestMixin):  
    def test_func(self):  
        return self.request.user.groups.filter(name='authors').exists()  

class PostCreateView(AuthorRequiredMixin, CreateView):  
    model = Post  
    template_name = 'post_form.html'  
    fields = ['title', 'content']  

class PostUpdateView(AuthorRequiredMixin, UpdateView):  
    model = Post  
    template_name = 'post_form.html'  
    fields = ['title', 'content']