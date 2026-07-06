# ##################################################################################################
# ComMgr.py - 공통 모듈
# ##################################################################################################
# ══════════════════════════════════════════════════════════════════════════════════════════
# 외부모듈 영역
# ══════════════════════════════════════════════════════════════════════════════════════════
import sys                                  # system 모듈(Built-In)
import os                                   # os 모듈(Built-In)
import time                                 # time 모듈(Built-In)
import datetime                             # datetime 모듈(Built-In)
import pprint                               # pprint 모듈(Built-In)
import gzip                                 # gzip 모듈(Built-In)

import numpy as np                          # Numpy 모듈(pip install numpy)
import pandas as pd                         # Pandas 모듈(pip install pandas)

import PyQt6.QtWidgets as QtWdg             # PyQt6 QtWidgets 모듈(pip install pyqt6)
import PyQt6.QtGui as QtGui                 # PyQt6 QtGui 모듈(pip install PyQt6)
import PyQt6.QtCore as QtCore               # PyQt6 QtCore 모듈(pip install PyQt6)

import matplotlib.axes as axes              # matplotlib axes 모듈(pip install matplotlib)

import darkdetect                           # darkdetect 모듈(pip install darkdetect)

import requests                             # requests 모듈(pip install requests)
import bs4                                  # BeautifulSoup4 모듈(pip install beautifulsoup4 or pip install bs4)
# ══════════════════════════════════════════════════════════════════════════════════════════
# 사용자정의 클래스 영역
# ------------------------------------------------------------------------------------------
# Common            - 공통 클래스
# Inheritance       - None
# ══════════════════════════════════════════════════════════════════════════════════════════
class Common():
    # ======================================================================================
    # 전역상수 관리 - 필수영역(정적변수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # Color         - 전역 색상 클래스
    # Inheritance   - None
    # ——————————————————————————————————————————————————————————————————————————————
    class Color():
        RED             = 'red'         # 빨강
        GREEN           = 'green'       # 초록
        BLUE            = 'blue'        # 파랑
        YELLOW          = 'yellow'      # 노랑
        CYAN            = 'cyan'        # 청록
        MAGENTA         = 'magenta'     # 자홍
        BLACK           = 'black'       # 검정
        WHITE           = 'white'       # 흰색
        GRAY            = 'gray'        # 회색
        ORANGE          = 'orange'      # 주황
        PURPLE          = 'purple'      # 보라
        BROWN           = 'brown'       # 갈색
        PINK            = 'pink'        # 분홍
        LIGHTGREEN      = 'lightgreen'  # 밝은 초록
    # ——————————————————————————————————————————————————————————————————————————————
    # ColorMode     - 전역 색상모드(라이트/다크) 클래스
    # Inheritance   - None
    # ——————————————————————————————————————————————————————————————————————————————
    class ColorMode():
        LIGHT           = 0             # 라이트 모드
        DARK            = 1             # 다크 모드
    # ======================================================================================
    # 전역클래스 관리 - 필수영역(사용자정의 보조클래스)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # UserEventFilter   - 사용자정의 이벤트 필터 클래스
    # Inheritance       - QtCore.QObject
    # ——————————————————————————————————————————————————————————————————————————————
    class UserEventFilter(QtCore.QObject):
        MouseWheelMoved = QtCore.pyqtSignal(object)                             # 커스텀 이벤트(시그널) 객체 생성
                                                                                # UserEventFilter 객체 안에 생성됨(self로 접근)

        def __init__(self, parent=None) -> None:
            super().__init__(parent)
            self.MouseWheelAccum = 0                                            # 포커스가 외부 브라우저에 있는 경우 휠 이벤트가 40개 발생됨을 처리

        def eventFilter(self, obj, event) -> None:                              # eventFilter 재정의
            oResult = None

            if event.type() == QtCore.QEvent.Type.Wheel:                        # 마우스 휠 이벤트인 경우
                # Ctrl + 마우스휠 움직이는 경우만 시그널 발생
                if event.modifiers() & \
                    QtCore.Qt.KeyboardModifier.ControlModifier:                 # Ctrl + 마우스 휠 인 경우
                    self.MouseWheelAccum = self.MouseWheelAccum + \
                                            event.angleDelta().y()              # 포커스가 외부 브라우저에 있는 경우
                                                                                # 이벤트가 40개 발생되므로 y() 값을 누적해서 120 확인 처리

                    # if abs(event.angleDelta().y()) == 120:                      # 포커스가 외부 브라우저가 아닌 경우 정확하게 y()는 120 반환됨
                    if abs(self.MouseWheelAccum) >= 120:                        # 누적 값이 120 이상인 경우 확인
                        self.MouseWheelMoved.emit(event)                        # 마우스 휠 이벤트(시그널) 발생
                        self.MouseWheelAccum = 0                                # 누적 값 초기화

                    oResult = True                                              # 기본 마우스 휠 스크롤 막기
                    
                else:
                    oResult = super().eventFilter(obj, event)                   # 기본 마우스 휠 스크롤 허용
            else:
                oResult = super().eventFilter(obj, event)                       # 기본 마우스 휠 스크롤 허용

            return oResult
    # ======================================================================================
    # 전역변수 관리 - 필수영역(정적변수)
    # ======================================================================================
    LogTextEdit:QtWdg.QTextEdit = None      # PrintLog()에서 사용할 텍스트 에디터 객체
    LogTextColorMode:ColorMode  = None      # PrintLog()에서 사용할 색상 모드
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
            # ==============================================================================
            # 전역변수 관리 - 필수영역(인스턴스변수)
            # ==============================================================================
            pass
            # ==============================================================================
            # 부모객체 생성 - 필수영역(상속을 받은 경우 필수)
            # ==============================================================================
            # super().__init__()              # 부모 클래스가 하나인 경우 부모 객체 생성
            # Parent1.__init__(self)          # 부모 클래스가 두개 이상인 경우 부모 객체 생성
            # Parent2.__init__(self)          # 부모 클래스가 두개 이상인 경우 부모 객체 생성
            # ==============================================================================
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ======================================================================================
    # 전역함수 관리 - 필수영역(정적함수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # ClearScreen   - 콘솔 화면 지우기
    # Args          - None
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def ClearScreen() -> None:
        try:
            os.system('cls')
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ClearTable    - QT 테이블 위젯 데이터 지우기
    # Args          - Table : QT 테이블 위젯 객체
    # Return        - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def ClearTable(Table:QtWdg.QTableWidget) -> None:
        try:
            Table.clear()
            Table.setColumnCount(0)
            Table.setRowCount(0)
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    # DoEvents  - PyQt 이벤트 큐 허용
    # Args      - None
    # Return    - None
    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    @staticmethod
    def DoEvents()->None:
        try:
            QtWdg.QApplication.processEvents()

            # import pythoncom                    # pythoncom 모듈(pip install pywin32 에 포함)
            # pythoncom.PumpWaitingMessages()
        except:
            raise Ex                # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # GetLengthOfArray  - 문자열 배열에서 가장긴 문자열의 길이 구하기
    # Args              - StrArray   : 문자열 배열
    # Return            - 가장긴 문자열의 길이(한글 1글자:2바이트 처리) 반환
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def GetLengthOfArray(StrArray:list) -> int:
        nLength = 0
        nByteLength = 0

        try:
            for sLine in StrArray:
                nByteLength = Common.GetStrLenB(sLine)

                if nLength < nByteLength: nLength = nByteLength
        except Exception as Ex:
            raise Ex                        # 예외 던지기

        return nLength
    # ——————————————————————————————————————————————————————————————————————————————
    # GetStrLenB    - 영문/한글이 섞인 문자열의 바이트 길이 구하기
    # Args          - Str       : 영문/한글이 섞인 문자열
    #               - Encode    : 한글 유니코드(기본:utf-8)
    # Return        - 문자열의 길이(영문 1글자:1바이트, 한글 1글자:2바이트 처리)
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def GetStrLenB(Str:str, Encode:str='utf-8') -> int:
        nLength = 0

        try:
            if len("가".encode(Encode)) == 3:
                # 한글1글자 : 3바이트인 경우
                nLength = len(Str) + int((len(Str.encode(Encode)) - len(Str)) / 2)
            else:
                # 한글1글자 : 2바이트인 경우
                nLength = len(Str.encode(Encode))
            # --------------------------------------------------------------
            # 다른 방법
            # --------------------------------------------------------------
            # for char in Str:
            #     if len(char.encode(Encode)) > 1:
            #         nHangulLen = nHangulLen + 1

            # nTotalLen = len(Str)
            # nTotalLen = (nTotalLen - nHangulLen) + (nHangulLen * 2)
            # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기

        return nLength
    # ——————————————————————————————————————————————————————————————————————————————
    # GetWeatherInfo    - 네이버 사이트에서 특정 지역의(시군구읍면동) 날씨 정보 가져오기(웹크롤링)
    # Args              - City      : 특정 지역의(시군구읍면동) 명칭
    # Return            - str
    # ——————————————————————————————————————————————————————————————————————————————
    # requests/response.text/bs4.BeautifulSoup 문법
    # --------------------------------------------------------------
    # response = requests.get(sUrl)
    # html = response.text                              # HTML 페이지 전체 소스
    # soup = bs4.BeautifulSoup(html, "html.parser")     # HTML 페이지 소스를 크롤링할 수 있도록 변환
    # soup.text                                         # HTML 페이지 소스에서 태그 모두 제거하고 내용만 남기기
    #
    # html = '''
    #           <div class='content'>
    #               <p class='example' id='target1'>첫번째문단</p>
    #               <p class='example' id='target2'>두번째문단</p>
    #           </div>
    #           <div class='content'>
    #               <h1>제목5</h1>
    #               <h1>제목6</h1>
    #           </div>
    #           <a href='http://www.naver.com'>네이버로 이동</a>
    #           <a href='#'>이동없음</a>
    #           <a>밑줄없음</a>
    #           <h1 class='example'>제목1</h1>
    #           <h1 class='example'>제목2</h1>
    #           <p>본문첫째줄</p>
    #           <p>본문두째줄</p>
    #           <p>본문셋째줄</p>
    #           <h1 id='target3'>제목3</h1>
    #           <h1 id='target4'>제목4</h1>
    #       '''
    # 
    # soup = BeautifulSoup(html, 'html.parser')
    # --------------------------------------------------------------
    # soup.select()/soup.select_one() 선택자(CSS Selector) 문법
    # --------------------------------------------------------------
    #   - 태그 선택자(태그)
    #       soup.select('p')                            # 모든 <p> 태그
    #       soup.select('p.example')                    # <p class='example'>  인 모든 태그 선택
    #       soup.select('div.example')                  # <div class='example'>인 모든 태그 선택
    #       soup.select('span#target')                  # <span id='target'>   인 모든 태그 선택
    #       soup.select('div.content p')                # <div class='content'>인 내부의 모든 <p> 태그 선택
    # 
    #   - 클래스 선택자(.)
    #       soup.select('.example')                     # class='example'인 모든 태그 선택
    # 
    #   - 아이디 선택자(#)
    #       soup.select('#target')                      # id='target'인 모든 태그 선택
    # 
    #   - 속성 선택자([])
    #       soup.select('a[href]')                      # <a href='...'> 인 모든 태그 선택
    #       soup.select("a[href='https://example.com']")# <a href='https://example.com'> 인 모든 태그 선택
    #       soup.select("a[href^='https']")             # <a href='https...'> 인 모든 태그 선택
    # 
    #   - 계층 구조 선택자(>)
    #       soup.select('ul.menu > li > a')             # <ul class='menu'> 바로 아래의 <li> 바로 아래의 모든 <a> 태그 선택
    #       soup.select('div.content > p')              # <div class='content'> 바로 아래의 모든 <p> 태그 선택
    # 
    #   - 여러 조건 조합(,)
    #       soup.select('p.example, span#target')       # <p class='example'> 와 <span id='target'>인 모든 태그 선택
    # --------------------------------------------------------------
    # soup.find()/soup.find_all() 문법
    # --------------------------------------------------------------
    # tag = soup.find('p')                                    # 첫 번째 <p> 태그
    # tag = soup.find('p', id='target1')                      # <p id='target1'>인 첫 번째 태그
    # tag = soup.find('p', id='target1').find_parent('div')   # <p id='target1'>인 첫 번째 태그의 부모 <div> 태그
    # tag = soup.find_all('p', class_='example')              # <p class='example'>인 모든 태그
    # 
    # tag = soup.find('h1').find_next_sibling('p')            # 첫 번째 <h1> 태그의 다음 형제 중 첫 번째 <p> 태그
    # tag = soup.find_all('p')[2].find_previous_sibling('h1') # 모든 <p> 태그중 세 번째 <p> 태그의 형제 중 이전 첫 번째 <h1> 태그
    # tag = soup.find_all('p')[2].find_next_sibling('h1')     # 모든 <p> 태그중 세 번째 <p> 태그의 형제 중 다음 첫 번째 <h1> 태그
    # 
    # tag = soup.find('h1').find_next('p')                    # 첫 번째 <h1> 태그의 다음 첫 번째 <p> 태그
    # tag = soup.find('h1').find_all_next("p")                # 첫 번째 <h1> 태그의 다음 모든 <p> 태그
    # 
    # tag = soup.find_all('p')[2].find_previous('h1')         # 모든 <p> 태그 중 세번째 <p> 태그의 앞 태그 중 첫 번째 <h1> 태그
    # 
    # print(tag.text)
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def GetWeatherInfo(City:str) -> str:
        sUrl        = None          # 네이버 날씨 정보 주소
        oResponse   = None          # Url 사이트 정보 저장 객체
        oSoup       = None          # HTML 페이지 소스를 크롤링할 수 있도록 변환한 객체
        oCity       = None          # 시군구읍면동 지역명 객체
        sCity       = None          # 시군구읍면동 지역명
        oTemp       = None          # 현재 기온 객체
        sTemp       = None          # 현재 기온
        oWeather    = None          # 날씨 정보 객체
        sWeather    = None          # 날씨 정보
        oTempBefore = None          # 어제 비교 기온/날씨 객체
        sTempBefore = None          # 어제 비교 기온/날씨
        oIconMap    = {}            # 날씨 정보 아이콘 맵
        sIcon       = None          # 날씨 정보 아이콘

        try:
            sUrl = f'https://search.naver.com/search.naver?query={City}+날씨'

            oResponse = requests.get(sUrl)

            oSoup = bs4.BeautifulSoup(oResponse.text, 'html.parser')    # HTML 페이지 소스를 크롤링할 수 있도록 객체 생성

            # 1. 시군구읍면동 지역명 가져오기
            oCity = oSoup.select_one('div.title_area._area_panel .title')
            sCity = oCity.text.strip() if oCity else '지역정보없음'

            # 2. 현재 기온 가져오기
            oTemp = oSoup.select_one('div.temperature_text')
            sTemp = oTemp.text.strip() if oTemp else '기온정보없음'

            # 3. 날씨 정보 가져오기
            oWeather = oSoup.select_one('div.weather_info span.blind')
            sWeather = oWeather.text.strip() if oWeather else '기온정보없음'

            # 4. 어제 비교 기온/날씨 상태 가져오기
            oTempBefore = oSoup.select_one('div.temperature_info p')
            sTempBefore = oTempBefore.text.replace('\n', '').strip() if oTempBefore else '어제정보없음'

            # 5. 파일에서 문자 아이콘 불러오기
            # oIconMap = {}
            # with open('WeatherIcons.txt', 'r', encoding='utf-8') as f:
            #     for line in f:
            #         if ':' in line:
            #             key, value = line.strip().split(':')
            #             oIconMap[key] = value

            # 6. 출력
            oIconMap = {'맑음':'☀️', '흐림':'☁️', '구름많음':'🌤️', '비':'🌧️', '눈':'❄️'}

            sIcon = oIconMap.get(sWeather, '❓')

            # 6. 출력
            # print("현재 기온:", oTemp)
            # print("현재 날씨 상태:", oWeather)
            # print(f"{oCity} : [{oTemp} / {icon} {oWeather} / {oTempComp}]")

            # return f'{oCity} : [{oTemp} / {sIcon} {oWeather} / {oTempComp}]'
        except Exception as Ex:
            raise Ex                        # 예외 던지기

        return f'{sCity} : {sTemp} / {sTempBefore} {sIcon}'
    # ——————————————————————————————————————————————————————————————————————————————
    # isWindowsDarkMode - 윈도우 테마가 다크 모드인지 확인
    # Args              - None
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def isWindowsDarkMode() -> bool:
        try:
            return darkdetect.isDark()

            # darkdetect.isLight():
            # print(darkdetect.theme())       # 'Dark' 또는 'Light'
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # MakeFashionMnistDataset   - Fashion-Mnist 데이터셋 생성
    # Args                      - None
    # Return                    - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def MakeFashionMnistDataset() -> bool:
        bResult = False

        try:
            # --------------------------------------------------------------
            # fashion-mnist.npz 파일이 없는 경우 생성
            # --------------------------------------------------------------
            import gzip, numpy as np, os

            def load_images(path):
                with gzip.open(path, 'rb') as f:
                    data = np.frombuffer(f.read(), np.uint8, offset=16)
                return data.reshape(-1, 28, 28)

            def load_labels(path):
                with gzip.open(path, 'rb') as f:
                    data = np.frombuffer(f.read(), np.uint8, offset=8)
                return data.reshape(-1,)

            # 원본 .gz 파일 경로 지정
            read_path = os.path.expanduser("~\\.keras\\datasets\\fashion-mnist\\")
            # read_path = f'C:\\Users\\{UserID}\\.keras\\datasets\\fashion-mnist\\'

            train_images_path = f"{read_path}train-images-idx3-ubyte.gz"
            train_labels_path = f"{read_path}train-labels-idx1-ubyte.gz"
            test_images_path  = f"{read_path}t10k-images-idx3-ubyte.gz"
            test_labels_path  = f"{read_path}t10k-labels-idx1-ubyte.gz"

            # 데이터 읽기
            x_train = load_images(train_images_path).astype("uint8")
            y_train = load_labels(train_labels_path).astype("uint8")
            x_test  = load_images(test_images_path).astype("uint8")
            y_test  = load_labels(test_labels_path).astype("uint8")

            # print("x_train:", x_train.shape, x_train.dtype)
            # print("y_train:", y_train.shape, y_train.dtype)
            # print("x_test:", x_test.shape, x_test.dtype)
            # print("y_test:", y_test.shape, y_test.dtype)

            # 압축 .npz 파일 경로 지정
            save_path = os.path.expanduser("~\\.keras\\datasets\\fashion-mnist.npz")
            # save_path = f'C:\\Users\\{UserID}\\.keras\\datasets\\fashion-mnist.npz'

            # Keras가 읽을 수 있는 위치에 fashion-mnist.npz 저장
            np.savez_compressed(save_path,
                                x_train=x_train, y_train=y_train,
                                x_test=x_test, y_test=y_test)

            # # 로컬 위치에 저장
            # save_path = "D:\\77.LectureStudy\\VisualStudioCode\\Python\\PythonStudy\\AIStudy\\Data\\fashion-mnist.npz"
            # np.savez_compressed(save_path,
            #                     x_train=x_train, y_train=y_train,
            #                     x_test=x_test, y_test=y_test)

            # print("Saved to:", save_path)

            bResult = True
        except Exception as Ex:
            raise Ex                        # 예외 던지기

        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # PrintListToTable  - 2차원 리스트를 QT 테이블 위젯에 넣기
    # Args              - ListData    : 2차원 리스트 데이터 객체
    #                   - Table       : QT 테이블 위젯 객체
    #                   - ColumnNames : QT 테이블 컬럼명 객체
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def PrintListToTable(ListData:list, Table:QtWdg.QTableWidget, ColumnNames:list=None) -> bool:
        bResult = False
        oColumnNames = []
        nRowCount = 0
        nColCount = 0

        try:
            # --------------------------------------------------------------
            # ResizeMode.ResizeToContents 모드인 경우
            # 행수를 변경하지 않으면 동일 쿼리 실행시 많이 느려짐(버그)
            # --------------------------------------------------------------
            # Table.clearContents()
            Table.setRowCount(0)
            Table.setColumnCount(0)
            # --------------------------------------------------------------
            # 행/열 수 만큼 메모리 할당
            # --------------------------------------------------------------
            if isinstance(ListData, list):                  # 리스트 배열 타입 확인
                nRowCount = len(ListData)                   # 행수 구하기

                Table.setRowCount(nRowCount)                    # 행수 만큼 메모리 할당

                if ColumnNames != None:                         # 테이블 컬럼명 있는 경우
                    oColumnNames = ColumnNames
                    nColCount = len(oColumnNames)               # 열수 구하기
                else:
                    if nRowCount > 0:                           # 리스트 데이터 있는 경우
                        nColCount = len(ListData[0])            # 열수 구하기
                    else:
                        nColCount = 5                           # 임시 열수 5로 하기

                    for nCol in range(0, nColCount):
                        oColumnNames.append(str(nCol + 1))      # 테이블 컬럼명 만들기

                Table.setColumnCount(nColCount)                 # 열수 만큼 메모리 할당
                # --------------------------------------------------------------
                # 테이블 컬럼명 지정
                # --------------------------------------------------------------
                if oColumnNames:
                    Table.setHorizontalHeaderLabels(oColumnNames)
                # --------------------------------------------------------------
                # 테이블 셀객체 생성
                # --------------------------------------------------------------
                for nRow in range(0, nRowCount):
                    for nCol in range(0, nColCount):
                        oItem = QtWdg.QTableWidgetItem(str(ListData[nRow][nCol]))
                        Table.setItem(nRow, nCol, oItem)
                # --------------------------------------------------------------
                # 테이블 셀 포커스 지정
                # --------------------------------------------------------------
                if nRowCount > 0 and nColCount > 0:
                    Table.setCurrentCell(0, 0)
            else:
                raise Exception('ListData 파라미터에 List 배열을 전달해야 합니다.\n\n' \
                                '프로그램 소스를 확인 하십시오.')
            # --------------------------------------------------------------
            bResult = True
        except Exception as Ex:
            raise Ex

        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # PrintNumpyToTable - 2차원 넘파이 배열을 QT 테이블 위젯에 넣기
    # Args              - NumpyData   : 2차원 넘파이 데이터 객체
    #                   - Table       : QT 테이블 위젯 객체
    #                   - ColumnNames : QT 테이블 컬럼명 객체
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def PrintNumpyToTable(NumpyData:np.ndarray, Table:QtWdg.QTableWidget, ColumnNames:list=None) -> bool:
        bResult = False
        oColumnNames = []
        nRowCount = 0
        nColCount = 0

        try:
            # --------------------------------------------------------------
            # ResizeMode.ResizeToContents 모드인 경우
            # 행수를 변경하지 않으면 동일 쿼리 실행시 많이 느려짐(버그)
            # --------------------------------------------------------------
            Table.setRowCount(0)
            Table.setColumnCount(0)
            # --------------------------------------------------------------
            # 행/열 수 만큼 메모리 할당
            # --------------------------------------------------------------
            if isinstance(NumpyData, np.ndarray):               # 넘파이 배열 타입 확인
                nRowCount = NumpyData.shape[0]                  # 행수 구하기
                nColCount = NumpyData.shape[1]                  # 열수 구하기

                Table.setRowCount(nRowCount)                    # 행수 만큼 메모리 할당

                if ColumnNames != None:                         # 테이블 컬럼명 있는 경우
                    oColumnNames = ColumnNames
                    nColCount = len(oColumnNames)               # 열수 구하기
                else:
                    if nRowCount > 0:                           # 리스트 데이터 있는 경우
                        nColCount = NumpyData.shape[1]          # 열수 구하기
                    else:
                        nColCount = 5                           # 임시 열수 5로 하기

                    for nCol in range(0, nColCount):
                        oColumnNames.append(str(nCol + 1))      # 테이블 컬럼명 만들기

                Table.setColumnCount(nColCount)                 # 열수 만큼 메모리 할당
                # --------------------------------------------------------------
                # 테이블 컬럼명 지정
                # --------------------------------------------------------------
                if ColumnNames:
                    Table.setHorizontalHeaderLabels(oColumnNames)
                # --------------------------------------------------------------
                # 테이블 셀객체 생성
                # --------------------------------------------------------------
                for nRow in range(0, nRowCount):
                    for nCol in range(0, nColCount):
                        oItem = QtWdg.QTableWidgetItem(str(NumpyData[nRow, nCol]))
                        Table.setItem(nRow, nCol, oItem)
                # --------------------------------------------------------------
                # 테이블 셀 포커스 지정
                # --------------------------------------------------------------
                if nRowCount > 0 and nColCount > 0:
                    Table.setCurrentCell(0, 0)
            else:
                raise Exception('NumpyData 파라미터에 Numpy 배열을 전달해야 합니다.\n\n' \
                                '프로그램 소스를 확인 하십시오.')
            # --------------------------------------------------------------
            bResult = True
        except Exception as Ex:
            raise Ex

        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # PrintDfToTable    - 데이터프레임을 QT 테이블 위젯에 넣기
    # Args              - Df    : 데이터프레임 객체
    #                   - Table : QT 테이블 위젯 객체
    #                   - AutoHeaderOK : QT 테이블 컬럼명 출력 여부
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def PrintDfToTable(Df:pd.DataFrame, Table:QtWdg.QTableWidget, AutoHeader:bool=True) -> bool:
        bResult = False
        oColumnNames = []
        oRowNames    = []
        nColCount    = 0
        nRowCount    = 0
        nRowInc      = 0

        try:
            # --------------------------------------------------------------
            # ResizeMode.ResizeToContents 모드인 경우
            # 행수를 변경하지 않으면 동일 쿼리 실행시 많이 느려짐(버그)
            # --------------------------------------------------------------
            Table.setRowCount(0)
            Table.setColumnCount(0)
            # --------------------------------------------------------------
            # 행/열 수 만큼 메모리 할당
            # --------------------------------------------------------------
            if isinstance(Df, pd.DataFrame):                    # 데이터프레임 배열 타입 확인
                nRowCount = Df.shape[0]                         # 행수 구하기
                nColCount = Df.shape[1]                         # 열수 구하기

                if Df.columns.empty == False:                   # 테이블 컬럼명 있는 경우
                    oColumnNames = Df.columns.astype(str).to_list()
                    nColCount = len(oColumnNames)               # 열수 구하기

                Table.setColumnCount(nColCount)                 # 열수 만큼 메모리 할당

                if Df.index.empty == False:                     # 테이블 인덱스명 있는 경우
                    if nRowCount > 0 and Df.index.dtype == 'int64' and Df.index[0] == 0:
                        nRowInc = 1

                    oRowNames = (Df.index + nRowInc).astype(str).to_list()
                    nRowCount = len(oRowNames)                  # 행수 구하기

                Table.setRowCount(nRowCount)                    # 행수 만큼 메모리 할당
                # --------------------------------------------------------------
                # 테이블 컬럼명/인덱스명 지정
                # --------------------------------------------------------------
                if AutoHeader:
                    Table.setHorizontalHeaderLabels(oColumnNames)
                    Table.setVerticalHeaderLabels(oRowNames)
                # --------------------------------------------------------------
                # 테이블 셀객체 생성
                # --------------------------------------------------------------
                for nRow in range(0, nRowCount):
                    for nCol in range(0, nColCount):
                        oItem = QtWdg.QTableWidgetItem(str(Df[Df.columns[nCol]][nRow]))
                        Table.setItem(nRow, nCol, oItem)
                # --------------------------------------------------------------
                # 테이블 셀 포커스 지정
                # --------------------------------------------------------------
                if nRowCount > 0 and nColCount > 0:
                    Table.setCurrentCell(0, 0)
            else:
                raise Exception('Df 파라미터에 데이터프레임을 전달해야 합니다.\n\n' \
                                '프로그램 소스를 확인 하십시오.')
            # --------------------------------------------------------------
            bResult = True
        except Exception as Ex:
            raise Ex

        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # PrintImageToAxes  - 이미지를 Axes에 그리드 구조로 출력
    # Args              - ImagesData    : 이미지 데이터셋
    #                   - ImagesText    : 이미지 별 텍스트
    #                   - ImageSize     : 이미지 픽셀 크기
    #                   - Rows          : 이미지 출력 행수
    #                   - Cols          : 이미지 출력 열수
    #                   - ax            : 이미지 출력 Axes
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def PrintImageToAxes(ImagesData:np.ndarray, ImagesText:np.ndarray, ImageSize:int, Rows:int, Cols:int, ax:axes.Axes) -> bool:
        bResult         = False
        img_size        = ImageSize
        rows, cols      = Rows, Cols    # 12 x 10
        col_gab_size    = 10
        row_gab_size    = 30
        col_gap_img     = None
        row_gap_img     = None
        font_size       = 7
        rows_images     = []
        grid_image      = None
        images          = None

        try:
            images = [ImagesData[i] for i in range(rows*cols)]

            # 가로 간격용 흰색 띠
            col_gap_img = np.ones((img_size, col_gab_size))

            # 세로 간격용 흰색 띠(글자 크기 포함 되도록)
            row_gap_img = np.ones((row_gab_size, img_size*cols + (cols-1)*col_gab_size))

            # 행별로 합치기
            for row in range(rows):
                one_row_cols_imgs = []

                # 이미지를 열로 합쳐서 한행 만들기
                for col in range(cols):
                    one_row_cols_imgs.append(images[row*cols+col])

                    # 열사이 간격 넣기
                    if col < cols-1:
                        one_row_cols_imgs.append(col_gap_img)

                # 열 이미지를 합쳐서 한행 만들기
                one_row_img = np.concatenate(one_row_cols_imgs, axis=1)
                rows_images.append(one_row_img)

                # 행사이 간격 넣기
                if row < rows-1:
                    rows_images.append(row_gap_img)

            # 행이미지를 합쳐서 그리드 만들기
            grid_image = np.vstack(rows_images)
            ax.imshow(grid_image, cmap="gray_r")
            ax.axis("off")

            # 이미지 상단에 글자 표시
            for row in range(rows):
                for col in range(cols):
                    x = col*(img_size+col_gab_size) + img_size/2
                    y = row*(img_size+row_gab_size)

                    ax.text(x, y, f'{ImagesText[row*cols+col]}',
                            color='red', ha='center', va='bottom',
                            fontsize=font_size)

            # 테두리 색상 변경
            # for spine in ax.spines.values():
            #     spine.set_edgecolor("green")    # 테두리 색상
            #     spine.set_linewidth(2)          # 테두리 두께

            bResult = True
        except Exception as Ex:
            raise Ex                        # 예외 던지기
        
        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # PrintImageToTable - 이미지를 QT 테이블 위젯에 넣기
    # Args              - ImagesData    : 이미지 데이터셋
    #                   - ImagesText    : 이미지 별 텍스트
    #                   - Table         : QT 테이블 위젯 객체
    #                   - Rows          : 이미지 출력 행수
    #                   - Cols          : 이미지 출력 열수
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def PrintImageToTable(ImagesData:np.ndarray, ImagesText:np.ndarray, Table:QtWdg.QTableWidget, Rows:int, Cols:int) -> bool:
        bResult = False

        try:
            Table.setRowCount(0)
            Table.setColumnCount(0)

            Table.setRowCount(Rows*2)
            Table.setColumnCount(Cols)

            # 첫 9개 이미지를 테이블에 넣기
            for row in range(0, Rows*2, 2):
                for col in range(0, Cols):
                    idx = row * 3 + col

                    img_array = ImagesData[idx]         # 28x28 numpy 배열
                    img_array = 255 - img_array         # gray_r 효과: 값 반전

                    # numpy 배열 → QImage 변환
                    qimg = QtGui.QImage(img_array.data, 28, 28, QtGui.QImage.Format.Format_Grayscale8)
                    pixmap = QtGui.QPixmap.fromImage(qimg).scaled(28, 28)

                    # QLabel에 이미지 넣기
                    label = QtWdg.QLabel()
                    label.setPixmap(pixmap)

                    # QLabel 셀에 배치
                    Table.setCellWidget(row, col, label)

                    # 이미지 텍스트 만들기
                    item = QtWdg.QTableWidgetItem(str(ImagesText[idx]))

                    # 폰트 크기와 스타일 변경
                    font = QtGui.QFont()
                    font.setPointSize(9)
                    font.setBold(True)

                    # 텍스트 정렬 및 색상 변경
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
                    item.setBackground(QtGui.QBrush(QtGui.QColor('white')))
                    item.setFont(font)

                    # 테이블에 텍스트 아이템 넣기
                    Table.setItem(row+1, col, item)

            # 테이블 셀의 행 높이 변경
            for row in range(0, Table.rowCount()):
                if row % 2 == 0:
                    Table.setRowHeight(row, 30)
                else:
                    Table.setRowHeight(row, 5)

            # 테이블 셀의 열 너비 변경
            for col in range(0, Table.columnCount()):
                Table.setColumnWidth(col, 28)

            Table.show()

            bResult = False
        except Exception as Ex:
            raise Ex                        # 예외 던지기
        
        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # PrintLog  - 문자열 데이터를 텍스트 에디터 객체에 출력
    # Args      - HeadLine          : 출력 할 헤더 문자열('{...}' 형식인 경우 메인 헤더)
    #           - LogText           : 출력 할 로그 텍스트(Common.LogTextEdit != None 인 경우 무시됨)
    #           - TextEdit          : !None - 출력 할 텍스트 에디터 객체 인스턴스
    #                                  None - 콘솔창에 출력
    #           - Wrap              : True/False  - 텍스트 에디터 객체 자동 줄바꿈 여부
    #           - ClearLog          : True/False  - 로그 텍스트 초기화 여부(콘솔은 의미 없음)
    #           - AutoScroll        : True/False  - 로그 텍스트 출력하고 자동 아래로 스크롤 여부(콘솔은 의미 없음)
    #           - HeadFontItalic    : True/False  - 헤더 폰트 이탤릭 여부
    #           - HeadSubOff        : True/False  - 보조 헤더 출력 여부
    #           - HeadSubUnderLine  : True/False  - 보조 헤더 아래에 라인 출력 여부
    #           - LogFontBold       : True/False  - 로그 텍스트 폰트 굵기 여부
    #           - LogTextType       : True/False  - 로그 텍스트 타입 출력 여부
    #           - LogDateTime       : True/False  - 로그 텍스트 시간 출력 여부
    #           - NumpyRowAll       : True  - Numpy 행을 생략 없이 출력
    #                                 False - Numpy 행을 생략 해서 출력(위 3줄 ... 아래 3줄)
    #           - NumpyOneRowLen    : None  - Numpy 한 행을 한줄로 출력
    #                                 Num   - Numpy 한 행을 Num 길이로 출력(Num 초과시 다음줄에 출력)
    #           - PandasRows        : None  - DataFrame 행을 생략 없이 출력
    #                                 Num   - DataFrame 행을 Num 수 만큼 만 출력
    #           - PandasCols        : None  - DataFrame 열을 생략 없이 출력
    #                                 Num   - DataFrame 열을 Num 수 만큼 만 출력
    #           - HeadColor         : None  - 헤더를 기본 색상으로 출력
    #                                 Color - 헤더를 지정 색상으로 출력
    #           - LogTextColor      : None  - 로그 텍스트 기본 색상으로 출력
    #                                 Color - 로그 텍스트 지정 색상으로 출력
    #           - LogTextColorMode  : 로그 출력 텍스트 색상을 색상모드(다크/라이트)에 마추기
    #                                 (Common.LogTextColorMode != None 인 경우 무시됨)
    # Return    - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def PrintLog(HeadLine:str, LogText:object=None,
                 TextEdit:QtWdg.QTextEdit=None,
                 Wrap:bool=False, ClearLog:bool=False, AutoScroll:bool=True,
                 HeadFontItalic:bool=False,
                 HeadSubOff:bool=False, HeadSubUnderLine:bool=True,
                 LogFontBold:bool=False, LogTextType:bool=True, LogDateTime:bool=True,
                 NumpyRowAll:bool=False, NumpyOneRowLen:int=None,
                 PandasRows:int=10, PandasCols:int=None,
                 HeadColor:str=None, LogTextColor:str=None, LogTextColorMode:ColorMode=ColorMode.DARK) -> None:
        sBeforeLogText      = None                  # 텍스트 에디터 기존 로그 텍스트
        sHeadLineMain       = None                  # 메인 헤더
        sHeadLineSub        = None                  # 보조 헤더

        sHeadLineMainColor  = None                  # 메인 헤더 기본 색상
        sHeadLineSubColor   = None                  # 보조 헤더 기본 색상
        sLogTextColor       = None                  # 로그 텍스트 기본 색상
        sLogTextTypeColor   = None                  # 로그 텍스트 타입 기본 색상

        sHeadMainChar       = ['{', '}']            # 메인 헤더 확인용
        sHeadChar           = ['▶', '◀', '▽']       # 헤더 시작/끝 문자[메인헤더좌, 메인헤더우, 보조헤더좌우] : '▶', '◀', '▽'
        sHeadLineChar       = ['—', '—', '—']       # 헤더 위/아래 라인 문자[메인헤더위, 메인헤더아래, 보조헤더아래] : '_', '‾', '—'
        nHeadLineLen        = 0                     # 헤더 위/아래 라인 길이

        sLogTextType        = None                  # 로그 텍스트 타입
        oTextEditCursor     = None                  # 텍스트 에디터 커서 객체
        oTextEditFormat     = None                  # 텍스트 에디터 문자열 형식 객체(색상, 폰트굵기)

        try:
            # --------------------------------------------------------------
            # 로그 출력 텍스트 에디터 객체 확인
            # --------------------------------------------------------------
            if Common.LogTextEdit != None:
                TextEdit = Common.LogTextEdit
            # --------------------------------------------------------------
            # 로그 출력 텍스트 색상모드(다크/라이트) 확인
            # --------------------------------------------------------------
            if Common.LogTextColorMode == None:
                # 윈도우 테마 모드로 적용
                if Common.isWindowsDarkMode():
                    LogTextColorMode = Common.ColorMode.DARK
                else:
                    LogTextColorMode = Common.ColorMode.LIGHT
            else:
                LogTextColorMode = Common.LogTextColorMode

            if LogTextColorMode == Common.ColorMode.LIGHT:
                sHeadLineMainColor  = Common.Color.GREEN    # 메인 헤더 기본 색상
                sHeadLineSubColor   = Common.Color.BROWN    # 보조 헤더 기본 색상
                sLogTextColor       = Common.Color.BLACK    # 로그 텍스트 기본 색상
                sLogTextTypeColor   = Common.Color.BLUE     # 로그 텍스트 타입 기본 색상
            elif LogTextColorMode == Common.ColorMode.DARK:
                sHeadLineMainColor  = Common.Color.ORANGE   # 메인 헤더 기본 색상
                sHeadLineSubColor   = Common.Color.WHITE    # 보조 헤더 기본 색상
                sLogTextColor       = Common.Color.CYAN     # 로그 텍스트 기본 색상
                sLogTextTypeColor   = Common.Color.YELLOW   # 로그 텍스트 타입 기본 색상
            # --------------------------------------------------------------
            # Numpy 출력 설정
            # --------------------------------------------------------------
            # Numpy 행 생략 없이 출력(threshold=np.inf)
            # Numpy 행 생략 해서 출력(threshold=데이터길이-1)
            # --------------------------------------------------------------
            if NumpyRowAll: np.set_printoptions(threshold=np.inf)
            elif type(LogText) == np.ndarray and len(LogText):
                            np.set_printoptions(threshold=len(LogText)-1)
            else:           np.set_printoptions(threshold=1000)
            # --------------------------------------------------------------
            # Numpy 행 한줄로 출력(linewidth=np.inf)
            # Numpy 행 지정 길이로 출력(linewidth=행길이)
            # --------------------------------------------------------------
            if NumpyOneRowLen == None: np.set_printoptions(linewidth=np.inf)
            elif NumpyOneRowLen > 0:   np.set_printoptions(linewidth=NumpyOneRowLen)
            else:                      np.set_printoptions(linewidth=75)
            # --------------------------------------------------------------
            # Pandas 출력 설정
            # --------------------------------------------------------------
            # DataFrame 행 데이터 출력('display.max_rows',    None(전체) | 출력행수)
            # DataFrame 열 데이터 출력('display.max_columns', None(전체) | 출력열수)
            # --------------------------------------------------------------
            if PandasRows == None or PandasRows > 0: pd.set_option('display.max_rows', PandasRows)
            if PandasCols == None or PandasCols > 0: pd.set_option('display.max_columns', PandasCols)
            # --------------------------------------------------------------
            # 헤더 만들기
            # --------------------------------------------------------------
            if HeadSubUnderLine == False:
                sHeadLineChar[2] = ''

            if HeadLine != None and type(HeadLine) == str and len(HeadLine) > 0 and \
                HeadLine[0] == sHeadMainChar[0] and HeadLine[-1] == sHeadMainChar[1]:
                HeadLine = HeadLine.strip(''.join(sHeadMainChar))

                sHeadLineMain = f'{sHeadChar[0]} {HeadLine} {sHeadChar[1]}'
                nHeadLineLen = Common.GetStrLenB(sHeadLineMain)

                sHeadLineMain = f'{sHeadLineChar[0]*nHeadLineLen}\n{sHeadLineMain}'
                sHeadLineMain = f'{sHeadLineMain}\n{sHeadLineChar[1]*nHeadLineLen}\n'

                if LogDateTime: sHeadLineMain = f'{sHeadLineMain}[{str(datetime.datetime.now())}]\n\n'
            else:
                sHeadLineSub = f'{sHeadChar[2]} {HeadLine} {sHeadChar[2]}'
                nHeadLineLen = Common.GetStrLenB(sHeadLineSub)

                sHeadLineSub = f'{sHeadLineSub}\n{sHeadLineChar[2]*nHeadLineLen}\n'

                if LogDateTime: sHeadLineSub = f'{sHeadLineSub}[{str(datetime.datetime.now())}]\n\n'
            # --------------------------------------------------------------
            # 로그 텍스트 타입 만들기
            # --------------------------------------------------------------
            if LogTextType: sLogTextType = f'{type(LogText)}'
            else:           sLogTextType = ''
            # --------------------------------------------------------------
            # 데이터가 Numpy, Pandas, List, Tuple인 경우 로그 텍스트 타입 뒤에 배열 길이를 붙이기
            # --------------------------------------------------------------
            if type(LogText) == np.ndarray or type(LogText) == pd.DataFrame:
                if sLogTextType: sLogTextType = f'{sLogTextType}, <size: {LogText.shape}>'
            elif type(LogText) == list or type(LogText) == tuple:
                if sLogTextType: sLogTextType = f'{sLogTextType}, <size: {np.array(LogText).shape}>'
            # --------------------------------------------------------------
            # 텍스트 에디터 객체에 출력
            # --------------------------------------------------------------
            if TextEdit:
                if ClearLog: TextEdit.clear()                               # 텍스트 에디터 초기화

                if Wrap != None: Common.SetTextEditWrap(TextEdit, Wrap)     # 텍스트 에디터 내려쓰기 모드 지정
                # --------------------------------------------------------------
                # 헤더와 데이터를 지정 색상으로 출력
                # --------------------------------------------------------------
                # 텍스트 에디터 출력 준비
                sBeforeLogText = TextEdit.toPlainText()                             # 로그 텍스트 읽기
                oTextEditCursor = TextEdit.textCursor()                             # 로그 텍스트 커서 객체 생성
                oTextEditCursor.setPosition(len(sBeforeLogText))                    # 로그 텍스트 커서 끝에 위치
                oTextEditFormat = QtGui.QTextCharFormat()                           # 텍스트 에디터 폰트 객체 생성

                # 헤더 출력
                if not HeadColor is None:
                    oTextEditFormat.setForeground(QtGui.QColor(HeadColor))              # 폰트 색상
                else:
                    if not sHeadLineMain is None:
                        oTextEditFormat.setForeground(QtGui.QColor(sHeadLineMainColor)) # 폰트 색상
                        oTextEditFormat.setFontWeight(QtGui.QFont.Weight.Bold)          # 폰트 굵기
                    else:
                        oTextEditFormat.setForeground(QtGui.QColor(sHeadLineSubColor))  # 폰트 색상

                if HeadFontItalic: oTextEditFormat.setFontItalic(True)                  # 헤더 폰트 이탤릭

                if not sHeadLineMain is None:
                    oTextEditCursor.insertText(f'{sHeadLineMain}', oTextEditFormat)     # 메인 헤더 출력
                else:
                    if HeadSubOff == False:
                        oTextEditCursor.insertText(f'{sHeadLineSub}', oTextEditFormat)  # 보조 헤더 출력

                oTextEditFormat.setFontWeight(QtGui.QFont.Weight.Normal)                # 폰트 굵기
                oTextEditFormat.setFontItalic(False)                                    # 헤더 폰트 이탤릭 해재

                # 로그 텍스트 & Type 출력
                if LogFontBold: oTextEditFormat.setFontWeight(QtGui.QFont.Weight.Bold)     # 폰트 굵기

                if not LogText is None:
                    if not LogTextColor is None: oTextEditFormat.setForeground(QtGui.QColor(LogTextColor))  # 폰트 색상
                    else:                        oTextEditFormat.setForeground(QtGui.QColor(sLogTextColor)) # 폰트 색상

                    oTextEditCursor.insertText(f'{LogText}\n', oTextEditFormat)                 # 로그 텍스트 출력

                    if 'size:' in sLogTextType:
                        oTextEditFormat.setForeground(QtGui.QColor(sLogTextTypeColor))          # 폰트 색상

                        oTextEditCursor.insertText(f'{sLogTextType}\n\n', oTextEditFormat)      # Type 출력
                    else:
                        oTextEditCursor.insertText('\n', oTextEditFormat)                       # 개행 출력
                else:
                    oTextEditCursor.insertText('\n', oTextEditFormat)                           # 개행 출력

                oTextEditFormat.setFontWeight(QtGui.QFont.Weight.Normal)                        # 폰트 굵기

                if AutoScroll: TextEdit.moveCursor(QtGui.QTextCursor.MoveOperation.End)         # 자동 스크롤
            # --------------------------------------------------------------
            # 콘솔창에 출력
            # --------------------------------------------------------------
            else:
                if ClearLog: Common.ClearScreen()

                # 헤더 출력
                if not sHeadLineMain is None: print(f'{sHeadLineMain}', end='')
                else:                         print(f'{sHeadLineSub}',  end='')

                # 로그 텍스트 출력
                if not LogText is None:
                    if type(LogText) != dict: print(f'{LogText}\n', end='')
                    else:                     pprint.pprint(LogText)

                    if 'size:' in sLogTextType: print(f'{sLogTextType}\n\n', end='')
                    else:                       print('\n', end='')
                else:
                    print('\n', end='')
            # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
        finally:
            Common.DoEvents()
    # ——————————————————————————————————————————————————————————————————————————————
    # SetMouseCursor    - 마우스 커서를 처리중 또는 기본값으로 변경
    # Args              - WaitCursor : True  - 처리중 모양으로 변경
    #                                  False - 기본값 모양으로 변경
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def SetMouseCursor(WaitCursor:bool=False) -> None:
        try:
            if WaitCursor == False: QtWdg.QApplication.restoreOverrideCursor()
            else:                   QtWdg.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)

            # 커서 변경 이벤트 즉시 반영(커서 변경이 보이지 않는 경우 활성화)
            # QtWdg.QApplication.processEvents()
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # SetTextEditWrap   - 텍스트 에디터 Word Wrap 기능 지정
    # Args              - TextEdit : 텍스트 에디터 객체 인스턴스
    #                   - Wrap     : True  - 텍스트 에디터 객체 자동 줄바꿈 허용
    #                                False - 텍스트 에디터 객체 자동 줄바꿈 없음
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def SetTextEditWrap(TextEdit:QtWdg.QTextEdit, Wrap:bool=True) -> None:
        try:
            if Wrap: TextEdit.setLineWrapMode(QtWdg.QTextEdit.LineWrapMode.WidgetWidth)
            else:    TextEdit.setLineWrapMode(QtWdg.QTextEdit.LineWrapMode.NoWrap)
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # Wait      - 화면 정지(콘솔 프로그램 인 경우에만 해당)
    # Args      - Message : 메시지를 출력하고 화면 정지
    # Return    - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def Wait(Message:str) -> None:
        try:
            print('\n')
            input(Message)
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # ZoomTextEditFont  - 텍스트 에디터 폰트 확대/축소
    # Args              - event     : 텍스트 에디터 이벤트(시그널) 객체
    #                   - TextEdit  : 텍스트 에디터 객체
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    @staticmethod
    def ZoomTextEditFont(event, TextEdit:QtWdg.QTextEdit):
        oMouseCursor       = None                           # 마우스 커서 객체
        oMouseCurRect      = None                           # 마우스 현재 위치 객체
        nMouseCurY         = 0                              # 마우스 현재 Y 좌표값
        oMouseNewRect      = None                           # 마우스 새위치 객체
        nMouseNewY         = 0                              # 마우스 새위치 Y 좌표값
        nMouseDiffY        = 0                              # 마우스 새위치와 이전위치 차이값

        oTextEditScrollbar = None                           # 텍스트 에디터 스크롤바 객체
        oTextEditFont      = None                           # 텍스트 에디터 폰트 객체
        nTextEditFontSize  = 0                              # 텍스트 에디터 폰트 크기

        try:
            if event.modifiers() & QtCore.Qt.KeyboardModifier.ControlModifier:
                # 1. 마우스 위치에 해당하는 커서 객체 구하기
                oMouseCursor = TextEdit.cursorForPosition(event.position().toPoint())

                # 2. 현재 마우스 커서의 화면 좌표 저장
                oMouseCurRect = TextEdit.cursorRect(oMouseCursor)
                nMouseCurY = oMouseCurRect.top()

                # 3. 텍스트 에디터 폰트 크기 변경
                oTextEditFont = TextEdit.font()
                nTextEditFontSize = oTextEditFont.pointSize()

                if event.angleDelta().y() > 0:                          # 마우스휠 위로
                    nTextEditFontSize = nTextEditFontSize + 1
                    # textObject.zoomIn()
                else:                                                   # 마우스휠 아래로
                    nTextEditFontSize = nTextEditFontSize - 1
                    # textObject.zoomOut()

                if nTextEditFontSize < 1:     nTextEditFontSize = 1     # 텍스트 에디터 폰트 크기 최소값 제한
                elif nTextEditFontSize > 100: nTextEditFontSize = 100   # 텍스트 에디터 최소 크기 최대값 제한

                oTextEditFont.setPointSize(nTextEditFontSize)
                TextEdit.setFont(oTextEditFont)

                # 4. 마우스 커서 위치 구하기
                oMouseNewRect = TextEdit.cursorRect(oMouseCursor)
                nMouseNewY = oMouseNewRect.top()

                # 5. 텍스트 에디터 스크롤 보정
                # 마우스 커서 중심으로 폰트 확대/축소 되도록 처리
                nMouseDiffY = nMouseNewY - nMouseCurY

                oTextEditScrollbar = TextEdit.verticalScrollBar()
                oTextEditScrollbar.setValue(oTextEditScrollbar.value() + nMouseDiffY)
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ======================================================================================
    # 전역함수 관리 - 필수영역(인스턴스함)
    # ======================================================================================
    pass
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