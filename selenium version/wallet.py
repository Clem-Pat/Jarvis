from spotipy.oauth2 import SpotifyOAuth

class Wallet():
    def __init__(self):
        self.client_id =
        self.client_secret =
        self.redirect_uri = 'https://open.spotify.com/'
        self.redirect_uri_encoded = 'https%3A%2F%2Fopen.spotify.com%2F'
        self.client_infos_b64 =
        self.scope = 'user-read-private%20user-read-playback-state%20user-modify-playback-state'

        self.old_code =

        self.get_the_code_request = "https://accounts.spotify.com/authorize?client_id=CLIENT_ID&response_type=code&redirect_uri=https%3A%2F%2Fopen.spotify.com%2F&scope=user-read-private%20user-read-playback-state%20user-modify-playback-state"
        self.get_token = 'curl -H "Authorization: Basic AUTH" -d grant_type=authorization_code -d code= CODE -d redirect_uri=https%3A%2F%2Fopen.spotify.com%2F https://accounts.spotify.com/api/token' #BUT CHANGE THE CODE !!!

        self.token = "BQDinjvU3kQo-V6KSTdtc15OIKQaIbIqjHwPgQNtF62FPWYZdA1hja0XRjfaJkXpURNKjkzzwMm1L-P074_5WGdFZ37MxSj6kGkKJZ30JGtQLCspVlRnEztIO2zEoVLJorYRR6vfm9vP6utnhC1DDEYiG-Xj3-6gLjeeiYRbtw"

        self.auth_manager = SpotifyOAuth(
    	    client_id=self.client_id,
    	    client_secret=self.client_secret,
    	    redirect_uri=self.redirect_uri,
    	    scope="user-read-private user-read-playback-state user-modify-playback-state",
    	    username='Clèm')
