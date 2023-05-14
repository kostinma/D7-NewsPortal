from django.contrib.auth.models import User
from news.models import *

# add new user if needed
new_user = User.objects.create_user('Adele James')
new_author = Author.objects.create(user = new_user)
style = 'news_piece'
the_title = 'Queen Cleopatra is Out Now On NETFLIX'
the_text = '''
I am so, so, so excited for you to take a deeper dive into this incredible woman’s life - 
all 4 eps are available to stream right away.
Feeling like the luckiest lady in the land today.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'business')
# category_3 = Category.objects.get(name = 'COVID-19')
# post_3 = Post.objects.get(pk = 3)
new_post.category.add(category_1)

#
# Post 5
#

new_user = User.objects.create_user('GOSHIPGURL')
new_author = Author.objects.create(user = new_user)
style = 'news_piece'
the_title = 'YG ANNOUNCES FINAL LINEUP FOR BABYMONS7ER, ALL 7 TRAINEES TO DEBUT IN THE GROUP'
the_text = '''
Troll master YG has announced the final lineup for BABYMONSTER. After countless pre-debut 
videos and evaluations, he revealed that all 7 trainees will debut in the group. Throwback 
to early March when he said "BABYMONSTER will never be a 7-member group. It will definitely 
be less than 7.".

In the video below, he explained that his final lineup for BABYMONSTER was Ahyeon (16), 
Ruka (21), Chiquita (14), Haram (15) and Pharita (17). Rora (14) and Asa (17) were kept out of 
lineup because he wanted Rora to debut with YG’s next girl group, and that he wanted Asa to 
partake in a girl group project he was planning in Japan.

Regarding why this decision took two weeks to make, Yang Hyun Suk shared that there were so 
many fans who wanted all seven trainees to debut, so he had to re-evaluate his decision to 
choose only five members. Elaborating on the importance of fans’ opinions, Yang Hyun Suk 
commented, “‘YG Family’ is not just the gathering of YG artists, as I believe that YG fans 
and everyone who has diligently tuned in to these broadcasts are the true YG Family.”

Yang Hyun Suk then took the opportunity to replace the poster board of BABYMONSTER’s five 
members with one of all seven trainees. Now referring to the seven-member group as BABYMONS7ER, 
Yang Hyun Suk announced, “I will take all seven with me.”

The founder explained that the five members he initially announced were chosen by YG, while 
Rora and Asa were chosen by fans. He added that they will debut as soon as possible, likely 
no later than this fall.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'business')
category_2 = Category.objects.get(name = 'rumors')
new_post.category.add(category_1, category_2)

#
# Post 6
#

new_user = User.objects.create_user('kohaku_imaki55')
new_author = Author.objects.create(user = new_user)
style = 'news_piece'
the_title = 'Looking for a Mirror of Erised fic'
the_text = '''
The author states that it is a time travel and not a time travel story. 
When Harry looks into the Mirror he goes into a vision of his life the canon life. 
When he comes out of the Mirror he is back to being a first year. 
I was looking for a different story and thought I have to come back to this. 
Unfortunately that was at least 2 years ago possibly 3. 
Now when I was looking for it I can't find it. 
Please help if you know it. 
Thank you in advance. 
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'other')
new_post.category.add(category_1)

#
# Post 7
#

new_user = User.objects.create_user('pamuphoff')
new_author = Author.objects.create(user = new_user)
style = 'article'
the_title = 'Pam Uphoff Planet'
the_text = '''
Lady Snezhana Rasputin, who at thirteen years of age was not actually a lady yet, twitched her long dark braid out of the reach of her little brother. Half brother, Nestor was an actual Lebedov, not a step daughter.
“Sneeze, do we still have to go to school?” Definitely a whine.
“Yes. We’ll be off tomorrow for the Funeral, then back for the last week, then we have almost a whole month off before the Summer Enrichment Classes start.”
A terminally cute scowl from the six year old.
“C’mon. Let’s go. It’s raining, we’ve got to go the long way around.”
He gave a terribly put upon huff, and stomped out the front door into the hallway. “The back door would have been much faster. I’m not afraid of getting wet.”
“Me neither, but I am scared of what all the ladies will say if I get soaked and bedraggled and all the people coming in for the funeral see me.” And I don’t have a lot of black in my wardrobe and I’m saving the best for the funeral.
Snezhana shouldered her computer bag and strode out after him, as he spotted Savely and ran to catch up with him.
“. . . you two made it in from the frontier.” Lord Vassily’s voice, and as she stepping in to walk across the entry, she spotted him with two other men.
Frontier? If those two are the ones we were especially waiting for, one of them is from Tier Two Mendeleev. Lord Adrian, the second of Nikanor’s three sons, so all of his have arrived. Admittedly Lord Amvrosiy, the second of Lord Ivan’s three lives all the way out on a Tier Four. Regulus? Yes, that was it.
She listened, and caught names. Yes, so all the sons are here, and it looks like their wives and children—who are all grown, and maybe with wives of their own.
The housekeeper’s kept rooms ready for them, hopefully not too near each other. The cousins appear to be sizing each other up.
Lord Amvrosiy is 7 Lebedov, and Lord Adrian is 10.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'other')
category_2 = Category.objects.get(name = 'opinion')
new_post.category.add(category_1, category_2)

