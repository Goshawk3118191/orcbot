import praw

bot = praw.Reddit(user_agent='Orcbot 1.0', 
                     client_id='ImMKcDDOn0vr4g', 
                     client_secret='	wLFgnqtnzrMdwRztCGihApOCa-M', 
                     username='OrcBot', 
                     password='orcbot1238')

subreddit = bot.subreddit('funny')

comments = subreddit.stream.comments()
for comment in comments:
    text = comment.body
    author = comment.author
    if 'and my axe' in text.lower():
        message = "SHUT UP STUPID DWARF!"
        comment.reply(message)