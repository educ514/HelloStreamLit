# ##################################################################################################
# frmMain.py - Streamlit 웹 폼 모듈
# ##################################################################################################
# ══════════════════════════════════════════════════════════════════════════════════════════
# 외부모듈 영역
# ══════════════════════════════════════════════════════════════════════════════════════════
import sys                                  # system 모듈(Built-In)
import os                                   # os 모듈(Built-In)
import time                                 # time 모듈(Built-In)
import datetime                             # datetime 모듈(Built-in)
import traceback                            # datetime 모듈(Built-in)

import numpy as np                          # Numpy 모듈(pip install numpy)
# import pandas as pd                         # Pandas 모듈(pip install pandas)

import streamlit as st                      # streamlit 모듈(pip install streamlit)

# import Css                                  # CSS 모듈(User)
import webMainMgr                           # webMainMgr 모듈(User)
# ══════════════════════════════════════════════════════════════════════════════════════════
# 사용자정의 클래스 영역
# ------------------------------------------------------------------------------------------
# Form              - Streamlit 웹 폼 클래스
# Inheritance       - None
# ══════════════════════════════════════════════════════════════════════════════════════════
class Form():
    # ======================================================================================
    # 전역상수 관리 - 필수영역(정적변수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # Const         - 전역상수 클래스 설명
    # Inheritance   - None
    # ——————————————————————————————————————————————————————————————————————————————
    class Const():
        CONST_NAME = 0                      # 전역상수 선언 예
    # ======================================================================================
    # 전역클래스 관리 - 필수영역(사용자정의 보조클래스)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # SubClassName  - 보조 클래스 설명
    # Inheritance   - None
    # ——————————————————————————————————————————————————————————————————————————————
    class SubClassName():
        pass                                # 사용자정의 클래스 선언 예
    # ======================================================================================
    # 전역변수 관리 - 필수영역(정적변수)
    # ======================================================================================
    HelloNum = 0                            # 전역변수 선언 예

    TabButtonNum = None                     # 탭 만들기-버튼 번호 선언
                                            # st.session_state.TabButtonNum 와 동일 효과
                                            # 단 디버깅시 모듈 리로드 부분 삭제 필요
    # ======================================================================================
    # 세션변수 관리 - 필수영역(정적변수)
    # ======================================================================================
    # 정적변수 영역에서 세션변수를 선언하면 모듈 로드시 한번만 실행되기 때문에
    # 웹 브라우저에서 F5(Refresh) 하는 경우 세션변수가 생성되지 않고 로직으로 흘러
    # 변수 없음 오류가 발생 할 가능성이 있음
    # --------------------------------------------------------------
    # 이런 경우 생성자를 활용해서 세션변수를 생성하는 것을 추천!
    # --------------------------------------------------------------
    # st.session_state.Hello = None               # 세션 변수 선언 예

    # st.session_state.TabButtonNum       = None  # 탭 만들기 버튼 번호 세션 변수 선언
    # st.session_state.GugudanTopMenu     = None  # 구구단 상단 메뉴 선택 세션 변수 선언
    # st.session_state.GugudanBottomMenu  = None  # 구구단 하단 메뉴 선택 세션 변수 선언
    # st.session_state.GugudanData        = None  # 구구단 데이터 세션 변수 선언
    # st.session_state.GugudanUploaderKey = 0     # 구구단 Uploader Key값 저장 세션 변수 선언
    # ======================================================================================
    # 생성자 관리 - 필수영역(인스턴스함수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # __init__  - 생성자(인스턴스변수 생성/초기화)
    # Args      - self : 객체 인스턴스
    # Return    - None
    # ——————————————————————————————————————————————————————————————————————————————
    def __init__(self) -> None:
        try:
            # --------------------------------------------------------------
            # 모듈 수정 후 디버깅시 반경될 수 있도록 재로드(임시)
            # --------------------------------------------------------------
            import importlib                        # importlib 모듈(Built-in)
            importlib.reload(webMainMgr)
            # ==============================================================================
            # 전역변수 관리 - 필수영역(인스턴스변수)
            # ==============================================================================
            self.Hello = None                       # 전역변수 선언 예

            self.Knnc   = webMainMgr.Knnc()         # k-최근접이웃분류(k-Nearest Neighbors Classification) 모델 객체 생성
            # ======================================================================================
            # 세션변수 관리 - 필수영역(세션변수)
            # ======================================================================================
            # 인스턴스 영역에서 세션변수를 선언하게 되면
            # st.form_submit_button 클릭 시 마다 화면 갱신(rerun)이 발생하고
            # Form 객체 생성이 호출 되면 세션변수가 매번 초기화 됨
            # --------------------------------------------------------------
            # 이런 경우 매번 초기화 방지를 위해 아래 코드 필요!
            # if 'hello' not in st.session_state: 처럼
            #    st.session_state.hello = None
            # --------------------------------------------------------------
            if 'Hello' not in st.session_state:
                st.session_state.Hello = None               # 세션 변수 선언 예

            if 'TabButtonNum' not in st.session_state:
                st.session_state.TabButtonNum = None        # 탭 만들기 버튼 번호 세션 변수 선언
            if 'GugudanTopMenu' not in st.session_state:
                st.session_state.GugudanTopMenu = None      # 구구단 상단 메뉴 선택 세션 변수 선언
            if 'GugudanBottomMenu' not in st.session_state:
                st.session_state.GugudanBottomMenu = None   # 구구단 하단 메뉴 선택 세션 변수 선언
            if 'GugudanData' not in st.session_state:
                st.session_state.GugudanData = None         # 구구단 데이터 세션 변수 선언
            if 'GugudanUploaderKey' not in st.session_state:
                st.session_state.GugudanUploaderKey = 0     # 구구단 Uploader Key값 저장 세션 변수 선언
            # ==============================================================================
            # 부모객체 생성 - 필수영역(상속을 받은 경우 필수)
            # ==============================================================================
            # super().__init__()                      # 부모 클래스가 하나인 경우 부모 객체 생성
            # Parent1.__init__(self)                  # 부모 클래스가 두개 이상인 경우 부모 객체 생성
            # Parent2.__init__(self)                  # 부모 클래스가 두개 이상인 경우 부모 객체 생성
            # ==============================================================================
        except Exception as Ex:
            print(traceback.format_exc())                   # 예외 출력하기(예외처리)
    # ======================================================================================
    # 전역함수 관리 - 필수영역(정적함수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # Hello1    - 정적함수 선언 예
    # Args      - None
    # Return    - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def Hello1() -> None:
        try:
            pass
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ======================================================================================
    # 전역함수 관리 - 필수영역(인스턴스함수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # ExpPrintString    - 문자열 출력 Expander
    # Args              - self : 객체 인스턴스
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    def ExpPrintString(self):
        try:
            # --------------------------------------------------------------
            # 타이틀 출력
            # --------------------------------------------------------------
            st.title('⭐ Hello StreamLit')
            # --------------------------------------------------------------
            with st.expander('🔹문자열 출력', key='expPrintString', expanded=False):
                # --------------------------------------------------------------
                # 설명 출력
                # --------------------------------------------------------------
                st.subheader('👉 st.title(...), st.header(...), st.subheader(...)')
                st.subheader('👉 st.write(...), st.text(...)')
                # --------------------------------------------------------------
                st.divider()                # st.write('<hr>', unsafe_allow_html=True)
                # --------------------------------------------------------------
                st.title('1. st.title → 큰 제목')
                st.header('2. st.header → 중간 제목')
                st.subheader('3. st.subheader → 작은 제목')
                st.write('4. st.write → 텍스트, 데이터프레임, 그래프 등 출력 가능')
                st.text('5. st.text → 텍스트')
                # --------------------------------------------------------------
                st.divider()
                # --------------------------------------------------------------
                st.page_link('pages/webPage1.py', label='🔸페이지 이동하기 [st.page_link(...) 사용] -> webPage1.py')
                # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # IncHelloNum   - HelloNum 값 증가
    # Args          - self : 객체 인스턴스
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    def IncHelloNum(self):
        try:
            Form.HelloNum = Form.HelloNum + 1
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ExpInputText  - 문자열 입력 Expander
    # Args          - self : 객체 인스턴스
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    def ExpInputText(self):
        try:
            with st.expander('🔹문자열 입력', key='expInputText', expanded=False):
                with st.form(key='form1', border=True):
                    # --------------------------------------------------------------
                    # 설명 출력
                    # --------------------------------------------------------------
                    st.subheader('👉 st.text_input(...)')
                    st.divider()
                    # --------------------------------------------------------------
                    sHello = st.text_input('Hello:', placeholder='hello StreamLit...')

                    bSubmit = st.form_submit_button('Submit', on_click=self.IncHelloNum)

                    if sHello:
                        st.write(f'입력내용:**&nbsp;<span style="color:cyan">{sHello}, Form.HelloNum={Form.HelloNum}</span>**', unsafe_allow_html=True)
                    else:
                        st.write('입력내용:&nbsp;<span style="color:gray; font-weight:bold;">내용없음</span>', unsafe_allow_html=True)
                    # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ExpInputTextNum   - 문자열/숫자 입력 Expander
    # Args              - self : 객체 인스턴스
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    def ExpInputTextNum(self):
        oCol    = []                        # 화면 디자인용 컬럼 리스트

        try:
            with st.expander('🔹문자열/숫자 입력', key='expInputTextNum', expanded=False):
                with st.form(key='form2', border=True):
                    # --------------------------------------------------------------
                    # 설명 출력
                    # --------------------------------------------------------------
                    st.subheader('👉 st.text_input(...), st.number_input(...)')
                    st.divider()
                    # --------------------------------------------------------------
                    oCol = st.columns(2)

                    with oCol[0]:
                        name = st.text_input('이름을 입력하세요:', placeholder='이름')

                    with oCol[1]:
                        age = st.number_input('나이를 입력하세요:', min_value=14, max_value=16)

                    if name and age:
                        st.write(f'입력내용:*&nbsp;<span style="color:yellow">Hello, {name}의 나이는 {age}입니다.</span>*', unsafe_allow_html=True)
                    else:
                        st.write('입력내용:&nbsp;<span style="color:gray; font-weight:bold;">내용없음</span>', unsafe_allow_html=True)

                    bSubmit = st.form_submit_button('Submit')
                    # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ExpMakeTabs   - 탭 만들기 Expander
    # Args          - self : 객체 인스턴스
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    def ExpMakeTabs(self):
        oTabs   = []                        # 화면 디자인용 탭 리스트

        try:
            with st.expander('🔹탭 만들기', key='expMakeTabs', expanded=False):
                with st.container(key='form3'):
                    with st.form(key='form3', border=True):
                        # --------------------------------------------------------------
                        # 설명 출력
                        # --------------------------------------------------------------
                        st.subheader('👉 st.tabs(...)')
                        st.divider()
                        # --------------------------------------------------------------
                        # 탭 만들기
                        # --------------------------------------------------------------
                        with st.container(key='contTabMain'):
                            oTabs = st.tabs(['탭-1', '탭-2', '탭-3'])

                            with oTabs[0]:
                                with st.container(key='contTab-1'):
                                    st.write('탭-1 영역 내용')

                                    st.form_submit_button('버튼-1', key='button1')

                                    if st.session_state.button1:
                                        st.session_state.TabButtonNum = '[버튼-1] 클릭 됨...'

                            with oTabs[1]:
                                with st.container(key='contTab-2'):
                                    st.write('탭-2 영역 내용')

                                    st.form_submit_button('버튼-2', key='button2')

                                    if st.session_state.button2:
                                        st.session_state.TabButtonNum = '[버튼-2] 클릭 됨...'

                            with oTabs[2]:
                                with st.container(key='contTab-3'):
                                    st.write('탭-3 영역 내용')

                                    st.form_submit_button('버튼-3', key='button3')

                                    if st.session_state.button3:
                                        st.session_state.TabButtonNum = '[버튼-3] 클릭 됨...'
                        # --------------------------------------------------------------
                        st.divider()
                        # --------------------------------------------------------------
                        # 탭 기능 처리
                        # --------------------------------------------------------------
                        with st.container(key='contTabCommon'):
                            # 다른 폼이 갱신되어도 현재 값을 다시 출력하도록
                            # 아래에서 공통으로 출력시킴
                            if st.session_state.TabButtonNum:
                                st.write(st.session_state.TabButtonNum)
                        # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ExpGugudan    - 구구단 Expander
    # Args          - self : 객체 인스턴스
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    def ExpGugudan(self):
        oColTop    = []         # 화면 디자인용 상단 컬럼 리스트
        oColBottom = []         # 화면 디자인용 하단 컬럼 리스트

        oUploadedFile = None    # 구구단 파일 읽기용 객체
        sGugudanData  = None    # 구구단 파일 데이터

        try:
            with st.expander('🔹고급 구구단', key='expGugudan', expanded=False):
                with st.form(key='frmGugudan', border=True):
                    # --------------------------------------------------------------
                    # 구구단 상단 메뉴 출력
                    # --------------------------------------------------------------
                    oColTop = st.columns(6, vertical_alignment='center')

                    with oColTop[0]:
                        nStart = st.number_input('시작단:', value=2, min_value=2, max_value=10000, key='Start')
                    with oColTop[1]:
                        nEnd = st.number_input('끝단:', value=9, min_value=2, max_value=10000, key='End')
                    with oColTop[2]:
                        nDanCount = st.number_input('출력단수:', value=4, min_value=1, max_value=100, key='DanCount')
                    with oColTop[3]:
                        if st.form_submit_button('🔢 구구단 출력 (Slow)', width='stretch'):
                            st.session_state.GugudanTopMenu = 'GugudanPrintSlow'
                    with oColTop[4]:
                        if st.form_submit_button('🔢 구구단 출력 (Fast)', width='stretch'):
                            st.session_state.GugudanTopMenu = 'GugudanPrintFast'
                    with oColTop[5]:
                        if st.form_submit_button('🗑️ 화면 지우기 (Clear)', width='stretch'):
                            st.session_state.GugudanTopMenu = 'GugudanClear'
                # --------------------------------------------------------------
                # 구구단 상단 메뉴 확인 및 기능 처리
                # --------------------------------------------------------------
                with st.container(key='contGugudanTopScroll'):
                    # 다른 쪽 폼이 갱신되어도 현재 구구단 데이터를 다시 출력하도록 아래에서 공통으로 출력시킴
                    if st.session_state.GugudanTopMenu == 'GugudanPrintSlow':
                        self.GugudanPrint(nStart, nEnd, nDanCount, False)
                    elif st.session_state.GugudanTopMenu == 'GugudanPrintFast':
                        self.GugudanPrint(nStart, nEnd, nDanCount, True)
                    elif st.session_state.GugudanTopMenu == 'GugudanClear':
                        st.session_state.GugudanData = None
                # --------------------------------------------------------------
                # st.divider()
                # --------------------------------------------------------------
                # 구구단 하단 메뉴 출력
                # --------------------------------------------------------------
                with st.container(border=True):
                    oColBottom = st.columns(2, vertical_alignment='center')

                    with oColBottom[0]:
                        # --------------------------------------------------------------
                        # st.file_uploader 키값을 매번 바꾸기 위해
                        # 한번 업로드하면 매번 자동으로 클릭 효과 되는것을 방지
                        # sGugudanUploaderKey = f'GugudanUploader{st.session_state.GugudanUploaderKey}'
                        # oUploadedFile = st.file_uploader('📂 구구단 파일열기:', key=sGugudanUploaderKey, type=['txt'])
                        # --------------------------------------------------------------

                        oUploadedFile = st.file_uploader('📂 구구단 파일열기:', type=['txt'])

                        if oUploadedFile:
                            if oUploadedFile.name.endswith('.txt'):
                                st.session_state.GugudanBottomMenu = 'GugudanRead'

                                st.session_state.GugudanUploaderKey = st.session_state.GugudanUploaderKey + 1
                    with oColBottom[1]:
                        if st.download_button(label     = '💾 구구단 파일저장',
                                            data      = str(st.session_state.GugudanData),  # 저장할 실제 데이터(문자열)
                                            file_name = 'gugudan_result.txt',               # 기본 파일 이름 지정
                                            mime      = 'text/plain',                       # 파일 형식 종류
                                            disabled  = not bool(st.session_state.GugudanData)):
                            st.session_state.GugudanBottomMenu = 'GugudanSave'
                # --------------------------------------------------------------
                # 고급 구구단 하단 메뉴 확인 및 기능 처리
                # --------------------------------------------------------------
                # 다른 폼이 갱신되어도 현재 고급 구구단 데이터를 다시 출력하도록
                # 아래에서 공통으로 출력시킴
                with st.container(key='contGugudanBottomScroll'):
                    if st.session_state.GugudanBottomMenu == 'GugudanRead':
                        with st.container(key='contGugudanPrintFile'):
                            if oUploadedFile:
                                sGugudanData = oUploadedFile.read().decode('utf-8')

                                st.text(sGugudanData)
                    elif st.session_state.GugudanBottomMenu == 'GugudanSave':
                        st.write(f'저장 또는 다른이름으로 저장하세요...!')
            # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # GugudanPrint  - 고급 구구단 출력
    # Args          - self : 객체 인스턴스
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    def GugudanPrint(self, Start:int, End:int, DanCount:int, FastSpeed:bool=True):
        nEndMaxLength   = 0     # 고급 구구단 끝값의 최대 길이
        nCalcMaxLength  = 0     # 고급 구구단 결과값 최대 길이
        nTitleMaxLength = 0     # 고급 구구단 타이틀 최대 길이

        sHeader = None          # 고급 구구단 헤더
        sFooter = None          # 고급 구구단 헤더

        oGugudan = []           # 고급 구구단 결과 저장 리스트
        sGugudan = None         # 고급 구구단 결과 저장 문자열

        try:
            # 고급 구구단 최대값 구하기
            nEndMaxLength   = len(str(End))
            nCalcMaxLength  = len(str(End*9))
            nTitleMaxLength = ((1 + nEndMaxLength + 7 + nCalcMaxLength + 3) * DanCount) - 2

            # 고급 구구단 머리말/꼬리말 만들기
            sHeader = '[GUGUDAN : {0} ~ {1}, {2}]'.format(Start, End, DanCount)
            sFooter = '[END]'

            # 고급 구구단 머리말 저장
            oGugudan.append('{0}{1}'.format('-'*nTitleMaxLength, '\n'))
            oGugudan.append('{0}{1}'.format('_'*int((nTitleMaxLength-len(sHeader))/2), sHeader))
            oGugudan.append('{0}{1}{2}'.format('\n', '-'*nTitleMaxLength, '\n'))

            # 고급 구구단 생성
            for dc in range(0, End-Start+1, DanCount):
                for num in range(1, 10):
                    for dan in range(Start, Start+DanCount):
                        if dan+dc <= End:
                            oGugudan.append('_{0:_>{3}} x {1} = {2:_>{4}}___'.format(dan+dc, num,
                                                                                    (dan+dc)*num,
                                                                                    nEndMaxLength,
                                                                                    nCalcMaxLength))
                    oGugudan.append('{0}'.format('\n'))

                if dc < End-Start+1-DanCount:
                    oGugudan.append('{0}'.format('\n'))

            # 고급 구구단 꼬리말 저장
            oGugudan.append('{0}{1}'.format('-'*nTitleMaxLength, '\n'))
            oGugudan.append('{0}{1}'.format('_'*int((nTitleMaxLength-len(sFooter))/2), sFooter))
            oGugudan.append('{0}{1}{2}'.format('\n', '-'*nTitleMaxLength, '\n'))

            # 고급 구구단 화면 출력
            if FastSpeed == False:
                with st.container(key='contGugudanPrintSlow'):
                    # sHtmlFontStart = '<span style="font-family: Consolas">'
                    # sHtmlFontEnd   = '</span>'

                    # \n -> <br>, _ -> &nbsp;
                    sGugudan = ''.join(oGugudan).replace('_', '&nbsp;').replace('\n', '<br>')

                    # st.write(f'{sHtmlFontStart}{sGugudan}{sHtmlFontEnd}', unsafe_allow_html=True)
                    st.write(f'{sGugudan}', unsafe_allow_html=True)
            else:
                with st.container(key='contGugudanPrintFast'):
                    # _ -> space;
                    sGugudan = ''.join(oGugudan).replace('_', ' ')

                    st.text(f'{sGugudan}')

            # 구구단 데이터 세션 변수에 저장
            st.session_state.GugudanData = ''.join(oGugudan).replace('_', ' ')
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ExpInputText  - k-최근접이웃분류(k-Nearest Neighbors Classification)
    # Args          - self : 객체 인스턴스
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    def ExpKnnc(self):
        bDisabled = None

        try:
            with st.expander('🔹k-최근접이웃분류(k-Nearest Neighbors Classification)', key='expKnnc', expanded=False):
                with st.form(key='frmKnnc', border=True):
                    # --------------------------------------------------------------
                    # k-최근접이웃분류(k-Nearest Neighbors Classification)
                    # --------------------------------------------------------------
                    st.subheader('👉 도미/빙어 데이터를 k-최근접이웃분류 모델로 학습하고 New-Fish 예측하기')
                    st.divider()

                    oCol = st.columns(3)

                    with oCol[0]:
                        nNeighbors = st.number_input('n_neighbors(5):', value=5 , min_value=1, max_value=100)

                    with oCol[1]:
                        nNewLength = st.number_input('New-Fish Length:', value=25 , min_value=10, max_value=100)

                    with oCol[2]:
                        nNewWeight = st.number_input('New-Fish Weight:', value=150 , min_value=10, max_value=1000)

                    st.divider()
                    # --------------------------------------------------------------
                    st.subheader('🔸[1] 데이터수집(준비)')

                    if st.form_submit_button('데이터수집(준비)', width='stretch'):
                        with st.container(key='contDataCollect'):
                            self.Knnc.DataCollect()

                    st.divider()
                    # --------------------------------------------------------------
                    st.subheader('🔸[2] 데이터탐색(분석)')

                    bDisabled = True
                    if st.session_state.fish_length_data and st.session_state.fish_weight_data:
                        bDisabled = False

                    if st.form_submit_button('데이터탐색(분석)', disabled=bDisabled, width='stretch'):
                        with st.container(key='contDataAnalyze'):
                            self.Knnc.DataAnalyze(nNewLength, nNewWeight)

                    st.divider()
                    # --------------------------------------------------------------
                    st.subheader('🔸[3] 데이터가공(전처리/검증)')

                    bDisabled = True
                    if st.session_state.fish_length_data and st.session_state.fish_weight_data:
                        bDisabled = False

                    if st.form_submit_button('데이터가공(전처리/검증)', disabled=bDisabled, width='stretch'):
                        with st.container(key='contDataPreProcess'):
                            self.Knnc.DataPreProcess(nNewLength, nNewWeight)

                    st.divider()
                    # --------------------------------------------------------------
                    st.subheader('🔸[4] 데이터학습(모델링/학습)')

                    bDisabled = True
                    if type(st.session_state.train_scaled) == np.ndarray and type(st.session_state.train_target) == np.ndarray:
                        if st.session_state.train_scaled.size and st.session_state.train_target.size:
                            bDisabled = False

                    if st.form_submit_button('데이터학습(모델링/학습)', disabled=bDisabled, width='stretch'):
                        with st.container(key='contDataTrain'):
                            self.Knnc.DataTrain(nNeighbors)

                    st.divider()
                    # --------------------------------------------------------------
                    st.subheader('🔸[5] 모델링평가(검증/예측)')

                    bDisabled = True
                    if type(st.session_state.train_scaled) == np.ndarray and type(st.session_state.train_target) == np.ndarray:
                        if st.session_state.train_scaled.size and st.session_state.train_target.size:
                            bDisabled = False

                    if st.form_submit_button('모델링평가(검증/예측)', disabled=bDisabled, width='stretch'):
                        with st.container(key='contDataPredict'):
                            self.Knnc.DataPredict(nNeighbors, nNewLength, nNewWeight)
                    # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
# ══════════════════════════════════════════════════════════════════════════════════════════
# 테스트 영역
# ══════════════════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    import traceback

    try:
        # test code...
        pass
    except Exception as Ex:
        print(traceback.format_exc())       # 예외 출력하기(예외처리)
# ##################################################################################################
# <END>
# ##################################################################################################