#
# Post 8
#

# new_user = User.objects.create_user('pamuphoff')
# new_author = Author.objects.create(user = new_user)
style = 'article'
the_title = 'Pam Uphoff Planet, Part 2'
the_text = '''
And everyone ahead and between them is decrepit and in no shape to command the House.
Oh . . . this will be interesting, in a fashion better enjoyed on the screen than in person.
I’ll take lots of notes.
Nestor had gotten well ahead of her, and was spotted by his Grandfather.
“Nestor, come and meet some cousins!”
Sneeze slowed down, taking mental notes as Nestor galloped over to the growing crowd around the doors. One man smiled down at the boy, the other had straightened and was glaring at Lord Vassily.
“Why did you allow Prokhor to marry a fertile woman? All these late born children just turn the line into a tangle!”
Because when Nestor passes his Presentation, he’ll be slotted into the top fifty . . . and possibly a very low number, given the age and health of so many of our low numbers . . .
Lord Vassily drew himself up. “Your children,” icy tone of voice, “will still be well ahead of him in the line, Adrian.”
The man glared. “And ahead of my grandchildren.”
“As it should be. Nephew.”
Lord Adrian bowed stiffly. “Uncle Vassily.”
Lord Vassily snapped his fingers without taking his eyes off Lord Adrian. “Show Lord Adrian and his family to their rooms.
Mr. Mikhail stepped up, “This way, sir.”
Lord Adrian, turned away, still stiff, and about three fourths of the crowd followed.
The other nephew watched them out of sight, then turned back to Lord Vassily. “Well, I’m glad to see lots of young faces in the House. “His gaze dropped. “Nestor, is it. I’m please to make you acquaintance, sir.”
He stuck out his hand, and Nestor grinned and shook it.
Sneeze huffed in relief. At least 7 Lebedov seems nice. And hopefully it’s not an act.
The funeral was long, but moderately interesting. She’d had no idea Ivan had been an army officer, or that Nikanor had traveled so widely. Lord Vassily looked tired, when he’d finished, and sat down. All six sons spoke, there were lots of prayers.
Eventually they filled out to cars and drove from the church to the family plot.
More prayers, then the two caskets were lowered and they filed past and back to the limos and home.
Nestor had napped though most of the oration, and was looking like he really wanted to whine . . . Sneeze herded him off with a few other youngsters to the most distant table and the maids slid quietly in with kid style food while the elaborate seven course meal for two hundred people went on at the rest.
The teenagers, unfortunately, were at the next table and got the tail end, and slightly abbreviated, version, served last. The soup, and the fish were barely warm.
“. . . and I’ve applied to both UAH and NMCC. I guess it will all depend on my EGE score.”
What? Was that Nikanor, who was only related though his mother? He’s really an Aslanov, and his father’s one of the bad ones who’d gone to prison instead of being executed. And got killed a few years after he got out. I guess . . . he’s sort of the family charity case. But they did send him to prep school.
I guess even a criminal’s legitimate son is better then a servant’s bastard, even if Arkady was adopted and presented.
I should look into that, there’s something irregular, there.
And Yegor’s laughing at something. He went to prep school too.
The little kids got cake and juice, and then were led off somewhere to be entertained.
Sneeze eyed the older boys. All presented, but some missing. I wonder why? Well, Arkady might be at one of the other tables. The rest of the teen agers are under the fifty line, so they’re out of the spotlight. And a few clever ones managed to dodge.
The beef serving was thankfully small, and they brought the mixed vegetables with it.
I’ve got to say, the kitchen and serving staff are doing a superb job. Really organized.
The sorbet was hustled in with the fruit and cheese dishes at their table.
But it is running the servants ragged.
Then cake and finally coffee.
She made a mental note to research the extended Family. Lord Vassily is like Nestor, a very late born child, the youngest of his generation, now, with Ivan and Nikanor gone. All his distant cousins and most of their children have died.
And judging by the number of old men needing assistance today . . . and probably being exposed to who knows what contagions coming to a large funeral like this . . .
She shook her head. If I can’t get an Exec chip, I want to marry into a much smaller household. A young lord, with just a few servants and nice house. Like Dad’s house. I suppose it got sold.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'other')
category_2 = Category.objects.get(name = 'opinion')
new_post.category.add(category_1, category_2)

#
# Post 9
#

new_user = User.objects.create_user('wangden')
new_author = Author.objects.create(user = new_user)
style = 'article'
# style = 'news_piece'
the_title = 'Челябинск - прекрасный город. Почти как Воронеж :)'
the_text = '''
NEXTA na Twitterze: „State Duma deputies demand a ban on the "Family Guy" episode about the Russian city of Chelyabinsk "The artist has the right to his vision, but this is a deliberately offensive artistic image that has nothing to do with reality. This is a deliberate work against our country.… https://t.co/2b5E0XzarN” / Twitter
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'opinion')
category_2 = Category.objects.get(name = 'politics')
new_post.category.add(category_1, category_2)

