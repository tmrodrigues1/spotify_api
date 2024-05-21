"""
Author: @thiagorodrigues
Descrição:
1) O script faz a leitura de um arquivo excel de todos os IDs de músicas do Spotify
2) Depois traz todas as features das musicas, como (acousticness, danceability, energy, instrumentalness)
"""


import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import time
from decouple import config

def _log(texto):
    print("[{time}] {texto}".format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), texto=texto))

_log('#### Spotify - Audio Features ####')

tempo_inicio = time.time()
client_id = '' # preencha o client_id do seu app
client_secret = '' # preencha o client_secret do seu app
redirect_uri = '' # preencha o redirect_uri do seu app
path_saved_tracks = 'C:/Users/THIAGORODRIGUES/Desktop/spotify_savedtracks.xlsx' # arquivo gerado pelo script savedtracks
path_audio_features = 'C:/Users/THIAGORODRIGUES/Desktop/audio_features.xlsx' # local onde será salvo o audio_features

# Inicialize o objeto de autenticação do Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=""))

# Função para ler os IDs do arquivo Excel
def read_ids_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df['id'].tolist()

# Função para fazer a requisição ao endpoint de audio-features do Spotify
def get_audio_features_batch(track_ids):
    try:
        audio_features = sp.audio_features(track_ids)
        if audio_features:
            return audio_features
        else:
            _log(f"Não foi possível obter dados para as músicas com IDs: {track_ids}")
            return None
    except spotipy.SpotifyException as e:
        if e.http_status == 429:  # Verifica se o erro é 429 - que é quando atinge o limite da API
            _log(f'Rate limit atingido. Aguardando {time.sleep(5)} segundos...')
            return get_audio_features_batch(track_ids)  # Tenta novamente a solicitação
        else:
            _log(f"Erro ao obter audio features para as faixas com IDs {track_ids}: {e}")
            return None

def main(file_path):
    ids = read_ids_from_excel(file_path)
    
    # Divide os IDs em lotes de até 100 IDs para respeitar o limite da API
    batches = [ids[i:i+100] for i in range(0, len(ids), 100)]
    
    audio_features_list = []

    # Faz a requisição para cada lote
    for batch_num, batch_ids in enumerate(batches, start=1):
        _log(f'Processando lote {batch_num}/{len(batches)}...')
        audio_features_batch = get_audio_features_batch(batch_ids)
        if audio_features_batch:
            audio_features_list.extend(audio_features_batch)
    
    df = pd.DataFrame(audio_features_list)
    _log(f'Quantidade de registros {df.shape[0]}')
    df.to_excel(path_audio_features, index=False)
    _log("Features de áudio salvas em 'audio_features.xlsx'")

if __name__ == "__main__":
    file_path = path_saved_tracks
    main(file_path)
