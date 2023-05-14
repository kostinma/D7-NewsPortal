from django.contrib.auth.models import User
from news.models import *

# Add categories to DB
for cat in Category.CATEGORIES:
    Category.objects.create(name = cat)

# Add users to DB
User.objects.create_user('IvanIvanich')
User.objects.create_user('cheburashka')
User.objects.create_user('aktin')
User.objects.create_user('taboyashi')
User.objects.create_user('mukhtar')

# Add authors to DB
Author.objects.create(user = User.objects.get(username = 'IvanIvanich'))
Author.objects.create(user = User.objects.get(username = 'taboyashi'))

#
# Добавить 2 статьи ('article') и 1 новость ('news_piece')
#

#
# Article 1

# Let's get authors by name, alternative to get(pk=...)
author_1 = Author.objects.get(user = User.objects.get(username = 'IvanIvanich'))
the_title = "Many Workers Remained Sidelined, With Job Losses Concentrated in Low-Paid Industries"
the_text = """
The unemployment rate jumped in April 2020 to a level not seen since the 1930s — 
and stood at 4.9 percent in October 2021, compared with 3.5 percent in February 2020. 
That official unemployment rate, moreover, understated job losses.
There were still 4.2 million fewer jobs in October 2021 than in February 2020. 
The majority of jobs lost in the crisis have been in industries that pay low average wages, 
with the lowest-paying industries accounting for 30 percent of all jobs but 59 percent of the 
jobs lost from February 2020 to October 2021, according to Labor Department employment data. 
Jobs were down nearly twice as much in low-paying industries (4.5 percent) as in medium-wage 
industries (2.6 percent) and roughly 15 times as much as in high-wage industries (0.3 percent) 
during this period. (See Figure 11.)
"""
category_1 = 'economy'
category_2 = 'health'
category_3 = 'COVID-19'
# will add categories later
Post.objects.create(post_type = 'article',
                    author    = author_1,
                    title     = the_title,
                    body      = the_text,
                    rating    = 0   )


#
# Article 2
author_2 = Author.objects.get(user = User.objects.get(username = 'taboyashi'))
the_title = 'Artemis program'
the_text = '''
The Artemis program is a robotic and human Moon exploration program led by the United States' 
National Aeronautics and Space Administration (NASA) along with three partner agencies: 
European Space Agency (ESA), Japan Aerospace Exploration Agency (JAXA), and Canadian Space Agency (CSA). 
The Artemis program intends to reestablish a human presence on the Moon for the first time since the 
Apollo 17 mission in 1972. The major components of the program are the Space Launch System (SLS), 
Orion spacecraft, Lunar Gateway space station and the commercial Human Landing Systems. 
The program's long-term goal is to establish a permanent base camp on the Moon and facilitate human missions to Mars.
'''
category_1 = 'science'
category_2 = 'top_stories'
# will add categories later
Post.objects.create(post_type = 'article',
                    author    = author_2,
                    title     = the_title,
                    body      = the_text,
                    rating    = 0   )

#
# News piece
author_3 = Author.objects.get(user = User.objects.get(username = 'taboyashi'))
the_title = 'Prince Harry strict dating rule he decided to ditch when he met Meghan Markle'
the_text = '''
When Prince Harry's romance with Meghan Markle first blossomed, his life was very different to what it is now.
Back then in 2016, he was a full-time working royal living in his Kensington Palace cottage close to his now estranged brother Prince William.
But when he first started dating former Suits actress Meghan, he has previously admitted that he knew she'd be the one he would marry from early in their romance.
So much so, that he also admits that a strict dating rule he once used to strictly follow was quickly ditched by him as soon as he met his future wife.
'''
category_1 = 'rumors'
category_2 = 'royalties'
category_3 = 'breaking_news'
category_4 = 'top_stories'
# will add categories later
Post.objects.create(post_type = 'news_piece',
                    author    = author_3,
                    title     = the_title,
                    body      = the_text,
                    rating    = 0   )

