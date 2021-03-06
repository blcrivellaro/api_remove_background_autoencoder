# api_remove_background_autoencoder

API para remoção de background de imagens com ruídos utilizando autoencoder.

### <b> 1. Descrição API </b>  

A API recebe uma imagem codificada em base 64 por meio de um JSON com a chave imgb64_dirty, e:

<ol>
<li> Remove o background da imagem utilizando autoencoder; </li>
<li> Salva a data e hora da requisição, juntamente com as strings base 64 da imagem original e da imagem processada em um banco de dados MySQL; </li>
<li> Retorna a string base 64 da imagem após remoção do background por meio de um JSON com a chave imgb64_clean. </li>
</ol>

### <b> 2. Requisição HTTP </b>  

```yaml
POST  
Host: http://localhost:3030  
Rota: /remove_background  
```

### <b> 3. JSON de entrada </b>  
```yaml
{
"imgb64_dirty": string base64
}
```

### <b> 4. JSON de saída </b>  

```yaml
{
"codigo_retorno": int,    
"mensagem": string,     
"imgb64_clean": string base64
}
```
### <b> 5. Descrição status da requisição </b>  

As chaves codigo_retorno e mensagem do JSON de saída representam o status da requisição:

codigo_retorno | mensagem                                                  | descrição
:-------------:|:----------------------------------------------------------|:----------
0              | Imagem processada com sucesso                             | Processamento da imagem realizado com sucesso e retorno da imagem após remoção do background
1              | Erro na requisição                                        | Requisição realizada de forma errada 
2              | Chave imgb64_dirty não encontrada                         | JSON não possui a chave imgb64_dirty
3              | Problema na string base 64 referente a chave imgb64_dirty | String base64 referente a chave imgb64_dirty está corrompida

### <b> 6. Instalações necessárias </b>

```yaml
pip install -r requirements.txt
```

### <b> 7. Execução da API </b>

Para execução da API pode-se utilizar o server do Flask (recomendado somente para ambientes de desenvolvimento):

```yaml
python api_remove_background.py
```
Para ambientes de produção pode-se utilizar um server WSGI, como Gunicorn, Gevent ou uWSGI. Exemplo de execução com Gunicorn:

```yaml
gunicorn -b 0.0.0.0:3030 api_remove_background:app
```
### <b> 8. Treinamento do modelo autoencoder </b>

O modelo autoencoder foi treinado utilizando o Google Colab, conforme modelo_autoencoder.ipynb.

<b> 8.1 Exemplos de imagens utilizadas no treinamento do modelo autoencoder </b>

![exemplos_imagens_treinamento](https://user-images.githubusercontent.com/56976250/100552468-21335f80-3266-11eb-90f6-7ac1af676aee.png)


<b> 8.2 Evolução do erro médio do quadrático em relação as épocas </b>

![loss_mse_treinamento](https://user-images.githubusercontent.com/56976250/100552469-21cbf600-3266-11eb-8689-b333ace22792.png)


<b> 8.3 Teste do modelo autoencoder para remoção de background </b>

![exemplos_imagens_teste](https://user-images.githubusercontent.com/56976250/100552467-20023280-3266-11eb-9d82-bdfae650770e.png)

