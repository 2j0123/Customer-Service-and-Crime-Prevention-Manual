import streamlit as st
import numpy as np
import streamlit as st
import cv2
# # from tools import tools, handle_function_call
from PIL import Image, ImageFont, ImageDraw
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


def img_with_text_results(img, st_frame):

    
    model_path = r"C:\Users\User\Desktop\Code\Github\Final_project\WASSUP_EST_FINAL_Team4\model.pt"
    model = YOLO(model_path)
    # img = cv2.resize(img, (720, int(720 * (9 / 16))))
    
    res = model.track(img, conf = 0.5, persist = True)

    # res = model.predict(img, 0.5)
    res_plotted = res[0].plot()
    # st_frame.image(res_plotted,
    #               caption='Detected Video',
    #               channels="BGR",
    #               use_column_width=True
    #               )
    
    return res_plotted






    # results = model.predict(img, save=False, imgsz=320, conf=0.5)
    
    # for result in results:
    #    boxes = result.boxes
    #    keypoints = results.keypoints
    #    probs = result.probs
    
    # 폰트 색상 지정
    # blue = (255, 0, 0)


    # # 폰트 지정
    # font = cv2.FONT_HERSHEY_PLAIN
    # # 이미지에 글자 합성하기
    # img = cv2.putText(img, results, (30, 40), font, 2, blue, 1, cv2.LINE_AA)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # return img
    # return results


run = st.checkbox('Run')
cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])

try:
  while run:
      success, frame = cap.read()
      st_frame = st.empty()

      # img = img_with_text_results(frame, st_frame)
      if success:
        img = img_with_text_results(frame, st_frame)
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

