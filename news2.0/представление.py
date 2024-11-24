from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.urls import reverse_lazy  
from .forms import PostForm  

class NewsCreate(CreateView):  
    form_class = PostForm  
    model = Post  
    template_name = 'post_form.html'  

    def form_valid(self, form):  
        post = form.save(commit=False)  
        post.post_type = Post.NEWS    
        return super().form_valid(form)  

class ArticleCreate(CreateView):  
    form_class = PostForm  
    model = Post  
    template_name = 'post_form.html'  

    def form_valid(self, form):  
        post = form.save(commit=False)  
        post.post_type = Post.ARTICLE  
        return super().form_valid(form)  

class NewsUpdate(UpdateView):  
    form_class = PostForm  
    model = Post  
    template_name = 'post_form.html'  

class NewsDelete(DeleteView):  
    model = Post  
    template_name = 'post_confirm_delete.html'  
    success_url = reverse_lazy('news_list')  