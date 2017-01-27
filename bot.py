#!/usr/bin/python3
import praw, re, time

# Read id, secret, and password from text file - security!
with open('client_id.txt', 'r') as client_id_file:
    # Parse into a string, and get rid of trailing newlines.
    client_id = client_id_file.read().replace('\n', '')

with open('secret.txt', 'r') as secret_file:
    # Parse into a string, and get rid of trailing newlines.
    secret = secret_file.read().replace('\n', '')

with open('password.txt', 'r') as password_file:
    # Parse into a string, and get rid of trailing newlines.
    password = password_file.read().replace('\n', '')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret,
                     user_agent='STEAMworksbot by /u/ErikBoesen',
                     username='STEAMworksbot',
                     password=password)

subreddit = reddit.subreddit('FRC')


print('Listening for new comments on r/' + subreddit.display_name + '...')
while True:
    print('Checking for comments...')
    for comment in subreddit.stream.comments():
        if re.search('[sS]teamworks', comment.body):
            comment.reply('*STEAMworks')
            print('Responded to the following comment: "' + comment.body + '"')
    time.sleep(600)
