#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pip', 'install tweepy datetime')


# In[ ]:


get_ipython().system('python Leitura_tweets.py')


# In[ ]:


import json


# In[ ]:


with open('tweets_coletados.txt','r') as file:
    tweets = file.readlines()


# In[5]:


tweets[0] 


# In[ ]:


json.loads(tweets[0])


# In[ ]:


type (json.loads(tweets[0]))


# In[ ]:


json.loads(
        json.loads(tweets[0])            
)                        


# In[ ]:


with open('tweets.json','w') as out:
  json.dump(
      json.loads(json.loads(tweets[0])), out
  )


# In[ ]:


tratar_tweets = [json.loads( json.loads(i) ) for i in tweets] 


# In[ ]:


len(tratar_tweets)


# In[ ]:


tratar_tweets[0].keys()


# In[ ]:


tratar_tweets[0]["created_at"]


# In[ ]:


tratar_tweets[0]["user"]


# In[ ]:


tratar_tweets[0]["user"]["listed_count"]


# In[ ]:


tratar_tweets[0].items()


# In[ ]:


list(tratar_tweets[0].items())[0]


# In[ ]:


tratar_tweets[5]


# In[ ]:


import pandas as pd


# In[ ]:


##teste = pd.DataFrame(tratar_tweets[0])


# In[ ]:


##teste


# In[ ]:


##teste.columns


# In[ ]:


df = pd.DataFrame(tratar_tweets[0]).reset_index(drop=True).iloc[:1]


# In[ ]:


df


# In[ ]:


df.columns


# In[ ]:


df.drop(columns=['quote_count', 'reply_count', 'retweet_count', 'favorite_count','favorited', 'retweeted',
                 'user','entities','retweeted_status'],inplace=True)


# In[ ]:


df.columns


# In[ ]:


df['user_id'] = tratar_tweets[0]["user"]["id"]
df['user_id_str'] = tratar_tweets[0]["user"]["id_str"]
df['user_screen_name'] = tratar_tweets[0]["user"]["screen_name"]
df['user_location'] = tratar_tweets[0]["user"]["location"]
df['user_description'] = tratar_tweets[0]["user"]["description"]
df['user_protected'] = tratar_tweets[0]["user"]["protected"]
df['user_verified'] = tratar_tweets[0]["user"]["verified"]
df['user_followers_count'] = tratar_tweets[0]["user"]["followers_count"]
df['user_friends_count'] = tratar_tweets[0]["user"]["friends_count"]
df['user_created_at'] = tratar_tweets[0]["user"]["created_at"]



# In[ ]:


df


# In[ ]:


# entities
tratar_tweets[0]["entities"]


# In[ ]:


users_mentions = []
for i in range(len(tratar_tweets[0]["entities"]["user_mentions"])):
  dicionario = tratar_tweets[0]["entities"]["user_mentions"][i].copy()
  dicionario.pop('indices', None)
  df1 = pd.DataFrame(dicionario,index=[0])
  df1 = df1.rename(columns={
        'screen_name': 'entities_screen_name',
        'name': 'entities_name',
        'id': 'entities_id',
        'id_str': 'entities_id_str'
  })
  users_mentions.append(df1)


# In[ ]:


users_mentions


# In[ ]:


###pd.concat(users_mentions,ignore_index=True)


# In[ ]:


df2 = []
for i in users_mentions:
  df2.append(
      pd.concat([df.copy(), i], axis=1)
  )


# In[ ]:


df2[0]


# In[ ]:


pd.concat(df2,ignore_index=True)


# In[ ]:


def tweet_para_df(tweet):
  try:
    df = pd.DataFrame(tweet).reset_index(drop=True).iloc[:1]
    df.drop(columns=['quote_count', 'reply_count', 'retweet_count', 'favorite_count','favorited', 'retweeted',
                  'user','entities','retweeted_status'],inplace=True)
    df['user_id'] = tweet["user"]["id"]
    df['user_id_str'] = tweet["user"]["id_str"]
    df['user_screen_name'] = tweet["user"]["screen_name"]
    df['user_location'] = tweet["user"]["location"]
    df['user_description'] = tweet["user"]["description"]
    df['user_protected'] = tweet["user"]["protected"]
    df['user_verified'] = tweet["user"]["verified"]
    df['user_followers_count'] = tweet["user"]["followers_count"]
    df['user_friends_count'] = tweet["user"]["friends_count"]
    df['user_created_at'] = tweet["user"]["created_at"]  
    users_mentions = []
    for i in range(len(tweet["entities"]["user_mentions"])):
      dicionario = tweet["entities"]["user_mentions"][i].copy()
      dicionario.pop('indices', None)  
      df1 = pd.DataFrame(dicionario,index=[0])
      df1 = df1.rename(columns={
            'screen_name': 'entities_screen_name',
            'name': 'entities_name',
            'id': 'entities_id',
            'id_str': 'entities_id_str'
      })
      users_mentions.append(df1)

    df2 = []
    for i in users_mentions:
      df2.append(
          pd.concat([df.copy(), i], axis=1)
      )
    df_final = pd.concat(df2,ignore_index=True)
  except:
    return None
  return df_final


# In[ ]:


tweet_para_df(tratar_tweets[5])


# In[ ]:


get_ipython().run_cell_magic('time', '', 'tweets_analisados = [tweet_para_df(tweet) for tweet in tratar_tweets]')


# In[ ]:


len(tweets_analisados)


# In[ ]:


tweets_analisados = [i for i in tweets_analisados if i is not None]


# In[ ]:


len(tweets_analisados)


# In[ ]:


tratados = pd.concat(tweets_analisados,ignore_index=True)


# In[ ]:


tratados

