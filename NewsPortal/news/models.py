from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

'''
Class description
'''
class Category(models.Model):
    CATEGORIES = [
        'other',
        'rumors',
        'education',
        'royalties', # aka Prince Harry
        'sport',
        'business',
        'national',
        'world_news',
        'politics',
        'science',
        'economy',
        'breaking_news',
        'top_stories',
        'analysis',
        'opinion',
        'criminal',
        'financial_markets',
        'health',
        'COVID-19'
    ]
    name = models.CharField(max_length=32, unique=True, default='other')

    def __str__(self):
        return f'{self.name}'

'''
Class description, will add later
'''
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    '''
    Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
    Он состоит из следующего:
    суммарный рейтинг каждой статьи автора умножается на 3;
    суммарный рейтинг всех комментариев автора;
    суммарный рейтинг всех комментариев к статьям автора.
    '''
    def update_rating(self):
        rating_articles_author = Post.objects.filter(author_id=self).aggregate(sum_articles=Sum('rating'))['sum_articles']
        rating_comment_author = Comment.objects.filter(user_id=self.user).aggregate(sum_articles=Sum('rating'))['sum_articles']
        rating_comment_posts = Comment.objects.filter(post__author__user=self.user).aggregate(sum_posts=Sum('rating'))['sum_posts']
        self.rating = 3*rating_articles_author + rating_comment_author + rating_comment_posts
        self.save()

    def __str__(self):
        return f'{self.user}'

'''
Class description
'''
class Post(models.Model):
    POSTS = ['article', 'news_piece']
    post_type = models.CharField(max_length=16, default='news_piece')
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.TextField(default='Unspecified Title')
    body = models.TextField(default='Unspecified Article Body')
    rating = models.IntegerField(default=0)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()
        return self

    def dislike(self):
        self.rating -= 1
        self.save()
        return self

    ''' return beginning 124 characters of the article'''
    def preview(self):
        return str(self.body)[0:124] + '...'

    def __str__(self):
        return f'{self.title} \n {self.body}\n\n'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


'''
Class description:
Intermediate type to provide a many-to-many connection between classes Post and Category
'''
class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

'''
Class comment
'''
class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank = False)
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()
        return self

    def dislike(self):
        self.rating -= 1
        self.save()
        return self

# End of file
