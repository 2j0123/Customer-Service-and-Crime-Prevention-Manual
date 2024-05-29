import streamlit as st
import situational_manual_atm
import situational_manual_kiosk

def main():
    # '장소 선택' 사이드바
    st.sidebar.title('장소 선택')
    selected_location = st.sidebar.radio('현재 위치', ['ATM', '키오스크'])

    # 선택한 장소에 따라 매뉴얼 표시
    if selected_location == 'ATM':
        situational_manual_atm.main()
    elif selected_location == '키오스크':
        situational_manual_kiosk.main()

if __name__ == "__main__":
    main()