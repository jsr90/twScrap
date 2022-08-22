# twScrap - scraping tweets using snscrape library

Jesús Sánchez Rodríguez

## Introduction

This python project allows to get a set of tweets in a .csv file, given a statement. In this case, I got tweets from Sevilla and Málaga's 2022 Feria with the purpose of analyse them using NLP and determine which one was the most funny.

## Input

The file 'tweets_scrap.py' contains both querys using twitter operators, that you can change however you want. This file works thanks to the class in file 'classes/Scrap.py', that allows for calling the library snscrape, executing the query and returning the dataframe.

## Output

After defining a Scrap object, we can call the searchTwt() function to get the dataframe and save it to a .csv file.

This dataframe contains these 27 columns:

['url', 'date', 'content', 'renderedContent', 'id', 'user', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'conversationId', 'lang', 'source', 'sourceUrl', 'sourceLabel', 'outlinks', 'tcooutlinks', 'media', 'retweetedTweet', 'quotedTweet', 'inReplyToTweetId', 'inReplyToUser', 'mentionedUsers', 'coordinates', 'place', 'hashtags', 'cashtags']

My data output is in the directory 'data/' in case you want it!

