import json
from platform import python_branch

import tweepy
from datetime import datetime

#-- Chaves Api Twitter --#
consumer_key = " "
consumer_secret = " "

access_token = " "
access_token_secret = " "


#-- Define arquivo de saida para armazenar os tweets coletados --#
hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collect_tweets_{hoje}.txt", "w")

#-- Conexão com Twitter --#
class MyListener(tweepy.Stream): 

    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True
    
    def o_error(self, status):
        print(status)


twitter_stream = MyListener(
    consumer_key, consumer_secret,
    access_token, access_token_secret
    
)

#-- Define palavra chave para busca dos tweets --#
twitter_stream.filter(track=['lula'])
