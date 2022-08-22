import snscrape.modules.twitter as sntwitter
import pandas as pd

class Scrap:

    def __init__(self, query, max):
        
        self.query = query
        self.max = max
        self.columns = ['url', 'date', 'content', 'renderedContent', 'id', 'user', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'conversationId', 'lang', 'source', 'sourceUrl', 'sourceLabel', 'outlinks', 'tcooutlinks', 'media', 'retweetedTweet', 'quotedTweet', 'inReplyToTweetId', 'inReplyToUser', 'mentionedUsers', 'coordinates', 'place', 'hashtags', 'cashtags']
    
    def searchTwt(self):
        
        list = []

        count = 0
        for tweet in sntwitter.TwitterSearchScraper(self.query).get_items():

            if (count == self.max):
                print('Added '+str(count)+' rows.')
                return pd.DataFrame(data=list, columns=self.columns)
        
            list.append(vars(tweet))
            count += 1
            if (count%500 == 0):
                print('Added '+str(count)+' rows. Still adding...')

        print('Added '+str(count)+' rows.')
        return pd.DataFrame(data=list, columns=self.columns)