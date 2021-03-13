from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post , Like


class TweetListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-create_date']


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['body']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TweetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    fields = ['body']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'tweet_confirm_delete.html'
    fields = ['body']
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TweetLikeView(LoginRequiredMixin, CreateView):
    model = Like
    # template_name = 'create.html'
    fields = ['users']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)