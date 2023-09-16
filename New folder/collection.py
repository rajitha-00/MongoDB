from pymongo import MongoClient
import pandas as pd

client = MongoClient('localhost', 27017)

data = pd.read_csv('./ne.csv')

artist_album_info = data[['Artist', 'Track', 'Album', 'Album_type','most_playedon','EnergyLiveness']]
audio_features = data[['Danceability','Energy','Loudness','Speechiness','Acousticness','Instrumentalness','Liveness','Valence','Tempo','Duration_min']]
platform_metrics = data [['Title','Channel','Views','Likes','Comments','Licensed','official_video','Stream','most_playedon']]


db = client['SpotifyMongo']

# Create and populate the Artist & Album Information collection
artist_album_collection = db['artist_album_info']
artist_album_collection.insert_many(artist_album_info.to_dict('records'))

# Create and populate the Audio Features collection
audio_features_collection = db['audio_features']
audio_features_collection.insert_many(audio_features.to_dict('records'))

# Create and populate the platform Metrics collection
platform_metrics_collection = db['platform_metrics']
platform_metrics_collection.insert_many(platform_metrics.to_dict('records'))
