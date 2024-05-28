import streamlit as st
import numpy as np
import cv2
from PIL import Image
from transformers import pipeline
import tensorflow as tf
import torch
from ultralytics import YOLO


def stream_display(response, placeholder):
  text=''
  for chunk in response:
    if parts:=chunk.parts:
      if parts_text:=parts[0].text:
        text += parts_text
        placeholder.write(text + "▌")
  return text

def init_messages() -> None:
  st.session_state.messages = []

def undo() -> None:
  st.session_state.messages.pop()

def set_generate(state=True):
  st.session_state.generate = state

  st.title("💬 Emotion detector")
st.caption("🚀 A streamlit emotion detector by custom model")


def img_with_text_results(img):

    
    yolo_path = r"C:\Users\User\Desktop\Code\Github\Final_project\WASSUP_EST_FINAL_Team4\person_model.pt"
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
        swin_path = r'C:\Users\User\Desktop\Code\Github\Final_project\swinv2-tiny-patch4-window8-256-finetuned-eurosat\checkpoint-2516'
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
    
    





run = st.checkbox('Run')
cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])

try:
  while run:
      success, frame = cap.read()
      

      # img = img_with_text_results(frame, st_frame)
      if success:
        img, label = img_with_text_results(frame)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = img_with_text_results(frame)
        FRAME_WINDOW.image(img)

      else:
        cap.release()
        break

  else:
      st.write('Stopped')
except Exception as e:
        st.error(f"Error loading video: {str(e)}")

