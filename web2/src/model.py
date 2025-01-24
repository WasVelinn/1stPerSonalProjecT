import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 현 폴더의 절대경로

model = load_model(os.path.join(BASE_DIR,'../model/model.h5'))

model.predict()