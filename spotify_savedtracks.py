'''
Author: @thiagorodrigues
Descricao: Exporta todas as músicas que constam na sua playlist de músicas favoritadas no Spotify
'''

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import time

def _log(texto):
    print("[{time}] {texto}".format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), texto=texto))

_log('#### Spotify - Saved Tracks #### ')

tempo_inicio = time.time()
client_id = '' # preencha o client_id do seu app
client_secret = '' # preencha o client_secret do seu app
redirect_uri = '' # preencha o redirect_uri do seu app
pasta = 'C:/Users/seu_usuario/Desktop/spotify_saved_tracks.xlsx' # local onde o arquivo será salvo

# Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read"))

# Obtém todas as músicas salvas do usuário
def get_all_saved_tracks():
    saved_tracks = []
    offset = 0
    limit = 50  # Limite máximo de itens por chamada (máximo permitido pela API)
    total = float('inf')  # Inicializa o total com infinito para iniciar o loop

    # Enquanto houver mais músicas para buscar
    while len(saved_tracks) < total:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        total = results['total']  # Atualiza o total de músicas
        offset += len(results['items'])  # Incrementa o offset para a próxima chamada
        for item in results['items']:
            track = item['track']
            album_image_url = next((image['url'] for image in track['album']['images'] if image['height'] == 640), None)
            artistas = ', '.join([artist['name'] for artist in track['artists']])
            saved_tracks.append({
                'id': track['id'],
                'popularity': track['popularity'],
                'album': track['album']['name'],
                'artista': artistas,
                'musica_nome': track['name'],
                'duracao': track['duration_ms'] / 60000,  # Convertendo MS em Minutos
                'external_urls': track['external_urls']['spotify'],
                'preview_song': track['preview_url'],
                'album_release': track['album']['release_date'],
                'album_tracks': track['album']['total_tracks'],
                'album_image': album_image_url,
            })

    return saved_tracks

def export_to_excel(file_path):
    saved_tracks = get_all_saved_tracks()
    df = pd.DataFrame(saved_tracks)
    _log(f'Quantidade de registros {df.shape[0]}')
    df.to_excel(file_path, index=False)
    _log(f'Exportado com sucesso: {file_path}')

if __name__ == "__main__":
    file_path = pasta
    export_to_excel(file_path)

_log(f'Tempo de duracao: {time.time() - tempo_inicio:.0f} sec')
