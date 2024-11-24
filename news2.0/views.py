from django.views.generic import ListView  
from .filters import PostFilter  
from .tasks import schedule_weekly_newsletter  

class NewsListView(ListView):  
    model = Post  
    template_name = 'news_list.html'  
    context_object_name = 'news_list'  
    paginate_by = 10  
    schedule_weekly_newsletter(repeat=604800)

    def get_queryset(self):  
        queryset = Post.objects.filter(post_type=Post.NEWS)  
        self.filterset = PostFilter(self.request.GET, queryset=queryset)  
        return self.filterset.qs  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        context['filterset'] = self.filterset  
        return context
    
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.models import Group  
from django.http import HttpResponseRedirect  
from django.urls import reverse  

@login_required  
def become_author(request):  
    author_group = Group.objects.get(name='authors')  
    request.user.groups.add(author_group)  
    return HttpResponseRedirect(reverse('profile_view'))  

from django.shortcuts import get_object_or_404  
from django.http import HttpResponseRedirect  
from .models import Subscription, Category  

@login_required  
def subscribe_to_category(request, category_id):  
    category = get_object_or_404(Category, id=category_id)  
    Subscription.objects.get_or_create(user=request.user, category=category)  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Вернуться на предыдущую страницу