import streamlit as st
import numpy as np
import streamlit as st
import cv2 
# # from tools import tools, handle_function_call
from PIL import Image
from transformers import pipeline


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
    pretrain_path = r'C:\Users\User\Desktop\Code\Github\Final_project\swinv2-tiny-patch4-window8-256-finetuned-eurosat\checkpoint-2516'
    pipe = pipeline("image-classification", pretrain_path)
    
    kr_to_en = { '분노'    : 'anger',
                 '기쁨'    : 'happy',
                 '당황'    : 'panic',
                 '슬픔'    : 'sadness'             
                 }
    
    
    #결과
    results = next(iter(pipe(Image.fromarray(img))))
    results_str = kr_to_en[results['label']] + ": " + str(round(results['score']*100, 2)) + '%'
    
    
    # 폰트 색상 지정
    blue = (255, 0, 0)


    # 폰트 지정
    font = cv2.FONT_HERSHEY_PLAIN
    # 이미지에 글자 합성하기
    img = cv2.putText(img, results_str, (30, 40), font, 2, blue, 1, cv2.LINE_AA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    return img, kr_to_en[results['label']]


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