#
# Post 10
#

new_user = User.objects.create_user('tanyahyatt18')
new_author = Author.objects.create(user = new_user)
style = 'article'
# style = 'news_piece'
the_title = 'Not in the Mood'
the_text = '''  
Last few days i have not been in the mood to write much on here.with all the writing i did for College and on here,i have just been taking it easy.relaxing hanging out at the pool,reading and hanging out my my friends and my dog.i went this morning and did my first workout since Friday.went to the big gym.so i think i am getting a good rest.i needed a few days to chill out.so fun just to swim and lay out.hang with my friends.walk and play with my dog.it has been hot here and muggy.but life is good.i have been making new ideals for lunch and dinner.i made a great pizza and spaghetti.casserole.putting spaghetti and sausage,onions and green peppers in casserole with sauce then a big topping of cheese on top and pepperoni slices on top.came out very yummy.hope you all had a great weekend and a great week so far.going to try to be on g-mail more now this summer.both guys i like have went back to their homes to see family and friends but will be back in 2 or 3 weeks,while i go home then go to fla and tx.Prayers to all the World.thank you for reading my blogs.love you.till my next blg......xoxoxo......out
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'other')
# category_2 = Category.objects.get(name = 'politics')
new_post.category.add(category_1)

#
# Post 11
#

new_user = User.objects.create_user('Joe Sutton')
new_author = Author.objects.create(user = new_user)
# style = 'article'
style = 'news_piece'
the_title = 'The prime suspect in the disappearance of Natalee Holloway in Aruba will be extradited to the US'
the_text = '''  
The prime suspect in the 2005 disappearance of the late American teen Natalee Holloway will be extradited to the US to face extortion and fraud charges, said officials in Peru, where Joran van der Sloot has been serving time for the murder of a Peruvian woman.

Peru “decided to agree to the request for temporary surrender … (of van der Sloot) … for his prosecution in the United States for the alleged commission of the crimes of extortion and fraud” against Holloway’s mother, Justice and Human Rights Minister Daniel Maurate Romero said in a statement Wednesday.

