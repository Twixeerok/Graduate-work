from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from news.forms import NewsForm, CommentForm
from apinews.models import ApiNews, Comment, Category, Like
from users.models import User
from users.forms import AccountForm, AccountForms
from django.core.paginator import Paginator

  
class SearchMixin:
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search','')
        if search:
            context['search'] = ApiNews.objects.filter(title__icontains=search)
        else:
            context['search'] = ApiNews.objects.all()
        return context



class Search(SearchMixin, TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MainView(SearchMixin, TemplateView):
    template_name = 'main.html'
    title = 'lox'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = Category.objects.all()
        return context
    

class MainPageView(SearchMixin, ListView):
    template_name = 'index.html'
    paginate_by = 3
    model = ApiNews
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new'] = Category.objects.get(slug=self.kwargs['slug'])
        context['page'] = ApiNews.objects.filter(category=Category.objects.get(slug=self.kwargs['slug']))
        return context

    def get_queryset(self):
        return ApiNews.objects.filter(category=Category.objects.get(slug=self.kwargs['slug']))

class Profile(SearchMixin, LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

class UserProfile(SearchMixin, LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prof'] = User.objects.get(pk=self.kwargs['id'])
        return context

class ProfileEdit(SearchMixin, LoginRequiredMixin, UpdateView):
    template_name = 'profile/profile_edit.html'
    form_class = AccountForms
    model = User
    success_url = reverse_lazy('category:profiledit')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            self.request.user.save()
            return HttpResponseRedirect(self.get_success_url()) 

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())


class PostNews(SearchMixin, LoginRequiredMixin, FormView):
    template_name = 'post.html'
    form_class = NewsForm
    success_url = reverse_lazy('category:mainpage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = ApiNews.objects.all()
        context['cho'] = Category.objects.all()
        return context
        
    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form = form.save(commit=False)
            form.users = self.request.user
            form.save()   
            return HttpResponseRedirect(self.get_success_url())
 


class News(SearchMixin, FormView):
    template_name = 'newspage.html'
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new'] = ApiNews.objects.get(pk=self.kwargs['id'])
        context['news'] = ApiNews.objects.all()
        context['comment'] = Comment.objects.all().filter(post = self.kwargs['id'])
        context['like'] = Like.objects.all().filter(post = self.kwargs['id'])
        return context

    def form_valid(self, form):
        posts = get_object_or_404(ApiNews, id=self.kwargs['id'])
        form = form.save(commit=False) 
        form.user = self.request.user
        form.post = posts
        form.save()
        return super(News, self).form_valid(form)

    def get_success_url(self):
        companyid=self.kwargs['id']
        return reverse_lazy('category:news', kwargs={'id': companyid})



class Likes(View):
    def post(self, *args, **kwargs):
        blog_post_id = int(self.request.POST.get('blog_post_id'))
        user_id = int(self.request.POST.get('user_id'))
        url_from = self.request.POST.get("url_from")
        
        user_inst = User.objects.get(id=user_id)
        blog_post_inst = ApiNews.objects.get(id=blog_post_id)
        try:
            blog_like_inst = Like.objects.get(post = blog_post_inst, user = user_inst)
        except:
            block_like = Like(post=blog_post_inst, \
                                user=user_inst, \
                                    like = True 
            )
            block_like.save()
        return redirect(url_from)

class RemoveLike(View):
    def post(self, *args, **kwargs):
        blog_post_id = int(self.request.POST.get('blog_post_id'))
        url_from = self.request.POST.get('url_from')
        blog_like = Like.objects.get(post_id = blog_post_id)
        blog_like.delete()
        return redirect(url_from)