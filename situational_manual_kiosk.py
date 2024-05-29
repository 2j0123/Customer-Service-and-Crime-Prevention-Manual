import streamlit as st

def set_step(step):
    st.session_state.step = step

# 초기 화면 (도움 제시) # 0
def display_initial_options():
    st.warning('현재 불안한 상태로 확인됩니다.')
    st.subheader('도움이 필요하신가요?')

    col_yes, col_no = st.columns(2)
    with col_yes:
        st.button('네', on_click=set_step, args=(1,), key='yes')
    with col_no:
        if st.button('아니오'):
            st.info('안전한 상황으로 판단하였습니다.  \n시스템을 종료하셔도 됩니다.')

# 필요한 매뉴얼 제시 # 1
def display_manual():
    st.write('필요하신 버튼을 터치해주세요.')

    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button('주문방법', key='order'):
            st.session_state.manual_selection = 'order'
        if st.button('결제방법', key='payment'):
            st.session_state.manual_selection = 'payment'
        if st.button('직원호출', key='call'):
            st.session_state.manual_selection = 'call'
    
    with col2:
        if 'manual_selection' in st.session_state:
            if st.session_state.manual_selection == 'order':
                st.image(r'C:\Users\USER\Pictures\Screenshots\order1.png', caption='매장/포장 여부 선택', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\order2.png', caption='원하는 메뉴 선택', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\order3.png', caption='옵션이 있다면 원하는 옵션 선택한 후 선택 완료 클릭', use_column_width=True)
            elif st.session_state.manual_selection == 'payment':
                st.image(r'C:\Users\USER\Pictures\Screenshots\payment.png', caption='메뉴 선택 완료 후 결제 버튼 클릭', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\payment1.png', caption='1. 카드 결제 시 카드 결제 선택', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\payment2.png', caption='카드 투입구에 카드 삽입', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\payment3.png', caption='2. 간편 결제 시 간편 결제 선택', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\payment4.png', caption='QR코드/바코드 스캔', use_column_width=True)
                st.image(r'C:\Users\USER\Pictures\Screenshots\payment5.png', caption='주문 완료 확인 및 영수증 출력', use_column_width=True)
            elif st.session_state.manual_selection == 'call':
                st.markdown('[직원 호출](tel:1234)') # 매장 전화번호 or 벨 울리기 등

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)  # Spacing
    st.button('초기화면', on_click=set_step, args=(0,), key='reset')

def main():
    st.markdown("<h1 style='font-family:Verdana; color:#EBEBEB;'>도움용 안내창</h1>", unsafe_allow_html=True)
    
    # 상태 초기화
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.manual_selection = None

    if st.session_state.step == 0:
        display_initial_options()
    elif st.session_state.step == 1:
        display_manual()

# 스타일 적용
st.markdown("""
    <style>
    .stButton>button {
        background-color: #BFECB4;
        color: black;
        font-size: 18px;
        width: 100%;
        height: 50px;
        margin: 10px 0;
    }
    .stButton>button:hover {
        background-color: #83BA82;
    }
    .stImage {
        display: inline-block;
        margin-right: 10px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()