Natalee Holloway senior portrait 
New clues, questions in Natalee Holloway case
Van der Sloot was among the last to see Holloway alive 13 years ago in Aruba. Separately, he was convicted in 2012 of murdering Stephany Flores, 21, in his Lima hotel room and sentenced to 28 years in prison.

A Dutch national, van der Sloot has been indicted in the US on federal charges of extortion and wire fraud in connection with a plot to sell information about the whereabouts of Holloway’s remains in exchange for $250,000, officials said.

The missing 18-year-old’s mother, Beth Holloway, wired $15,000 to a bank account van der Sloot held in the Netherlands and through an attorney gave him another $10,000 in person, the indictment states. Once he had the initial $25,000, van der Sloot showed the attorney, John Kelly, where Natalee Holloway’s remains allegedly were hidden, but the information turned out to be false, the indictment states.

The indictment seeks for van der Sloot to forfeit $25,100, including $100 Beth Holloway initially transferred to van der Sloot to confirm his account.

A conviction in the United States could affect Joran van der Sloot's chances of being paroled in Peru, his lawyer says.
Joran van der Sloot challenges extradition to US in 2012
Holloway was last seen in the early hours of May 30, 2005, leaving a nightclub in Aruba with van der Sloot and two other men.

The three men – van der Sloot and brothers Deepak and Satish Kalpoe – were arrested in 2005 and released due to insufficient evidence. They were rearrested and charged in 2007 for “involvement in the voluntary manslaughter of Natalee Holloway or causing serious bodily harm to Natalee Holloway, resulting in her death,” Aruban prosecutors said at the time.

But a few weeks later, an Aruban judge ordered van der Sloot’s release, citing a lack of direct evidence that Holloway died from a violent crime or that van der Sloot was involved in such a crime. The Kalpoe brothers were also released.

Holloway’s body has not been found. An Alabama judge signed an order in 2012 declaring her legally dead.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'top_stories')
category_2 = Category.objects.get(name = 'criminal')
new_post.category.add(category_1, category_2)


#
# Post 12
#

new_user = User.objects.create_user('Jonah E. Bromwich')
new_author = Author.objects.create(user = new_user)
# style = 'article'
style = 'news_piece'
the_title = 'Daniel Penny Will Be Charged in Subway Chokehold Killing of Jordan Neely'
the_text = '''
Mr. Penny choked Mr. Neely for several minutes on the floor of an F train. He is expected to surrender on Friday and be charged with manslaughter.
Daniel Penny, the 24-year-old Marine veteran who choked and killed a homeless man on the subway last week, will face a charge of second-degree manslaughter and is expected to appear in Manhattan Criminal Court on Friday.
The Manhattan district attorney’s office confirmed in a statement that it planned to charge Mr. Penny in the killing of the man, Jordan Neely.
“Daniel Penny will be arrested on a charge of manslaughter in the second degree,” the statement said. “We cannot provide any additional information until he has been arraigned in Manhattan Criminal Court, which we expect to take place tomorrow.”
Mr. Penny encountered Mr. Neely, 30, on an F train on May 1 and placed him in a chokehold, killing him. Witnesses told the police that Mr. Neely had been shouting at passengers, but there has been no indication that he physically attacked anyone.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
# category_1 = Category.objects.get(name = 'top_stories')
category_1 = Category.objects.get(name = 'criminal')
new_post.category.add(category_1)

#
# Post 13
#

new_user = User.objects.create_user('Deirdre Walsh')
new_author = Author.objects.create(user = new_user)
# style = 'article'
style = 'news_piece'
the_title = 'As debt ceiling talks progress, Biden and lawmakers are postponing their meeting'
the_text = '''
President Biden will not meet with congressional leaders Friday to discuss the debt ceiling as planned, according to House Speaker Kevin McCarthy's office.
Biden was set to meet McCarthy, Senate Minority Leader Mitch McConnell, House Democratic Leader Hakeem Jeffries and Senate Majority Leader Chuck Schumer at the White House to continue talks on lifting the nation's debt limit, which expires as soon as early June. An meeting on Tuesday ended with no resolution.
McCarthy's office said Friday that he, Biden and the other leaders agreed that their staffs should continue to meet.
A source familiar with the meetings told NPR that Biden and the congressional leaders postponed their gathering because did not want interrupt the progress that was being made.
"This is a positive development. Meetings are progressing. Staff is continuing to meet and it wasn't the right moment to bring it back to principals," said the source, who spoke on condition of anonymity to describe private meetings.
McCarthy told reporters he expected another meeting with the president and congressional leaders next week.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'national')
category_2 = Category.objects.get(name = 'economy')
new_post.category.add(category_1, category_2)

