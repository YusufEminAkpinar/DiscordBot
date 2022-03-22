import asyncpraw
import random
import sys
sys.path.insert(0, 'C:\\Users\\Hardal\\PycharmProjects\\dc_bot\\Others')
from cred import reddit_sec, reddit_id, reddit_uname, reddit_pass


async def red_post(sub= 'shitposting'):
    global will_returned
    reddit = asyncpraw.Reddit(
        client_id=reddit_id,
        client_secret=reddit_sec,
        user_agent="For my Discord Bot",
        password=reddit_pass,
        username=reddit_uname,
    )
    subreddit = await reddit.subreddit(sub)
    posts = []
    async for submission in subreddit.hot(limit=25):
        posts.append(submission)
    i = random.randint(0, 25)
    await reddit.close()
    url = posts[i].url
    title = posts[i].title
    text = posts[i].selftext
    permalink = posts[i].permalink
    if url.startswith('https://v.redd.it'):
        url = f'https://reddit.com/{permalink}'
    will_returned = f"""
    {title}
    {url}
    {text}
    """
    if posts[i].over_18:
        return 'krdşm bu NSFW porrrrrno olabilir güvenemedim.'
    else:
        return will_returned

async def secret_red_post(sub= 'shitposting'):
    global will_returned
    reddit = asyncpraw.Reddit(
        client_id=reddit_id,
        client_secret=reddit_sec,
        user_agent="For my Discord Bot",
        password=reddit_pass,
        username=reddit_uname,
    )
    subreddit = await reddit.subreddit(sub)
    posts = []
    async for submission in subreddit.hot(limit=25):
        posts.append(submission)
    i = random.randint(0, 25)
    await reddit.close()
    url = posts[i].url
    title = posts[i].title
    text = posts[i].selftext
    permalink = posts[i].permalink
    if url.startswith('https://v.redd.it'):
        url = f'https://reddit.com/{permalink}'
    will_returned = f"""
    {title}
    {url}
    {text}
    """
    return will_returned
