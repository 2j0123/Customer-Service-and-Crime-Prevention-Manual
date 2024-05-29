import streamlit as st
import numpy as np
import cv2
from PIL import Image
from transformers import pipeline
import tensorflow as tf
import torch
from ultralytics import YOLO
import config_test



def vid_with_label_2stage(img):

    
    yolo_path = "models/yolo_face_detection"
    model = YOLO(yolo_path)
    
    if torch.cuda.is_available():
      res = model.track(img, conf = 0.5, persist = True, device = 'cuda' )
    else:
      res = model.track(img, conf = 0.5, persist = True)

    if res is not None:
      try:
        # yolo 에서 가져온 값들 따로 처리해보기
        start_point , end_point = np.array_split(res[0].boxes.xyxy.cpu().numpy().tolist()[0],2)
        # 이미지를 슬라이스 하기
        roi = img[int(start_point[1]):int(end_point[1]), int(start_point[0]):int(end_point[0])]

        # swin 모델 불러오기
        swin_path = config_test.SWINV2
        pipe = pipeline("image-classification", swin_path)

        kr_to_en = { '분노'    : 'anger',
                    '기쁨'    : 'happy',
                    '당황'    : 'panic',
                    '슬픔'    : 'sadness'             
                    }
        
        
        #결과
        results = next(iter(pipe(Image.fromarray(roi))))
        results_str = kr_to_en[results['label']] + ": " + str(round(results['score']*100, 2)) + '%'

        #cv2 로 박스랑 글자 생성
        font = cv2.FONT_HERSHEY_SIMPLEX
        blue  = (255, 0, 0)
        red = (0, 0, 255)

        cv2.rectangle(img, (int(start_point[0]), int(start_point[1])), 
                  (int(end_point[0]), int(end_point[1])), blue, 3)

        cv2.putText(img, results_str, (int(start_point[0]), int(start_point[1])) , font, 1, red, 3, cv2.LINE_AA)
        # cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        return img, kr_to_en[results['label']]
      except Exception as e :
         return img, None
    else:
      return img, None
    

def vid_with_label_1stg(img):

    
    model_path = "models\yolo_custom_model.pt"
    model = YOLO(model_path)
    # img = cv2.resize(img, (720, int(720 * (9 / 16))))
    
    if torch.cuda.is_available():
      res = model.track(img, conf = 0.5, persist = True, device = 'cuda' )
    else:
      res = model.track(img, conf = 0.5, persist = True)
    
    res_plotted = res[0].plot()
    id2label = {
    '0' : 'Anger',
    '1' : 'Happy',
    '2' : 'Panic',
    '3' : 'Sadness'
    }
    # yolo 에서 가져온 값들 따로 처리해보기
    try:
        # start_point , end_point = np.array_split(res[0].boxes.xyxy.cpu().numpy().tolist()[0],2)
        # score = str(round(res[0].boxes.conf.cpu().numpy().tolist()[0]*100,2))+ '%'
   
        label = id2label[str(int(res[0].boxes.cls.cpu().numpy().tolist()[0]))]
        return res_plotted, label
        # results_str = label + ':'+ score
    except Exception as e:
       return res_plotted, None
    #cv2 로 박스랑 글자 생성
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # blue  = (255, 0, 0)
    # red = (0, 0, 255)

    # processed_img  = cv2.rectangle(img,(int(start_point[0]), int(start_point[1])), (int(end_point[0]), int(end_point[1])), blue, 3)
    # processed_img = cv2.putText(processed_img, results_str, (int(start_point[0]), int(start_point[1])) , font, 2, red, 3, cv2.LINE_AA)
    # processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    # return res_plotted
    