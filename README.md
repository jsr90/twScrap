# twScrap - scraping tweets using snscrape library

Jesús Sánchez Rodríguez

## Introduction

This python project allows to get a set of tweets in a .csv file, given a statement. In this case, I got tweets from Sevilla and Málaga's 2022 Feria with the purpose of analyse them using NLP and determine which one was the most funny.

## Execution example


```python
#Import class Scrap
from classes.Scrap import Scrap

# Create the query using twitter operators
query_example = "'Data Science' lang:en until:2021-05-3 since:2021-04-25"

# Get dataframe with a maximum of 20 rows
scrap = Scrap(query=query_example, max=20)
df_example = scrap.searchTwt()

# Save dataframe to csv
df_example.to_csv('data/example.csv', index=False)
```

    Added 20 rows.



```python
df_example.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>url</th>
      <th>date</th>
      <th>content</th>
      <th>renderedContent</th>
      <th>id</th>
      <th>user</th>
      <th>replyCount</th>
      <th>retweetCount</th>
      <th>likeCount</th>
      <th>quoteCount</th>
      <th>...</th>
      <th>media</th>
      <th>retweetedTweet</th>
      <th>quotedTweet</th>
      <th>inReplyToTweetId</th>
      <th>inReplyToUser</th>
      <th>mentionedUsers</th>
      <th>coordinates</th>
      <th>place</th>
      <th>hashtags</th>
      <th>cashtags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://twitter.com/Sololearn/status/138900654...</td>
      <td>2021-05-02 23:59:01+00:00</td>
      <td>Data science, machine learning, deep learning,...</td>
      <td>Data science, machine learning, deep learning,...</td>
      <td>1389006544705032199</td>
      <td>https://twitter.com/Sololearn</td>
      <td>0</td>
      <td>10</td>
      <td>6</td>
      <td>0</td>
      <td>...</td>
      <td>[Photo(previewUrl='https://pbs.twimg.com/media...</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>[SoloLearn, ComeCodeWithUs, LearnToCode, datas...</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://twitter.com/Datascience__/status/13890...</td>
      <td>2021-05-02 23:58:29+00:00</td>
      <td>Advances in Financial Machine Learning https:/...</td>
      <td>Advances in Financial Machine Learning amazon....</td>
      <td>1389006412815249408</td>
      <td>https://twitter.com/Datascience__</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>[datascience, ad]</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://twitter.com/Strat_AI/status/1389006341...</td>
      <td>2021-05-02 23:58:12+00:00</td>
      <td>@AI_Miami #Python: 12 Websites to Learn #Codin...</td>
      <td>@AI_Miami #Python: 12 Websites to Learn #Codin...</td>
      <td>1389006341063196677</td>
      <td>https://twitter.com/Strat_AI</td>
      <td>0</td>
      <td>25</td>
      <td>14</td>
      <td>0</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1.389006e+18</td>
      <td>https://twitter.com/HumanCenterAI</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>[Python, Coding, 100DaysOfCode, AI, Analytics,...</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://twitter.com/CoolerData/status/13890063...</td>
      <td>2021-05-02 23:58:04+00:00</td>
      <td>Similarity Encoding for Dirty Categories Using...</td>
      <td>Similarity Encoding for Dirty Categories Using...</td>
      <td>1389006307911364608</td>
      <td>https://twitter.com/CoolerData</td>
      <td>0</td>
      <td>4</td>
      <td>3</td>
      <td>0</td>
      <td>...</td>
      <td>[Photo(previewUrl='https://pbs.twimg.com/media...</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>[GetMoreInsights, CoolerData, Data, Science, D...</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://twitter.com/CoolerData/status/13890063...</td>
      <td>2021-05-02 23:58:03+00:00</td>
      <td>DAG Factories — A better way to Airflow https:...</td>
      <td>DAG Factories — A better way to Airflow dlvr.i...</td>
      <td>1389006302504841217</td>
      <td>https://twitter.com/CoolerData</td>
      <td>0</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>...</td>
      <td>[Photo(previewUrl='https://pbs.twimg.com/media...</td>
      <td>None</td>
      <td>None</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>[GetMoreInsights, CoolerData, Data, Analytics,...</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>



We can see that our dataframe has 27 columns such as the id of the tweet, the date it was created, its link, etc.
