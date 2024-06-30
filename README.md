
### TEAM
  + 최재형 : 프로젝트 매니저(팀장) + 개발 
  + 이진영 : 프로젝트 관리자(데이터, 코드 관리자) + 개발
  + 최한솔 : 프로젝트 서기(회의 안건, 주요 내용 기록) + 개발
  + 황승욱 : 프로젝트 자료 전담자(프로젝트 관련 자료 조사 및 공유) + 개발
  + 모든 인원이 모든 과정에 참여합니다. 담당 업무는 명목상 정했습니다.

![감정 따뜻쟁이 (1)](https://github.com/2j0123/WASSUP_EST_FINAL_Team4/assets/91775854/e2aa64fc-017b-4ddf-b2b7-ca5c46f99080)

# PROJECT  
## TITLE
감정 분석을 통한 고객 응대 및 범죄 예방 메뉴얼 제시

## INTRODUCTION
ATM or KIOSK 이용 시 사용자 얼굴을 인식합니다. <br>
Anger, Panic, Sadness의 감정이 5초 이상 지속될 시 사용자 응답에 따른 대응 메뉴얼을 제공합니다. <br>
Data Preprocessing :`Data Augmentation`, `YOLOv8`, `Swin` <br>
1stage model : `YOLO` <br>
2stage model : `YOLO` + `SwinV2` <br>
* 2stage process
  - YOLO : Object Detection + Bounding Box
  - SwinV2 : Emotion Classification

`Streamlit`을 이용한 GUI 구현

![img](https://github.com/2j0123/WASSUP_EST_FINAL_Team4/assets/63550106/15103646-00a6-4248-970e-61e733d7f2bb)
![img2](https://github.com/2j0123/WASSUP_EST_FINAL_Team4/assets/63550106/0604bf21-ce4d-4d68-ad56-2ce6e2ef3968)
![img3](https://github.com/2j0123/WASSUP_EST_FINAL_Team4/assets/63550106/2d56a139-f5f6-44b4-acf2-ea0896633eb4)
![img4](https://github.com/2j0123/WASSUP_EST_FINAL_Team4/assets/63550106/3a423d46-9d3e-48fe-822b-22ce512dc8ef)

## DATA
* ESTsoft 제공
   - Anger, Happy, Panic, Sadness 4가지 감정의 이미지 데이터
   - 각 감정의 json 파일
   - Segmentation Data
* AI HUB에서 데이터 확보
   - Neutral Emotion 추가

## INSTALLATION
```bash
# Clone repository
git clone https://github.com/2j0123/WASSUP_EST_FINAL_Team4.git
```

```bash
# Install packages
pip install ultralytics
pip install streamlit
pip install cv2
pip install tensorflow
pip install torch
pip install transformers
```

```bash
# Run
streamlit run Final.py
```

## PROJECT TIMELINE
https://docs.google.com/spreadsheets/d/10FW3OlBUKH2F5dS39VDBljzR9_W99PY1/edit#gid=395812352
