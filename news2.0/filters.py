import django_filters  
from .models import Post  
from django import forms  

class PostFilter(django_filters.FilterSet):  
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Название')  
    author = django_filters.ModelChoiceFilter(field_name='author__user__username', queryset=User.objects.all(), label='Автор')  
    created_at = django_filters.DateFilter(field_name='created_at', widget=forms.DateInput(attrs={'type': 'date'}), label='Дата публикации (после)')  

    class Meta:  
        model = Post  
        fields = []