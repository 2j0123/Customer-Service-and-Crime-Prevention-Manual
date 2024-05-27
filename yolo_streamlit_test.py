import streamlit as st
import numpy as np
import streamlit as st
import cv2 
# # from tools import tools, handle_function_call
from PIL import Image, ImageFont, ImageDraw
from transformers import pipeline
import tensorflow as tf
import torch


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
    
    model_path = r"C:\Users\User\Desktop\Code\Github\Final_project\WASSUP_EST_FINAL_Team4\best_yolov8_model.pt"
    model = torch.load(model_path)
    # model = tf.keras.models.load(r"C:\Users\User\Desktop\Code\Github\Final_project\WASSUP_EST_FINAL_Team4\model.h5")
    #결과

    results = model.predict(img, save=False, imgsz=320, conf=0.5)

    for result in results:
       boxes = result.boxes
       keypoints = results.keypoints
       probs = result.probs
    
    # 폰트 색상 지정
    blue = (255, 0, 0)


    # 폰트 지정
    font = cv2.FONT_HERSHEY_PLAIN
    # 이미지에 글자 합성하기
    img = cv2.putText(img, result, (30, 40), font, 2, blue, 1, cv2.LINE_AA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    return img, result


run = st.checkbox('Run')
cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])
panic_counter = 0

while run:
    ret, frame = cap.read()
    img, label = img_with_text_results(frame)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(img)

    if label == 'panic':
       panic_counter += 1
    else:
       panic_counter == 0
    
    if panic_counter >= 50:
       panic_counter == 0
       st.write("피싱 스캠을 당하고 계신가요?")
       
    else:
       pass

else:
    st.write('Stopped')