#
# Post 14
#

new_user = User.objects.create_user('SUZAN FRASER')
new_author = Author.objects.create(user = new_user)
style = 'article'
# style = 'news_piece'
the_title = "Turkey’s closely watched elections may stretch Erdogan’s rule or set country on new course"
the_text = '''
ANKARA, Turkey (AP) — In the year in which the Turkish republic marks its centenary, the country is being closely watched to see if a united opposition can succeed in unseating an increasingly authoritarian leader in the NATO-member country.
Turkey’s presidential and parliamentary elections, taking place on Sunday, could stretch President Recep Tayyip Erdogan’s rule into a third decade — or they could set the country on a new course.
Kemal Kilicdaroglu, the leader of the secular, center-left Republican People’s Party, or CHP, is the main challenger trying to dislodge Erdogan after 20 years in office. The 74-year-old is the joint candidate of a six-party alliance that has vowed to dismantle an executive presidential system that Erdogan installed and return the country to a parliamentary democracy with checks and balances.
As well as the opposition alliance, Kilicdaroglu has clinched the support of the country’s pro-Kurdish party, which garners around 10% of the votes. And polls have given him a slight lead. The race is so close, however, that it is likely to be decided in a runoff between the two frontrunners on May 28.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'world_news')
category_2 = Category.objects.get(name = 'politics')
new_post.category.add(category_1, category_2)

#
# Post 15
#

new_user = User.objects.create_user('Antonio G. Di Benedetto')
new_author = Author.objects.create(user = new_user)
style = 'article'
# style = 'news_piece'
the_title = 'PSA: if you bought The Legend of Zelda: Tears of the Kingdom digitally, get preloading now'
the_text = '''
Did you preorder The Legend of Zelda: Tears of the Kingdom on the Nintendo eShop? Cool. Wait, did you also preorder it using Nintendo’s Game Voucher so you got it for cheaper? Even better — extra points for you! But regardless of how much you paid, if you opted for the digital version of TOTK, you should fire up your Switch and get downloading if you’d like to start playing when the game goes live in the US tonight a 12:00AM ET on May 12th.
While Tears is already playable in time zones that live in the future, and players are already getting up to, well, umm... stuff — we here in the States get to begin at midnight ET / 9:00PM PT (curse you, left-coasters and your respectable bedtimes tonight). TOTK is a 16GB download from the eShop, so you don’t want to be stuck losing precious game time waiting over an hour extra to get into Hyrule. Plus, if you haven’t used your Switch a whole lot recently, you may have a lingering software update for your console that also needs to get done.
It took me about an hour and 20 minutes to run an update and install the game, and I’d be pretty upset with myself if I forgot to do it well ahead of time. Also, don’t forget that if you have a non-OLED Switch, you’re working with just 32GB of built-in storage — of which TOTK will consume more than half. So make sure you’ve got the space or a microSD card handy.
So get preloading. It’s also the only way to play and win the “stare at your homescreen waiting for the game to unlock at midnight” prologue mini-game.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'education')
category_2 = Category.objects.get(name = 'sport')
category_3 = Category.objects.get(name = 'analysis')
new_post.category.add(category_1, category_2, category_3)

#
# Post 16
#

