import streamlit as st
import numpy as np
import cv2
from PIL import Image
import time
import os
# 사용자 정의 모듈
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

def init_messages() -> None:                # init_message 함수로 리스트 초기화
    st.session_state.messages = []

def undo() -> None:                        # undo 함수로 리스트의 마지막 메시지 제거
    st.session_state.messages.pop()

def set_generate(state=True):                # 기본값을 True로 설정
    st.session_state.generate = state

st.title("💬 Emotion detector")            # Streamlit 제목과 캡션
st.caption("🚀 A streamlit emotion detector by custom model")

# confidence = float(st.sidebar.slider(
#     "Select Model Confidence", 25, 40, 60, 80, 100 )) / 100

confidence = float(st.sidebar.slider("Select Model Confidence", 25, 100, 40)) / 100        # 사이드 바에 모델 신뢰도 & 모델 선택 메뉴
model_selection = st.sidebar.selectbox("Select Model", ["Model 1 (1stg)", "Model 2 (5emo_1stg)", "Model 3 (2stg)", "Model 4 (5emo_2stg)"])

def main():            #camera_active키가 sesstion_state 값에 없으면 True로 설정
    if 'camera_active' not in st.session_state:
        st.session_state.camera_active = True
        
    set_generate()  # generate 호출해서 타이틀 & 캡션 설정, Run 체크박스 추가
    run = st.checkbox('Run')
    cap = cv2.VideoCapture(0)    # 카메라 초기화
    FRAME_WINDOW = st.image([])    # 이미지 프레임을 표시할 위치

    start_time = None
    emotion_detected = None
    dark_warning = st.empty()  # 화면이 어두울 경우 경고 메시지 표시할 자리

    last_frame = None

    try:
        while run and st.session_state.get("camera_active", True):        # Run 선택된 경우 camera_active가 True인 동안 실행
            success, frame = cap.read()
            frame = cv2.resize(frame, (640, 480))
            
            if success:                                                # 프레임을 last_frame에 저장 & GrayScale로 변환 -> 밝기 계산
                last_frame = frame.copy()
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #GrayScale 
                brightness = np.mean(gray_frame)
                
                if brightness < 30:  # 밝기 30 미만이면 경고 메시지 표시
                    dark_warning.warning("너무 어둡습니다. 화면이 가려진건 아닌지 확인해주세요.")
                    continue
                else:
                    dark_warning.empty()

                # 모델별로 적절한 함수 호출 -> 이미지 & 레이블 할당
                if model_selection == "Model 1 (1stg)":
                    img, label = vid_with_label_1stg(frame, confidence, config.YOLO_CUSTOM)
                elif model_selection == "Model 2 (5emo_1stg)" :
                    img, label = vid_with_label_1stg(frame, confidence, config.YOLO_5EMO)
                elif model_selection == "Model 3 (2stg)" :
                    img, label = vid_with_label_2stage(frame, confidence, config.SWINV2)
                elif model_selection == "Model 4 (5emo_2stg)" :
                    img, label = vid_with_label_2stage(frame, confidence, config.SWINV2_5EMO)

                # 감지된 이미지를 RGB로 변환하여 화면에 표시
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                FRAME_WINDOW.image(img)

                # Happy가 아닌 경우가 1초 이상 감지되면 감정을 화면에 표시 & 카메라 종료 / 그렇지않을경우 감정 초기화
                if label and label != 'Happy':
                    if emotion_detected is None:
                        emotion_detected = label
                        start_time = time.time()
                    elif emotion_detected == label and time.time() - start_time >= 1:
                        st.write(f"{label} detected for 1 s")
                        st.session_state.camera_active = False
                        break
                else:
                    emotion_detected = None
                    start_time = None    
            else:                #프레임을 읽지 못한경우 카메라 해제 & 루프 종료
                cap.release()
                break

        # 마지막 프레임이 있으면 RGB로 변환하여 화면에 표시
        if last_frame is not None:
            last_frame_rgb = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(last_frame_rgb)

        cap.release()        # 카메라를 해제하고 감지된 감정을 화면에 표시 -> run_select 함수 호출
        
        st.write(f'Detected emotion: {emotion_detected}')
        run_select()

    except Exception as e:        # 예외 발생시 에러 메시지 표시
        st.error(f"Error loading video: {str(e)}")

# script가 직접 실행될 때 main 함수 호출
if __name__ == "__main__":
    main()
