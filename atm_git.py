import streamlit as st
import os
import config_test

def set_step(step):
    st.session_state.step = step

def select_scam(scam_number):
    st.session_state.selected_scam = scam_number
    set_step(2)

# 초기 화면
def display_initial_options():
    st.warning('현재 불안한 상태로 확인됩니다.')
    st.subheader('누군가가 금전을 요구하고 있나요?')

    col1, col2 = st.columns(2)
    with col1:
        st.button('예', on_click=set_step, args=(1,), key='initial_yes')
    with col2:
        st.button('아니오', on_click=set_step, args=(4,), key='initial_no')

# 금전 요구 상황 확인
def display_money_demand_question():
    st.write('이 중에 연관된 상황이 있나요?')

    col3, col4, col5 = st.columns(3)
    with col3:
        if st.button('선택', key='scam1_select'):
            select_scam(1)
        st.image(os.path.join(config_test.IMG_FOLDER, 'family_scam.jpg'), use_column_width=True)
        st.write('예시 1', unsafe_allow_html=True)
        if 'selected_scam' in st.session_state and st.session_state.selected_scam == 1:
            st.write('✔️', unsafe_allow_html=True)
    with col4:
        if st.button('선택', key='scam2_select'):
            select_scam(2)
        st.image(os.path.join(config_test.IMG_FOLDER, 'government_scam.jpg'), use_column_width=True)
        st.write('예시 2', unsafe_allow_html=True)
        if 'selected_scam' in st.session_state and st.session_state.selected_scam == 2:
            st.write('✔️', unsafe_allow_html=True)
    with col5:
        if st.button('선택', key='scam3_select'):
            select_scam(3)
        st.image(os.path.join(config_test.IMG_FOLDER, 'app_scam.jpg'), use_column_width=True)
        st.write('예시 3', unsafe_allow_html=True)
        if 'selected_scam' in st.session_state and st.session_state.selected_scam == 3:
            st.write('✔️', unsafe_allow_html=True)

    st.button('해당 사항 없음', on_click=set_step, args=(4,), key='no_related_situation')

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)  # Spacing

    col_reset = st.columns([1])
    with col_reset[0]:
        st.button('초기화면', on_click=set_step, args=(0,), key='reset_from_money_demand')

# 112 신고 및 범죄 대응 매뉴얼
def display_crime_options():
    st.write('아래 항목 중 한 가지를 선택해주세요.')

    col5, col6, col7 = st.columns(3)
    with col5:
        if st.button('112 연결', key='112_connect'):
            st.markdown('<a href="tel:112" style="font-size:20px;">112 연결</a>', unsafe_allow_html=True)
    with col6:
        if st.button('보이스피싱 대응 매뉴얼', key='scam_manual'):
            st.image(os.path.join(config_test.IMG_FOLDER, 'voice1.png'))
            st.image(os.path.join(config_test.IMG_FOLDER, 'voice2.png'))
    with col7:
        if st.button('사이버 범죄 도움 사이트', key='cyber_crime_help'):
            st.markdown('<a href="https://ecrm.police.go.kr/minwon/main" style="font-size:20px;">사이버 범죄 도움 사이트</a>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)  # Spacing

    col_prev, col_reset = st.columns([1, 1])
    with col_prev:
        st.button('이전', on_click=set_step, args=(1,), key='prev_from_crime')
    with col_reset:
        st.button('초기화면', on_click=set_step, args=(0,), key='reset_from_crime')

# 도움이 필요한 상황인지 확인
def display_help_question():
    st.write('도움이 필요한 상황인가요?')

    col7, col8 = st.columns(2)
    with col7:
        st.button('필요', on_click=set_step, args=(3,), key='help_needed')
    with col8:
        st.button('불필요', on_click=set_step, args=(5,), key='help_not_needed')

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)  # Spacing

    col_reset = st.columns([1])
    with col_reset[0]:
        st.button('초기화면', on_click=set_step, args=(0,), key='reset_from_help')

# 금융 업무 관련 매뉴얼
def display_finance_options():
    st.subheader('금융 업무 도움 시스템')
    st.write('금융 관련 업무를 도와드리겠습니다.')
    st.write('필요하신 매뉴얼을 선택해주세요.')

    col9, col10, col11, col12, col13, col14 = st.columns([2, 2, 2, 2, 2, 2])
    with col9:
        if st.button('현금입금', key='cash_deposit'):
            st.image(os.path.join(config_test.IMG_FOLDER, 'deposit.png')) 
    with col10:
        if st.button('현금출금', key='cash_withdrawal'):
            st.image(os.path.join(config_test.IMG_FOLDER, 'withdrawal.png'))
    with col11:
        if st.button('계좌송금', key='account_transfer'):
            st.image(os.path.join(config_test.IMG_FOLDER, 'remittance.png')) 
    with col12:
        if st.button('거래조회', key='transaction_inquiry'):
            st.image(os.path.join(config_test.IMG_FOLDER, 'transactional_information.png'))
    with col13:
        if st.button('통장정리', key='update_bankbook'):
            st.image(os.path.join(config_test.IMG_FOLDER, 'update_bankbook.png')) 
    with col14:
        if st.button('상담연결', key='consultation_connect'):
            st.markdown('<a href="tel:1234" style="font-size:20px;">상담원 연결</a>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)  # Spacing

    col_prev, col_reset = st.columns([1, 1])
    with col_prev:
        st.button('이전', on_click=set_step, args=(4,), key='prev_from_finance')
    with col_reset:
        st.button('초기화면', on_click=set_step, args=(0,), key='reset_from_finance')

# 안전한 상황
def display_safe_message():
    st.info('''안전한 상황으로 판단하였습니다.  
               시스템을 종료하셔도 됩니다.''')

def main():
    st.markdown(
        "<h1> <span style='color:red'>위험</span> 감지 시스템</h1>",
        unsafe_allow_html=True
    )
    
    # 상태 초기화
    if 'step' not in st.session_state:
        st.session_state.step = 0

    if st.session_state.step == 0:
        display_initial_options()
    elif st.session_state.step == 1:
        display_money_demand_question()
    elif st.session_state.step == 2:
        display_crime_options()
    elif st.session_state.step == 3:
        display_finance_options()  
    elif st.session_state.step == 4:
        display_help_question()
    elif st.session_state.step == 5:
        display_safe_message()
    
    
    # 스타일 적용
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #add8e6;
            color: black;
            font-size: 16px;
            width: 100%;
            margin: 10px 0;
        }
        .stButton>button:hover {
            background-color: #87cefa;
        }
        .stImage {
            width: 100%;
        }
        .stButton {
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()