post_1 = Post.objects.get(pk = 1)
post_2 = Post.objects.get(pk = 2)
post_3 = Post.objects.get(pk = 3)

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# ... Working progress ...
category_1 = Category.objects.get(name = 'economy')
category_2 = Category.objects.get(name = 'health')
category_3 = Category.objects.get(name = 'COVID-19')
post_1.category.add(category_1, category_2, category_3)

category_1 = Category.objects.get(name = 'science')
category_2 = Category.objects.get(name = 'top_stories')
post_2.category.add(category_1, category_2)

category_1 = Category.objects.get(name = 'rumors')
category_2 = Category.objects.get(name = 'royalties')
category_3 = Category.objects.get(name = 'breaking_news')
category_4 = Category.objects.get(name = 'top_stories')
post_3.category.add(category_1, category_2, category_3, category_4)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

# Comments
comment_1_post_1 = Comment.objects.create(post = post_1,
                                          user = User.objects.get(username = 'aktin'),
                                          comment = 'I do not believe you!. COVID-19 is fake!',
                                          rating = 0)
comment_2_post_1 = Comment.objects.create(post = post_1,
                                          user = User.objects.get(username = 'cheburashka'),
                                          comment = 'You are an idion! Spetznaz is better than SAS!',
                                          rating = 0)
comment_3_post_1 = Comment.objects.create(post = post_1,
                                          user = User.objects.get(username = 'IvanIvanich'),
                                          comment = 'Actually, I know better than any of you.',
                                          rating = 0)

comment_1_post_2 = Comment.objects.create(post = post_2,
                                          user = User.objects.get(username = 'mukhtar'),
                                          comment = 'Earth is flat!',
                                          rating = 0)
comment_2_post_2 = Comment.objects.create(post = post_2,
                                          user = User.objects.get(username = 'taboyashi'),
                                          comment = 'No, it is not! I saw it from space myself.',
                                          rating = 0)

comment_1_post_3 = Comment.objects.create(post = post_3,
                                          user = User.objects.get(username = 'aktin'),
                                          comment = 'Poor Queen.',
                                          rating = 0)
comment_2_post_3 = Comment.objects.create(post = post_3,
                                          user = User.objects.get(username = 'aktin'),
                                          comment = 'God Save the Queen!',
                                          rating = 0)

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post_1.like()
post_1.like()
post_1.like()
post_1.dislike()

post_2.dislike()
post_2.like()
post_2.dislike()
post_2.like()
post_2.like()

post_3.like()
post_3.like()
post_3.dislike()

comment_1_post_1.like()
comment_1_post_1.like()
comment_1_post_1.like()

comment_2_post_1.dislike()
comment_2_post_1.dislike()
comment_2_post_1.like()

comment_3_post_1.like()
comment_3_post_1.like()

comment_1_post_2.like()
comment_2_post_2.like()

comment_1_post_3.dislike()
comment_2_post_3.like()

# Обновить рейтинги пользователей.
author_1.update_rating()
author_2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
print("The highest rating author is ", Author.objects.all().order_by('rating')[0].user.username)
print("Rating of the best author=", Author.objects.all().order_by('rating')[0].rating)

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
the_best_article = Post.objects.all().order_by('rating')[0]
print("The best article by ranking based on likes/dislikes :")
print("By ", the_best_article.author.user.username)
print("Posted ", the_best_article.time_in)
print("Ranking based on likes/dislikes=", the_best_article.rating)
print("Titled: ", the_best_article.title)
the_best_article.preview()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
i_c = 1
print("Comments for the best articles:")
for c in Comment.objects.filter(post = the_best_article):
    print("Comment ", i_c)
    print("Posted ", c.time_in)
    print("Rating ", c.rating)
    print("By ", c.user.username)
    print(c.comment)
    print()
    i_c += 1

# end of file
