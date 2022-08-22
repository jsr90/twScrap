from classes.Scrap import Scrap

# Create queries with hastags, language, dates of ferias and excluiding retweets
query_mlg = "(#FeriaDeMalaga OR #FeriaMalaga OR #FeriaMLG OR 'Feria de Malaga') lang:es until:2022-08-21 since:2022-08-13 -filter:retweets"
query_svq = "(#FeriaDeSevilla OR #FeriaSevilla OR #FeriaDeAbril OR 'Feria de Sevilla' OR 'Feria de Abril') lang:es until:2022-05-08 since:2022-05-01 -filter:retweets"

# Get dataframes
scrap = Scrap(query=query_mlg, max=10000)
df_mlg = scrap.searchTwt()

scrap = Scrap(query=query_svq, max=10000)
df_svq = scrap.searchTwt()

# Save dataframes to csv
df_svq.to_csv('data/tweets_svq.csv', index=False)
df_mlg.to_csv('data/tweets_mlg.csv', index=False)