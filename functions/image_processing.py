import io
import base64
import cv2 as cv
import numpy as np
from PIL import Image

# Conversao base64 para imagem
def string2RGB(base64_string):
     imgdata = base64.b64decode(str(base64_string))
     img = Image.open(io.BytesIO(imgdata))
     return cv.cvtColor(np.array(img), cv.COLOR_BGR2RGB)   

# Conversao imagem para base64
def RGB2string(img):
     is_success, im_buf_arr = cv.imencode(".png", img)
     io_buf = io.BytesIO(im_buf_arr)
     byte_im = io_buf.getvalue()
     string = base64.b64encode(byte_im)
     return string

# Processamento imagem
def process_img(img):
     img = cv.resize(cv.cvtColor(img, cv.COLOR_BGR2GRAY), (540, 420))
     img = np.reshape(np.asarray(img/255.0, dtype="float32"), (420, 540, 1))
     return img