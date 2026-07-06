import streamlit as st                      # streamlit 모듈(pip install streamlit)

with st.container(border=True):
    st.subheader('📝 현재 페이지 : webPage1.py')

    if st.button('🔸페이지 이동하기 [st.switch_page(...) 사용] -> webPage2.py'):
        st.switch_page('pages/webPage2.py')
