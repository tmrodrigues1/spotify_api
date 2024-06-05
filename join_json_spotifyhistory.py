import os
import json
import pandas as pd
from datetime import datetime
import time

def _log(texto):
    print("[{time}] {texto}".format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), texto=texto))

_log('#### Spotify - Juntando Arquivos ####')
tempo_inicio = time.time()

def read_json_files_from_folder(folder_path):
    # Lista para armazenar todos os dados dos arquivos JSON
    all_data = []

    # Verifica todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        # Verifica se o arquivo contem o texto "Streaming" e sua extensao é json
        if filename.startswith('Streaming_') and filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Adiciona os dados lidos à lista geral
                all_data.extend(data)
    
    return all_data

def save_data_to_excel(data, output_file):
    df = pd.DataFrame(data)
    _log(f'Quantidade de registros: {df.shape[0]}')
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    folder_path = 'C:/Users/seu_usuario/Desktop/' # pasta onde estao os arquivos json
    output_file = 'C:/Users/seu_usuario/Desktop/spotifyhistory_combined.xlsx' # pasta onde os arquivo sera salvo
    all_data = read_json_files_from_folder(folder_path)
    save_data_to_excel(all_data, output_file)

    _log(f'Tempo de duracao: {time.time() - tempo_inicio:.0f} sec')
