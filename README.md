# Introdução
Este repositório reúne scripts que criei para extrair informações das minhas músicas favoritas do Spotify. Os dados extraídos são salvos em arquivos CSV, facilitando a criação de Dashboards e análises mais apuradas.
Existem várias formas de conseguir esses dados, mas a opção escolhida foi através da utilização da biblioteca <a href="https://spotipy.readthedocs.io/en/">Spotipy</a>

# Spotify WEB API
Fiz um tutorial resumido e simples baseado na documentação oficial da API do Spotify.

1) Necessário ter uma conta Free ou Premium do Spotify
2) Fazer login na área de <a href="https://www.google.com/](https://developer.spotify.com/dashboard">Spotify for Developer</a>
4) Criar um app
5) Acesse seu app e salve seu "client_id", "client_secret" e "Redirect URIs"
6) Agora você está pronto!

# Utilização dos Scripts
Por padrão, todos os scripts precisarão ser preenchidos com as credenciais obtidas em seu app.
Conforme exemplo abaixo:

```
client_id: huashas9877as7798fsa77987
client_secret: h1295a877as7798fsa77987
Redirect URIs http://127.0.0.1:9090
```

### > Script: Saved Tracks (Músicas Favoritadas)
O escopo (scope) utilizado da API é o ```user-library-read``` e o retorno será um arquivo com todas as músicas que estão listadas como favoritas em sua conta.

#### Response esperado:
```python
[2024-05-21 16:37:38] #### Spotify - Saved Tracks #### 
[2024-05-21 16:38:45] Quantidade de registros 4634
[2024-05-21 16:38:48] Exportado com sucesso: C:/Users/THIAGORODRIGUES/Desktop/spotify_lista_teste.xlsx
[2024-05-21 16:38:48] Tempo de duracao: 70 sec
```

### > Script: Audio Features (Detalhamento das músicas)
Para executar esse script é necessário que o arquivo gerado pelo Saved Tracks tenha sido gerado. O escopo (scope) utilizado da API é o ```audio_features``` e o retorno será um arquivo com as características de cada música, por exemplo: se ela é mais instrumental, acústica e por aí vai. Se estiver curioso para entender melhor acesse <a href="https://developer.spotify.com/documentation/web-api/reference/get-audio-features">Audio Features</a>  

#### Response esperado:
```python
[2024-05-21 16:53:33] #### Spotify - Audio Features ####
[2024-05-21 16:53:35] Processando lote 1/10...
[2024-05-21 16:53:36] Processando lote 2/10...
[2024-05-21 16:53:36] Processando lote 3/10...
[2024-05-21 16:53:37] Processando lote 4/10...
[2024-05-21 16:53:37] Processando lote 5/10...
[2024-05-21 16:53:38] Processando lote 6/10...
[2024-05-21 16:53:38] Processando lote 7/10...
[2024-05-21 16:53:39] Processando lote 8/10...
[2024-05-21 16:53:39] Processando lote 9/10...
[2024-05-21 16:53:39] Processando lote 10/10...
[2024-05-21 16:53:56] Quantidade de registros 4634
[2024-05-21 16:53:59] Features de áudio salvas em 'audio_features.xlsx'
```
### > Script: Histórico (Juntando Arquivos)
Por conta das limitações da API do Spotify não é possível coletar os seus histórico de músicas reproduziadas. Nesse caso se faz necessário solicitar seus dados na plataforma, o que pode levar de 2-5 dias para estar pronta para download. 
Clique no link para saber mais <a href="https://www.spotify.com/account/privacy/?_ga=2.120424716.566690053.1717614374-1133634410.1680754123">Download Dados Spotify</a>. 
Você receberá um e-mail informando que os arquivos estão prontos para download e quando você o fizer, irá reparar em diversos arquivos no formato JSON.
O script nesse repositírio é feito para juntar todos eles e convertê-los em .xlsx para facilitar a manipulação.

# Dúvidas
Compilado de principais dúvidas
- O que é e quais são os Scopes - https://developer.spotify.com/documentation/web-api/concepts/scopes
- Limitações da API - https://developer.spotify.com/documentation/web-api/concepts/rate-limits
- Status Code - https://developer.spotify.com/documentation/web-api/concepts/api-calls
<br>
