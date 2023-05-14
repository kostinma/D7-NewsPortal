from datetime import datetime
from pprint import pprint

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .filters import SearchPostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    # ordering = 'title'
    ordering = 'time_in'
    # Or, alternatively
    # queryset = Post.objects.order_by('time_in')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # pprint(context)
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class SearchPostList(ListView):
    model = Post
    # ordering = 'title'
    ordering = 'time_in'
    # Or, alternatively
    # queryset = Post.objects.order_by('time_in')
    template_name = 'news_search.html'
    context_object_name = 'news_search'
    paginate_by = 2

    # redefine function of getting list of Posts
    # SearchPostFilter is in filters.py
    def get_queryset(self):
        # get request
        queryset = super().get_queryset()

        # self.request.Get has an object of class QueryDict
        # keep filtration in class object so that will add it into context
        # and use in template.
        # SearchPostFilter is found in filters.py
        self.filterset = SearchPostFilter(self.request.GET, queryset)

        # return filtered list
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()

        # self.get_queryset(self) created an object of filtered list
        context['filterset'] = self.filterset

        # pprint(context)
        return context

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            path_info = self.request.META['PATH_INFO']
            if path_info == '/news/create/':
                post.post_type = Post.POSTS[1]
                # Post.POSTS = ['article', 'news_piece']
            elif path_info == '/article/create/':
                post.post_type = Post.POSTS[0]
                # Post.POSTS = ['article', 'news_piece']
            else:
                raise ValidationError(
                    'PostCreate.from_valid(): Wrong url.'
                )

        post.save()
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_search')

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

# End of file
