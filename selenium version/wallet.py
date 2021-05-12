from spotipy.oauth2 import SpotifyOAuth

class Wallet():
    def __init__(self):
        self.client_id = 'b5f9ebb9c59a44cca61aa8d874d94c30'
        self.client_secret = '743aeccd74cb43428f25ca49fca31c79'
        self.redirect_uri = 'https://open.spotify.com/'
        self.redirect_uri_encoded = 'https%3A%2F%2Fopen.spotify.com%2F'
        self.client_infos_b64 = "YjVmOWViYjljNTlhNDRjY2E2MWFhOGQ4NzRkOTRjMzA6NzQzYWVjY2Q3NGNiNDM0MjhmMjVjYTQ5ZmNhMzFjNzk="
        self.scope = 'user-read-private%20user-read-playback-state%20user-modify-playback-state'

        self.old_code = "AQBEbHmbkJeFTr5Ubo-F5yeZDgZFQ4NjM8-XhLIS2NffHjMNQvwwfsTaI_yvwyFWcbVp1Ta3BkOuVtESCPBWEFAOo2PsTrydPHAOgSvFfYJD1X70VfWS2Sp9Rn86s_K9xEh3tFpyAR70mE2Skd7zvpstMjBmTgbrmWCkYSWkXb7qpzILOttmGEcJ7rNFm6kZIdOkL1HWe_1kmD7lqKcuFSB3l4irRFE1G8j-yt_560TQKM_M0NycMrtucDmYsVrKj17DrGjQ"

        self.get_the_code_request = "https://accounts.spotify.com/authorize?client_id=b5f9ebb9c59a44cca61aa8d874d94c30&response_type=code&redirect_uri=https%3A%2F%2Fopen.spotify.com%2F&scope=user-read-private%20user-read-playback-state%20user-modify-playback-state"
        self.get_token = 'curl -H "Authorization: Basic YjVmOWViYjljNTlhNDRjY2E2MWFhOGQ4NzRkOTRjMzA6NzQzYWVjY2Q3NGNiNDM0MjhmMjVjYTQ5ZmNhMzFjNzk=" -d grant_type=authorization_code -d code=AQBZKvJzLoN4YL0e0v9NPKwZdhAYPAeqhUh3AUPh1B7Ycvk-ZdeT0o_vSfSXo9BC40ABTy1gSzyK4gr8geVjMVRdDRGw0bQUyAQpAB3qKAzMbDAsqV7pXEFr83Oc5zG-oUJsSbAZcLx1FSrZBiw9fd71b_6nMsx8fJaiELD6M_jycyWlOAgyQp2h0aIFxQXFrQQ32_shTuyd14O45hM6UpVp8slioFeQ9Q3_Rye3dzrZ6RCxCYo-f0PNs2tbf45luXpYnI6e -d redirect_uri=https%3A%2F%2Fopen.spotify.com%2F https://accounts.spotify.com/api/token' #BUT CHANGE THE CODE !!!
        self.old_token = "BQCVSa9OYYVBPcWO4GQL8CGs7s2TObSboun35APzM6T0UU2wW2OEjarNCk-EyzMtliKBRJ48dOp_gmyPXXnbREn2Ct_hQVtJqwAvP2rTn2mLXDIMym14w0Ca_Io0Uu6TEFifRzIhROR0eI1DQ4mr9ZrBr72UGLYzRW5coO2mOw"

        self.token = "BQDinjvU3kQo-V6KSTdtc15OIKQaIbIqjHwPgQNtF62FPWYZdA1hja0XRjfaJkXpURNKjkzzwMm1L-P074_5WGdFZ37MxSj6kGkKJZ30JGtQLCspVlRnEztIO2zEoVLJorYRR6vfm9vP6utnhC1DDEYiG-Xj3-6gLjeeiYRbtw"

        self.auth_manager = SpotifyOAuth(
    	    client_id=self.client_id,
    	    client_secret=self.client_secret,
    	    redirect_uri=self.redirect_uri,
    	    scope="user-read-private user-read-playback-state user-modify-playback-state",
    	    username='Clèm')
