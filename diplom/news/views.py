from django.db.models import Count
from django.views.generic import TemplateView, FormView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from news.forms import NewsForm, CommentForm
from apinews.models import ApiNews, Comment
from users.models import User
from users.forms import AccountForm

class MainPageView(TemplateView):
    template_name = 'index.html'
    extra_context = {'page': ApiNews.objects.all()}

class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'


class ProfileEdit(LoginRequiredMixin, UpdateView):
    template_name = 'profile/profile_edit.html'
    form_class = AccountForm
    model = User
    success_url = reverse_lazy('profiledit')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            self.request.user.save()
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())


class PostNews(LoginRequiredMixin, FormView):
    template_name = 'post.html'
    form_class = NewsForm
    success_url = reverse_lazy('mainpage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = ApiNews.objects.all()
        return context
        
    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form = form.save(commit=False)
            form.user = self.request.user
            form.save()   
            return HttpResponseRedirect(self.get_success_url())
        return redirect('add')


class News(FormView):
    template_name = 'newspage.html'
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new'] = ApiNews.objects.get(pk=self.kwargs['id'])
        context['news'] = ApiNews.objects.all()
        context['comment'] = Comment.objects.all().filter(post = self.kwargs['id'])
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
        return reverse_lazy('news', kwargs={'id': companyid})



