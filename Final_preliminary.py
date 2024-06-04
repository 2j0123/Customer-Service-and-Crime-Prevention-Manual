import streamlit as st
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
import torch
from ultralytics import YOLO
import time
import os
import config
from select_git import run_select
from utils import vid_with_label_1stg, vid_with_label_2stage

def stream_display(response, placeholder):        # 응답을 스트리밍하여 텍스트를 실시간으로 업데이트 (응답객체, 텍스트 표시할 위치)
    text = ''
    for chunk in response:
        if parts := chunk.parts:
            if parts_text := parts[0].text:
                text += parts_text
                placeholder.write(text + "▌")
    return text

def init_messages() -> None:                # init_message 함수로 리스트 초기
    st.session_state.messages = []

def undo() -> None:                        # undo 함수로 리스트의 마지막 메시지 제거
    st.session_state.messages.pop()

def set_generate(state=True):                # 기본값을 True로 설정
    st.session_state.generate = state

    st.title("💬 Emotion detector")        # Streamlit 제목과 캡션
    st.caption("🚀 A streamlit emotion detector by custom model")

# confidence = float(st.sidebar.slider(
#     "Select Model Confidence", 25, 40, 60, 80, 100 )) / 100
confidence = 0.5

def main():
    set_generate()      # generate 호출해서 타이틀 & 캡션 설정, Run 체크박스 추가
    run = st.checkbox('Run')
    cap = cv2.VideoCapture(0)    # 카메라 초기화
    FRAME_WINDOW = st.image([])    # 이미지 프레임을 표시할 위치

    start_time = None
    emotion_detected = None

    try:
        while run:
            success, frame = cap.read()
            frame = cv2.resize(frame, (640, 480))
            
            if success:    # 모델별로 적절한 함수 호출 -> 이미지 & 레이블 할당
                img, label = vid_with_label_1stg(frame, confidence)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                FRAME_WINDOW.image(img)

                # Happy가 아닌 경우가 1초 이상 감지되면 감정을 화면에 표시 & 카메라 종료 / 그렇지않을경우 감정 초기화
                if label and label != 'Happy':        
                    if emotion_detected is None:
                        emotion_detected = label
                        start_time = time.time()
                    elif emotion_detected == label and time.time() - start_time >= 1:
                        st.write(f"{label} detected for 1 s")
                        run = False
                        os.system("streamlit run select_git.py")
                        break
                else:
                    emotion_detected = None
                    start_time = None    

            else:        #프레임을 읽지 못한경우 카메라 해제 & 루프 종료
                cap.release()
                break

        else:
            st.write('Stopped')

    except Exception as e:        # 예외 발생시 에러 메시지 표시
        st.error(f"Error loading video: {str(e)}")

# script가 직접 실행될 때 main 함수 호출
if __name__ == "__main__":
    main()
