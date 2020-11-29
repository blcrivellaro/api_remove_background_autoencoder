import re
import cv2 as cv
import numpy as np
from datetime import datetime
from flask import Flask, request

from tensorflow.keras.models import load_model

from functions.mysql_database import create_table, insert_data
from functions.image_processing import string2RGB, RGB2string, process_img

# Criacao da tabela no banco de dados - Database ImagensApi
table_name = 'Imagens'
create_table(table_name)

app = Flask(__name__)
@app.route('/remove_background', methods=['POST']) 
def remove_background():
      data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      message = {'codigo_retorno': '', 'mensagem':'', 'imgb64_clean': ''}

      # Analise requisicao
      try:
           request_json = request.get_json()
      except:
           message['codigo_retorno'] = 1
           message['mensagem'] = "Erro na requisição"
           return message
      try:
           key = 'imgb64_dirty'
           imgb64_dirty = request_json.get(key)
           img_dirty = string2RGB(re.sub(r"data:image/png;base64,", "", imgb64_dirty))
      except:
           if imgb64_dirty == None:
                message['codigo_retorno'] = 2
                message['mensagem'] = "Chave {} não encontrada".format(key)
                return message
           else:
                message['codigo_retorno'] = 3
                message['mensagem'] = "Problema na string base 64 referente a chave {}".format(key)
                return message

      # Caracteristicas imagem de entrada e processamento da mesma
      heigth, width, channel = img_dirty.shape
      img_dirty = process_img(img_dirty)
      
      # Aplicacao do modelo treinado
      model = load_model('./model')
      img_dirty = np.asarray([img_dirty])
      img_clean = model.predict(img_dirty)
      img_clean = cv.resize(img_clean[0]*255, (width, heigth))
      imgb64_clean = "data:image/png;base64,{}".format(re.sub(r"b\'|\'", "", str(RGB2string(img_clean))))

      # Retorno requisicao
      message['codigo_retorno'] = 0
      message['mensagem'] = "Imagem processada com sucesso"
      message['imgb64_clean'] = imgb64_clean

      # Insercao de dados na tabela Imagens: data/hora, imgb64_dirty, imgb64_clean
      insert_data(table_name, data_hora, imgb64_dirty, imgb64_clean)

      return message

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=3030)


