import streamlit as st
import numpy as np
import cv2
from PIL import Image
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

    
    model_path = r"C:\Users\User\Desktop\Code\Github\Final_project\WASSUP_EST_FINAL_Team4\model.pt"
    model = YOLO(model_path)
    # img = cv2.resize(img, (720, int(720 * (9 / 16))))
    
    if torch.cuda.is_available():
      res = model.track(img, conf = 0.5, persist = True, device = 'cuda' )
    else:
      res = model.track(img, conf = 0.5, persist = True)
    
    res_plotted = res[0].plot()
    # id2label = {
    # '0' : 'Anger',
    # '1' : 'Happy',
    # '2' : 'Surprised',
    # '3' : 'Sadness'
    # }
    # yolo 에서 가져온 값들 따로 처리해보기
    # start_point , end_point = np.array_split(res[0].boxes.xyxy.cpu().numpy().tolist()[0],2)
    # score = str(round(res[0].boxes.conf.cpu().numpy().tolist()[0]*100,2))+ '%'
    # label = id2label[str(int(res[0].boxes.cls.cpu().numpy().tolist()[0]))]
    # results_str = label + ':'+ score

    #cv2 로 박스랑 글자 생성
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # blue  = (255, 0, 0)
    # red = (0, 0, 255)

    # processed_img  = cv2.rectangle(img,(int(start_point[0]), int(start_point[1])), (int(end_point[0]), int(end_point[1])), blue, 3)
    # processed_img = cv2.putText(processed_img, results_str, (int(start_point[0]), int(start_point[1])) , font, 2, red, 3, cv2.LINE_AA)
    # processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    return res_plotted
    # return res_plotted, label





run = st.checkbox('Run')
cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])

try:
  while run:
      success, frame = cap.read()
      frame = cv2.resize(frame, (640, 480))

      # img = img_with_text_results(frame, st_frame)
      if success:
        img = img_with_text_results(frame)
        # img, label = img_with_text_results(frame)
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

