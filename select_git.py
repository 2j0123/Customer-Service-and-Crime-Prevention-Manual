import streamlit as st
import atm_git
import kiosk_git

def main():
    # '장소 선택' 사이드바
    st.sidebar.title('장소 선택')
    selected_location = st.sidebar.radio('현재 위치', ['ATM', '키오스크'])

    # 선택한 장소에 따라 매뉴얼 표시
    if selected_location == 'ATM':
        atm_git.main()
    elif selected_location == '키오스크':
        kiosk_git.main()

if __name__ == "__main__":
    main()