new_user = User.objects.create_user('WFAA Staff')
new_author = Author.objects.create(user = new_user)
# style = 'article'
style = 'news_piece'
the_title = "2023 ACM Awards: Everything you need to know about this year's show -- including red carpet coverage"
the_text = '''
Our red carpet coverage of the 58th Academy of Country Music Awards starts at 3:30 p.m. Thursday. The awards themselves will air on Amazon Prime at 6 p.m.
FRISCO, Texas — On Thursday, May 11, the 2023 Academy of County Music Awards will take place at the Ford Center at The Star in Frisco. 
Hosted by country music legends Dolly Parton and Garth Brooks, this 58th edition of the annual awards show will, for the very first time in the awards show's history, be broadcast on the streaming service Amazon Prime starting at 6 p.m. CT.
It's the first time the ACM Awards have been hosted in Texas since the 50th anniversary of the awards show was hosted at another Dallas Cowboys facility -- AT&T Stadium in Arlington - in 2015. 
Before the show itself kicks off, however, WFAA Daybreak co-anchor Marc Istook will be interviewing the attendees of this year's event from the red carpet as they arrive on the scene. That coverage will begin right here at 3:30 p.m.
Beyond that, here's everything else you need to know about this year's awards show.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'national')
category_2 = Category.objects.get(name = 'top_stories')
new_post.category.add(category_1, category_2)

#
# Post 17
#

new_user = User.objects.create_user('Jordain Carney')
new_author = Author.objects.create(user = new_user)
style = 'article'
# style = 'news_piece'
the_title = 'House GOP lays down its border marker as Trump-era migrant policy runs out'
the_text = '''
House Republicans passed a sweeping border bill Thursday after months of intraparty sniping, a symbolic victory achieved just hours before a Trump-era migrant expulsion policy expires.
The bill is stacked with long-sought GOP priorities, including restarting construction on the border wall and placing new limits on asylum seekers. Republicans still lost two of their own members — Reps. Thomas Massie (R-Ky.) and John Duarte (R-Calif.) — despite days of around-the-clock negotiations that resulted in multiple last-minute changes.
The legislation is dead on arrival in the Democratic-controlled Senate. Instead, several senators are focused on trying to find a narrow, bipartisan solution focused on the end of Title 42, a law that permits the U.S. to deny asylum and migration claims for public health reasons.
But Republicans view the ability to pass their larger legislation as a dual political win: a political cudgel they can use to whack Democrats and a showcase of hard-fought unity on a divisive issue. The party’s immigration priorities had sparked weeks of high-profile infighting earlier this year — when lawmakers had to punt more conservative asylum legislation that caused heartburn among some centrists — a storyline that has replayed several times since January as House GOP leaders maneuver around their four-vote margin.
“We all wanted to achieve the same thing, but we started off in very different places,” Majority Leader Steve Scalise (R-La.) said in an interview Thursday.
'''
new_post = Post.objects.create(
    post_type = style,
    author = new_author,
    title = the_title,
    body = the_text,
    rating = 0
)

# Category.objects.create(name = cat)
# 'other',    'rumors',            'education',   'royalties', 'sport',
# 'business', 'national',          'world_news',  'politics',  'science',
# 'economy',  'breaking_news',     'top_stories', 'analysis',  'opinion',
# 'criminal', 'financial_markets', 'health',      'COVID-19'
category_1 = Category.objects.get(name = 'national')
category_2 = Category.objects.get(name = 'politics')
new_post.category.add(category_1, category_2)


# add new user if needed
# User.objects.create_user('IvanIvanich')
# add new author if needed
# Author.objects.create(user = User.objects.get(username = 'IvanIvanich'))
# add new post
# author_1 = Author.objects.get(user = User.objects.get(username = 'IvanIvanich'))
# the_title = "Many Workers Remained Sidelined, With Job Losses Concentrated in Low-Paid Industries"
# the_text = """The unemployment """

# will add categories later
#Post.objects.create(post_type = 'article',
#                    author    = author_1,
#                    title     = the_title,
#                    body      = the_text,
#                    rating    = 0   )

# add categories to the post
# add category if needed
#     Category.objects.create(name = cat)
# category_1 = Category.objects.get(name = 'economy')
# category_2 = Category.objects.get(name = 'health')
# category_3 = Category.objects.get(name = 'COVID-19')
# post_1.category.add(category_1, category_2, category_3)




# End of file
