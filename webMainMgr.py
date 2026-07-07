# ##################################################################################################
# MLMgr.py - 머신러닝 모델 클래스 모듈
# ##################################################################################################
# ══════════════════════════════════════════════════════════════════════════════════════════
# 외부모듈 영역
# ══════════════════════════════════════════════════════════════════════════════════════════
import sys                                  # system 모듈(Built-In)
import os                                   # os 모듈(Built-In)
import io                                   # io 모듈(Built-In)
import time                                 # time 모듈(Built-In)
import datetime                             # datetime 모듈(Built-in)
import traceback                            # datetime 모듈(Built-in)

import numpy as np                          # Numpy 모듈(pip install numpy)
import pandas as pd                         # Pandas 모듈(pip install pandas)

import matplotlib.pyplot as plt             # matplotlib.pyplot 모듈(pip install matplotlib)
import matplotlib as pltlib                 # matplotlib 모듈(pip install matplotlib)
import matplotlib.font_manager as pltfont   # matplotlib 모듈(pip install matplotlib)

import streamlit as st                      # streamlit 모듈(pip install streamlit)

import sklearn.model_selection              # sklearn.model_selection 모듈(pip install scikit-learn)
import sklearn.neighbors                    # sklearn.neighbors 모듈(pip install scikit-learn)
import sklearn.metrics                      # sklearn.metrics 모듈(pip install scikit-learn)
import sklearn.linear_model                 # sklearn.linear_model 모듈(pip install scikit-learn)
import sklearn.preprocessing                # sklearn.preprocessing 모듈(pip install scikit-learn)
import sklearn.tree                         # sklearn.tree 모듈(pip install scikit-learn)
import sklearn.ensemble                     # sklearn.ensemble 모듈(pip install scikit-learn)
# ══════════════════════════════════════════════════════════════════════════════════════════
# 사용자정의 클래스 영역
# ------------------------------------------------------------------------------------------
# Knnc          - k-최근접이웃분류(k-Nearest Neighbors Classification) 모델 클래스
# Inheritance   - None
# ══════════════════════════════════════════════════════════════════════════════════════════
class Knnc():
    # ======================================================================================
    # 전역상수 관리 - 필수영역(정적변수)
    # ======================================================================================
    pass
    # ======================================================================================
    # 전역클래스 관리 - 필수영역(사용자정의 보조클래스)
    # ======================================================================================
    pass
    # ======================================================================================
    # 전역변수 관리 - 필수영역(정적변수)
    # ======================================================================================
    pass
    # ======================================================================================
    # 생성자 관리 - 필수영역(인스턴스함수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # __init__  - 생성자(인스턴스변수 생성/초기화)
    # Args      - self : 인공지능 모델 객체 인스턴스
    #           - Form : 윈도우 폼 객체 인스턴스
    # Return    - None
    # ——————————————————————————————————————————————————————————————————————————————
    def __init__(self): #, Form:Ui_frmMain.Ui_Form) -> None:
        sFontPath = None

        try:
            # ==============================================================================
            # 전역변수 관리 - 필수영역(인스턴스변수)
            # ==============================================================================
            # self.frmMain                = Form      # 윈도우 폼 객체 저장
            # self.TrainComplete          = False     # 학습 완료 상태 확인용
            # self.ModelTitle             = '[k-최근접이웃분류 모델]'

            # self.knnc                   = None      # k-최근접이웃분류 모델 객체

            # self.fish_data              = None      # 원본데이터(도미/빙어) 길이/무게
            # self.fish_length_data       = None      # 원본데이터(도미/빙어) 길이
            # self.fish_weight_data       = None      # 원본데이터(도미/빙어) 무게
            # self.fish_target            = None      # 원본데이터(도미/빙어) 정답데이터

            # self.train_input:np.ndarray = None      # 학습데이터
            # self.val_input:np.ndarray   = None      # 검증데이터
            # self.train_target           = None      # 학습용정답
            # self.val_target             = None      # 검증용정답

            # self.train_scaled           = None      # 학습데이터 표준점수(z점수)
            # self.val_scaled             = None      # 검증데이터 표준점수(z점수)
            # self.new_fish_scaled        = None      # New-Fish 길이/무게 표준점수
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
            # matplotlib 폰트가 StreamLit Cloud 에서 깨짐 방지
            # --------------------------------------------------------------
            # # 나눔 폰트가 설치되는 기본 경로 확인
            # sFontPath = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

            # if os.path.exists(sFontPath):
            #     # 클라우드 환경 (리눅스)
            #     font_prop = pltfont.FontProperties(fname=sFontPath)
            #     plt.rc('font', family=font_prop.get_name())
            # else:
            #     # 로컬 환경 (OS별 자동 지정 또는 맑은 고딕)
            #     plt.rc('font', family='Malgun Gothic')
                
            # # # 마이너스 기호 깨짐 방지
            # # plt.rcParams['axes.unicode_minus'] = False


            # 현재 파이썬 파일과 같은 위치에 있는 폰트 파일 지정
            sFontPath = os.path.join(os.path.dirname(__file__), "NanumGothic.ttf")

            if os.path.exists(sFontPath):
                font_prop = pltfont.FontProperties(fname=sFontPath)
                # Matplotlib의 기본 폰트 패밀리 이름을 이 폰트의 실제 이름으로 설정
                plt.rc('font', family=font_prop.get_name())
            else:
                # 폰트 파일이 없을 때만 로컬 시스템 폰트 사용
                plt.rc('font', family='sans-serif')



            # --------------------------------------------------------------
            if 'knnc' not in st.session_state:
                st.session_state.knnc = None                # k-최근접이웃분류 모델 객체

            if 'fish_data' not in st.session_state:
                st.session_state.fish_data = None           # 원본데이터(도미/빙어) 길이/무게
            if 'fish_length_data' not in st.session_state:
                st.session_state.fish_length_data = None    # 원본데이터(도미/빙어) 길이
            if 'fish_weight_data' not in st.session_state:
                st.session_state.fish_weight_data = None    # 원본데이터(도미/빙어) 무게
            if 'fish_target' not in st.session_state:
                st.session_state.fish_target = None         # 원본데이터(도미/빙어) 정답데이터

            if 'train_input' not in st.session_state:
                st.session_state.train_input = None         # 학습데이터
            if 'val_input' not in st.session_state:
                st.session_state.val_input = None           # 검증데이터
            if 'train_target' not in st.session_state:
                st.session_state.train_target = None        # 학습용정답
            if 'val_target' not in st.session_state:
                st.session_state.val_target = None          # 검증용정답

            if 'train_scaled' not in st.session_state:
                st.session_state.train_scaled = None        # 학습데이터 표준점수(z점수)
            if 'val_scaled' not in st.session_state:
                st.session_state.val_scaled = None          # 검증데이터 표준점수(z점수)
            if 'new_fish_scaled' not in st.session_state:
                st.session_state.new_fish_scaled = None     # New-Fish 길이/무게 표준점수

            # ==============================================================================
            # 부모객체 생성 - 필수영역(상속을 받은 경우 필수)
            # ==============================================================================
            # super().__init__()                      # 부모 클래스가 하나인 경우 부모 객체 생성
            # Parent1.__init__(self)                  # 부모 클래스가 두개 이상인 경우 부모 객체 생성
            # Parent2.__init__(self)                  # 부모 클래스가 두개 이상인 경우 부모 객체 생성
            # ==============================================================================
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ======================================================================================
    # 전역함수 관리 - 필수영역(정적함수)
    # ======================================================================================
    pass
    # ======================================================================================
    # 전역함수 관리 - 필수영역(인스턴스함수)
    # ======================================================================================
    # ——————————————————————————————————————————————————————————————————————————————
    # DataCollect       - [1] 데이터수집(준비)
    # Args              - self       : 객체 인스턴스
    # Return            - bool
    # ——————————————————————————————————————————————————————————————————————————————
    def DataCollect(self) -> bool:
        nChartIndex         = 0                 # Chart Index
        bResult             = False             # 데이터수집 결과

        # oDialogResult       = None              # 파일 열기 다이얼로그 버튼 상태
        df_fish_data        = None              # 원본데이터(도미/빙어)

        sDataFilePath       = 'Data//1.fish_Knnc.csv'

        try:
            # --------------------------------------------------------------
            # 원본데이터(도미/빙어) 초기화
            # --------------------------------------------------------------
            # 데이터 파일 읽기 - 원본데이터(도미/빙어) 길이/무게
            df_fish_data = pd.read_csv(sDataFilePath)

            if df_fish_data.empty == False:
                st.write(f'- 📂 {sDataFilePath} : 원본데이터(도미/빙어) 길이/무게')
                st.write(df_fish_data)

            # 데이터 분리 - 원본데이터(도미/빙어) 길이 분리'
            st.session_state.fish_length_data = df_fish_data['length'].tolist()
            st.session_state.fish_weight_data = df_fish_data['weight'].tolist()

            # --------------------------------------------------------------
            bResult = True
        except Exception as Ex:
            raise Ex                        # 예외 던지기
        
        return bResult
    # ——————————————————————————————————————————————————————————————————————————————
    # DataAnalyze       - [2] 데이터탐색(분석)
    # Args              - self : 객체 인스턴스
    #                   - NewLength : New-Fish 길이
    #                   - NewWeight : New-Fish 무게
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    def DataAnalyze(self, NewLength:int, NewWeight:int) -> None:
        nChartIndex         = 0                 # Chart Index

        try:
            # --------------------------------------------------------------
            # 그래프 환경설정
            # --------------------------------------------------------------
            st.write(f'- 📊 원본데이터(도미/빙어) & New-Fish')

            fig, ax = plt.subplots(1, 2, figsize=(8, 4))

            # pltlib.rcParams['font.family'] = 'Malgun Gothic'    # 'Consolas', 'Malgun Gothic', 'Gulim', 'Dotum', 'batang'
            pltlib.rcParams['font.weight'] = 'normal'           # 'normal', 'bold', 'light', 'ultralight', 'heavy', 'black', 'semibold', 'medium'
            pltlib.rcParams['font.size']   = 6
            pltlib.rcParams['axes.unicode_minus'] = False

            # plt.rc('font', family='Malgun Gothic', size=7) # 윈도우 환경 기준 (맥은 AppleGothic)
            # plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
            # --------------------------------------------------------------
            # 그래프 출력(scatter) - 원본데이터(도미/빙어) & New-Fish -
            # --------------------------------------------------------------
            nChartIndex = 0
            ax[nChartIndex].clear()

            ax[nChartIndex].scatter(st.session_state.fish_length_data[:35],
                                    st.session_state.fish_weight_data[:35],
                                    s=25, alpha=1.0,
                                    label='도미')
            ax[nChartIndex].scatter(st.session_state.fish_length_data[35:],
                                    st.session_state.fish_weight_data[35:],
                                    s=25, alpha=1.0,
                                    label='빙어')
            ax[nChartIndex].scatter(NewLength,
                                    NewWeight,
                                    s=25, alpha=1.0, marker='^',
                                    label=f'[{NewLength},{NewWeight}]')

            ax[nChartIndex].set_title('- 원본데이터(도미/빙어) & New-Fish -', fontsize=7)
            ax[nChartIndex].set_xlabel('길이')
            ax[nChartIndex].set_ylabel('무게')
            ax[nChartIndex].grid(True, alpha=0.3)
            ax[nChartIndex].legend()
            # --------------------------------------------------------------
            # 그래프 출력(scatter) - 원본데이터(도미/빙어) & New-Fish -
            #                      - X축 스케일 마춰서 그래프 출력
            # --------------------------------------------------------------
            nChartIndex = 1
            ax[nChartIndex].clear()

            ax[nChartIndex].scatter(st.session_state.fish_length_data[:35],
                                    st.session_state.fish_weight_data[:35],
                                    s=25, alpha=1.0,
                                    label='도미')
            ax[nChartIndex].scatter(st.session_state.fish_length_data[35:],
                                    st.session_state.fish_weight_data[35:],
                                    s=25, alpha=1.0,
                                    label='빙어')
            ax[nChartIndex].scatter(NewLength,
                                    NewWeight,
                                    s=25, alpha=1.0, marker='^',
                                    label=f'[{NewLength},{NewWeight}]')

            ax[nChartIndex].set_title('- 원본데이터(도미/빙어) & New-Fish -', fontsize=7)
            ax[nChartIndex].set_xlabel('길이')
            ax[nChartIndex].set_ylabel('무게')
            ax[nChartIndex].grid(True, alpha=0.3)
            ax[nChartIndex].legend()
            ax[nChartIndex].set_xlim(0, 1000)
            # --------------------------------------------------------------
            st.pyplot(fig)
            # --------------------------------------------------------------
            st.write(f'- 📊 분석 : 도미/빙어 길이가 길어지면 무게도 늘어남')
            # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # DataPreProcess    - [3] 데이터가공(전처리/검증)
    # Args              - self : 객체 인스턴스
    #                   - NewLength : New-Fish 길이
    #                   - NewWeight : New-Fish 무게
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    def DataPreProcess(self, NewLength:int, NewWeight:int) -> None:
        nChartIndex         = 0                 # Chart Index

        nTrainMean          = 0                 # 학습데이터 평균
        nTrainStd           = 0                 # 학습데이터 표준편차

        try:
            # --------------------------------------------------------------
            # 학습(fit())을 위해 원본데이터(도미/빙어) Numpy 2차원 배열 변환
            # 정답데이터 도미(1)/빙어(0) Numpy 1차원 배열 생성
            # --------------------------------------------------------------
            st.session_state.fish_data = np.column_stack((st.session_state.fish_length_data, st.session_state.fish_weight_data))
            st.session_state.fish_target = np.concatenate((np.ones(35), np.zeros(14)))
            # --------------------------------------------------------------
            # 학습데이터, 검증데이터, 학습용정답, 검증용정답 분할
            # --------------------------------------------------------------
            st.session_state.train_input, st.session_state.val_input, \
            st.session_state.train_target, st.session_state.val_target = \
                sklearn.model_selection.train_test_split(st.session_state.fish_data, st.session_state.fish_target,
                                                         test_size=0.25,
                                                         stratify=st.session_state.fish_target,
                                                         random_state=42)

            st.write(f'- 데이터 분할 : 학습데이터, 검증데이터, 학습용정답, 검증용정답 분할')
            st.write(f'&nbsp;&nbsp;&nbsp;1.test_size : 학습용(75%)/검증용(25%) 분할(기본값=0.25)')
            st.write(f'&nbsp;&nbsp;&nbsp;2.stratify  : 지정하면 샘플링 편향(bias) 억제 = fish_target')
            st.write(f'&nbsp;&nbsp;&nbsp;3.데이터 확인 - 학습데이터', st.session_state.train_input)
            st.write(f'&nbsp;&nbsp;&nbsp;4.데이터 확인 - 검증데이터', st.session_state.val_input)
            st.write(f'&nbsp;&nbsp;&nbsp;5.데이터 확인 - 학습용정답', st.session_state.train_target)
            st.write(f'&nbsp;&nbsp;&nbsp;6.데이터 확인 - 검증용정답', st.session_state.val_target)
            # --------------------------------------------------------------
            # 학습데이터/검증데이터 스케일링 - 길이/무게 스케일 마추기
            # --------------------------------------------------------------
            nTrainMean = np.mean(st.session_state.train_input, axis=0)      # 학습데이터 별 평균(열기준)
            nTrainStd  = np.std(st.session_state.train_input, axis=0)       # 학습데이터 별 표준편차(열기준)

            st.write(f'- 학습데이터/검증데이터 스케일링 - 길이/무게 스케일 마추기')
            st.write(f'&nbsp;&nbsp;&nbsp;1.스케일링 계산 준비 : 학습데이터 별 평균, 학습데이터 별 표준편차')
            st.write(f'&nbsp;&nbsp;&nbsp;2.계산 확인 - 학습데이터 별 평균 : {nTrainMean}')
            st.write(f'&nbsp;&nbsp;&nbsp;3.계산 확인 - 학습데이터 별 표준편차 : {nTrainStd}')

            st.session_state.train_scaled    = (st.session_state.train_input - nTrainMean) / nTrainStd
            st.session_state.val_scaled      = (st.session_state.val_input   - nTrainMean) / nTrainStd
            st.session_state.new_fish_scaled = ([NewLength, NewWeight]       - nTrainMean) / nTrainStd  # New-Fish 스케일링

            st.write(f'- 스케일링 계산 - 학습데이터/검증데이터 별 표준점수 계산')
            st.write(f'&nbsp;&nbsp;&nbsp;1.표준점수(z점수) - 각 특성값이 평균에서 표준편차의 몇배 떨어져 있는지 파악')
            st.write(f'&nbsp;&nbsp;&nbsp;2.학습데이터 표준점수 - (학습데이터 - 평균) / 표준편차')
            st.write(f'&nbsp;&nbsp;&nbsp;3.검증데이터 표준점수 = (검증데이터 - 평균) / 표준편차')
            st.write(f'&nbsp;&nbsp;&nbsp;4.표준점수 확인 - 학습데이터 표준점수', st.session_state.train_scaled)
            st.write(f'&nbsp;&nbsp;&nbsp;5.표준점수 확인 - 검증데이터 표준점수', st.session_state.val_scaled)
            st.write(f'&nbsp;&nbsp;&nbsp;6.표준점수 확인 - New-Fish   표준점수', st.session_state.new_fish_scaled)
            # --------------------------------------------------------------
            # 그래프 환경설정
            # --------------------------------------------------------------
            st.write('- 📊 Scaled 학습데이터 & Scaled New-Fish')

            fig, ax = plt.subplots(1, 1, figsize=(8, 4))

            pltlib.rcParams['font.family'] = 'Malgun Gothic'    # 'Consolas', 'Malgun Gothic', 'Gulim', 'Dotum', 'batang'
            pltlib.rcParams['font.weight'] = 'normal'           # 'normal', 'bold', 'light', 'ultralight', 'heavy', 'black', 'semibold', 'medium'
            pltlib.rcParams['font.size']   = 6
            pltlib.rcParams['axes.unicode_minus'] = False

            # plt.rc('font', family='Malgun Gothic', size=7) # 윈도우 환경 기준 (맥은 AppleGothic)
            # plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
            # --------------------------------------------------------------
            # 그래프 출력(scatter) - Scaled 학습데이터 & Scaled New-Fish -
            # --------------------------------------------------------------
            # nChartIndex = 0
            ax.clear()

            ax.scatter(st.session_state.train_scaled[:, 0],
                                    st.session_state.train_scaled[:, 1],
                                    s=25, alpha=1.0,
                                    label='도미/빙어')
            ax.scatter(st.session_state.new_fish_scaled[0],
                                    st.session_state.new_fish_scaled[1],
                                    s=25, alpha=1.0, marker='^',
                                    label=f'[{NewLength},{NewWeight}]')

            ax.set_title('- Scaled 학습데이터 & Scaled New-Fish -', fontsize=7)
            ax.set_xlabel('길이')
            ax.set_ylabel('무게')
            ax.grid(True, alpha=0.3)
            ax.legend()
            # --------------------------------------------------------------
            st.pyplot(fig)
            # --------------------------------------------------------------
            st.write(f'📊 분석 - 표준점수로 스케일링된 데이터가 그래프에도 정상으로 표현됨')
            # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # DataTrain         - [4] 데이터학습(모델링/학습)
    # Args              - self : 객체 인스턴스
    #                   - Neighbors : 최근접이웃 수
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    def DataTrain(self, Neighbors:int) -> None:
        nChartIndex         = 0                 # Chart Index

        try:
            # --------------------------------------------------------------
            # 모델 생성 및 학습 시키기
            # --------------------------------------------------------------
            st.session_state.knnc = sklearn.neighbors.KNeighborsClassifier(n_neighbors=Neighbors)

            st.session_state.knnc.fit(st.session_state.train_scaled, st.session_state.train_target)

            st.write(f'- 모델 생성 및 학습 시키기')
            st.write(f'&nbsp;&nbsp;&nbsp;1.모델 생성')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Args - n_neighbors={Neighbors} : 예측 시 사용하는 k-최근접이웃의 수(기본값 k=5)')
            st.write(f'&nbsp;&nbsp;&nbsp;3.모델 학습')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Args - X : 학습데이터 반드시 2차원 배열 사용')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Args - Y : 학습용정답 보통   1차원 배열 사용')
            # --------------------------------------------------------------
        except Exception as Ex:
            raise Ex                        # 예외 던지기
    # ——————————————————————————————————————————————————————————————————————————————
    # DataPredict       - [5] 모델링평가(검증/예측)
    # Args              - self : 객체 인스턴스
    #                   - Neighbors : 최근접이웃 수
    #                   - NewLength : New-Fish 길이
    #                   - NewWeight : New-Fish 무게
    # Return            - None
    # ——————————————————————————————————————————————————————————————————————————————
    def DataPredict(self, Neighbors:int, NewLength:int, NewWeight:int) -> None:
        # sTrainStepTitle     = None              # 학습단계 타이틀
        nChartIndex         = 0                 # Chart Index

        # nNewLength          = 0                 # New-Fish 길이
        # nNewWeight          = 0                 # New-Fish 무게

        oNewScaledPredict   = None              # Scaled New-Fish 예측 결과
        oValScaledPredict   = None              # Scaled 검증데이터 예측 결과

        nTrainScore         = 0                 # 학습데이터 정확도
        nValScore           = 0                 # 검증데이터 정확도
        nTrainCrossScore    = 0                 # 학습데이터 교차 검증 정확도
        nValCrossScore      = 0                 # 검증데이터 교차 검증 정확도

        oNewDistances       = None              # New-Fish의 근접한 이웃의 거리
        oNewIndexes         = None              # New-Fish의 근접한 이웃의 색인

        try:
            # --------------------------------------------------------------
            # Scaled New-Fish & Scaled 검증데이터 예측
            # --------------------------------------------------------------
            oNewScaledPredict = st.session_state.knnc.predict([st.session_state.new_fish_scaled])
            oValScaledPredict = st.session_state.knnc.predict(st.session_state.val_scaled)

            # if oNewScaledPredict == 1: self.frmMain.lineKnnNewResult.setText('도미')
            # else:                      self.frmMain.lineKnnNewResult.setText('빙어')

            st.write(f'- Scaled New-Fish & Scaled 검증데이터 예측')
            st.write(f'&nbsp;&nbsp;&nbsp;1.예측 모델 - New-Fish')
            st.write(f'&nbsp;&nbsp;&nbsp;2.예측 모델 - 검증데이터')
            st.write(f'&nbsp;&nbsp;&nbsp;3.정답 확인 - 검증용정답', st.session_state.val_target)
            st.write(f'&nbsp;&nbsp;&nbsp;4.예측 결과 - New-Fish',   oNewScaledPredict)
            st.write(f'&nbsp;&nbsp;&nbsp;5.예측 결과 - 검증데이터', oValScaledPredict)
            st.write(f'&nbsp;&nbsp;&nbsp;6.예측 비교 - val_target == oValScaledPredict',
                     st.session_state.val_target == oValScaledPredict)
            st.write(f'&nbsp;&nbsp;&nbsp;7.예측 비교 결과 - ' + \
                     f'정답수 / 전체수 = {len(oValScaledPredict[st.session_state.val_target == oValScaledPredict])} / {len(st.session_state.val_target)}')
            st.write(f'&nbsp;&nbsp;&nbsp;8.예측 비교 결과 분석 - 분류 모델은 정확한 결과 예측이 가능함')
            # --------------------------------------------------------------
            # KNN 분류 모델 성능 평가 방법
            # --------------------------------------------------------------
            # KNN 분류 모델은 정확한 결과를 예측 가능함
            # k개의 최근접이웃 중 다수결로 클래스 결정
            # 얼마나 올바른 클래스에 분류했는지가 중요
            # --------------------------------------------------------------
            # 1. 정확도(Accuracy) 검증 - 학습정확도 vs 검증정확도 활용
            # --------------------------------------------------------------
            #    - 정상 1                 : 학습정확도(높음) ≈ 검증정확도(높음)
            #                               가장 이상적인 상황
            #                               모델이 학습데이터와 검증데이터 모두에서 잘 작동
            #                               일반화 성능이 좋다
            #
            #    - 정상 2                 : 학습정확도(높음) > 검증정확도(높음)
            #                               가장 일반적인 상황
            #                               모델이 학습데이터에 조금 더 잘 작동
            #                               일반화 성능이 좋다
            #
            #    - 과대적합(Overfitting)  : 학습정확도(높음) > 검증정확도(낮음)
            #                               k 값이 너무 작을 때 (예: k=1) 주로 발생
            #                               모델이 학습데이터의 개별 샘플에 지나치게 민감 해 짐
            #                               학습데이터에서는 정확도가 높지만, 검증데이터에서는 성능이 떨어짐
            #
            #    - 과소적합(Underfitting) : 학습데이터 정확도(낮음) <  검증데이터 정확도(높음)
            #                             : 학습데이터 정확도(낮음) <≈ 검증데이터 정확도(낮음)
            #                             : k 값이 너무 클 때 (예: k=전체 샘플 수)
            #                             : 모델이 학습데이터 패턴을 제대로 학습하지 못한 경우
            #                             : 모든 학습데이터를 평균적으로만 보고 세부적인 패턴을 놓칠 수 있음
            # --------------------------------------------------------------
            # 2.평가 지표(Metrics) 검증
            # --------------------------------------------------------------
            #    - Accuracy(정확도)  : 전체 샘플 중 맞게 분류한 비율
            #                          클래스 불균형에 취약
            #                          기본 성능 평가
            #
            #    - Precision(정밀도) : 모델이 양성이라고 예측한 것 중 실제 양성 비율
            #                          False Positive 줄이는 데 중요
            #                          스팸 필터, 질병 진단
            #
            #    - Recall(재현율)    : 실제 양성 중 모델이 양성이라고 맞춘 비율
            #                          False Negative 줄이는 데 중요
            #                          암 진단, 이상 탐지
            #
            #    - F1-score          : Precision과 Recall의 조화 평균
            #                          두 지표 균형 평가
            #                          Precision/Recall 균형 필요할 때
            #
            #    - ROC-AUC           : 임계값 변화에 따른 성능 평가
            #                          1에 가까울수록 좋은 모델
            # 	                       이진 분류 성능 종합 평가
            # --------------------------------------------------------------
            # 3.교차 검증(Cross-Validation)(기본:5-fold)
            # --------------------------------------------------------------
            #    - 교차 검증 의미
            #      회귀는 데이터 분포에 민감하기 때문에 교차 검증이 특히 중요
            #      데이터셋을 여러 번 나누어 학습/검증을 반복
            #      각 fold(겹)를 번갈아 검증용으로 써서 데이터 편향을 줄임
            #      일반화 성능을 더 정확히 평가하는 방법
            #      k값(이웃수)이 모델의 일반화 성능 또는 데이터셋 특성 때문인지 파악
            #
            #    - 5 Fold란?
            #      데이터셋을 5등분
            #      1회차 : 학습용 - Fold2 ~ 5,   검증용 - Fold1 -> 점수 계산(R²)
            #      2회차 : 학습용 - Fold1,3 ~ 5, 검증용 - Fold2 -> 점수 계산(R²)
            #      ...
            #      5회차 : 학습용 - Fold1 ~ 4,   검증용 - Fold5 -> 점수 계산(R²)
            #
            #    - R²(결정계수) : Fold별 점수
            #      R²는 데이터 분할에서 모델 성능을 평가한 값
            #      R²는 모델이 데이터를 얼마나 잘 설명하는지를 나타내는 지표
            #      Fold 간 점수 차이가 크면 모델이 데이터 분할에 따라 성능이 불안정함을 의미
            #      Fold 간 점수가 비슷하면 모델이 안정적으로 작동한다는 의미
            #      R² = 1 -> 완벽하게 설명
            #      R² = 0 -> 아무 설명 못함 (단순히 평균값 예측과 동일)
            #      R² < 0 -> 모델이 평균값으로만 예측하는 것보다 더 못한 성능을 보임
            #
            #    - 평균 R²(기준선)
            #      전체 Fold 성능의 평균
            #      이 값이 1에 가까우면 모델이 전반적으로 잘 맞춘다는 의미
            #
            #    - 분석 방법
            #      1.Fold별 점수가 모두 1에 가깝고 비슷하면 모델이 안정적이고 신뢰할 수 있음
            #      2.Fold별 점수 차이가 크면 데이터에 따라 성능 편차가 크므로 모델 개선 필요
            #      3.평균 R²(결정계수)가 낮다면 모델이 데이터 패턴을 잘 설명하지 못함
            # --------------------------------------------------------------
            # 1. 정확도(Accuracy) 검증 - 학습정확도 vs 검증정확도 활용
            # --------------------------------------------------------------
            nTrainScore = st.session_state.knnc.score(st.session_state.train_scaled, st.session_state.train_target)
            nValScore   = st.session_state.knnc.score(st.session_state.val_scaled, st.session_state.val_target)

            st.write(f'- 정확도(Accuracy) 검증 - 학습정확도 vs 검증정확도 활용')
            st.write(f'&nbsp;&nbsp;&nbsp;1.정확도 계산 - 학습데이터 정확도 : n_neighbors={Neighbors}, Accuracy={nTrainScore}')
            st.write(f'&nbsp;&nbsp;&nbsp;2.정확도 계산 - 검증데이터 정확도 : n_neighbors={Neighbors}, Accuracy={nValScore}')
            st.write(f'&nbsp;&nbsp;&nbsp;3.정확도 분석')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.학습데이터/검증데이터 정확도 비교')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.정상/과대적합/과소적합 판단')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.과대적합 - n_neighbors값 늘림')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.과소적합 - n_neighbors값 줄임')
            # --------------------------------------------------------------
            # 2.평가 지표(Metrics) 검증 - 검증용정답 vs 검증용예측(평가 지표 활용)
            # --------------------------------------------------------------

            # --------------------------------------------------------------
            # 3.교차 검증(Cross-Validation) - 학습데이터 vs 검증데이터(교차 검증 활용)
            # --------------------------------------------------------------
            nTrainCrossScore = sklearn.model_selection.cross_val_score(st.session_state.knnc,
                                                                       st.session_state.train_scaled,
                                                                       st.session_state.train_target, cv=5)

            nValCrossScore = sklearn.model_selection.cross_val_score(st.session_state.knnc,
                                                                     st.session_state.val_scaled,
                                                                     st.session_state.val_target, cv=5)

            st.write(f'- 교차 검증(Cross-Validation) - 학습데이터 vs 검증데이터(교차 검증 활용)')
            st.write(f'&nbsp;&nbsp;&nbsp;1.교차 검증 - 학습데이터 교차 검증 점수 계산(cross_val_score(...))')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.cv=5(Fold 값) 경우 Fold 별      점수(R²(결정계수))={nTrainCrossScore}')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.cv=5(Fold 값) 경우 Fold 별 평균 점수(평균 R²(기준선))={np.mean(nValCrossScore)}')
            st.write(f'&nbsp;&nbsp;&nbsp;2.교차 검증 분석')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Fold 별 점수가 모두 1에 가깝고 비슷하면 모델이 안정적이고 신뢰할 수 있음')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Fold 별 점수 차이가 크면 데이터에 따라 성능 편차가 크므로 모델 개선 필요')
            st.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.평균 R²가 낮다면 모델이 데이터 패턴을 잘 설명하지 못함')
            # --------------------------------------------------------------
            # 그래프 환경설정
            # --------------------------------------------------------------
            st.write('- 📊 Scaled 학습데이터 & Scaled New-Fish & 이웃')

            fig, ax = plt.subplots(1, 3, figsize=(8, 4))

            pltlib.rcParams['font.family'] = 'Malgun Gothic'    # 'Consolas', 'Malgun Gothic', 'Gulim', 'Dotum', 'batang'
            pltlib.rcParams['font.weight'] = 'normal'           # 'normal', 'bold', 'light', 'ultralight', 'heavy', 'black', 'semibold', 'medium'
            pltlib.rcParams['font.size']   = 6
            pltlib.rcParams['axes.unicode_minus'] = False

            # plt.rc('font', family='Malgun Gothic', size=7) # 윈도우 환경 기준 (맥은 AppleGothic)
            # plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
            # --------------------------------------------------------------
            # 그래프 출력(scatter) - Scaled 학습데이터 & Scaled New-Fish & 이웃 -
            # --------------------------------------------------------------
            oNewDistances, oNewIndexes = st.session_state.knnc.kneighbors([st.session_state.new_fish_scaled])
            # Com.PrintLog('5-17.이웃데이터 준비', 'New-Fish 근접한 이웃의 거리/색인 구하기')
            # Com.PrintLog('5-18.거리 확인 - New-Fish 근접한 이웃의 거리', oNewDistances)
            # Com.PrintLog('5-19.색인 확인 - New-Fish 근접한 이웃의 색인', oNewIndexes)
            # --------------------------------------------------------------
            nChartIndex = 0
            ax[nChartIndex].clear()

            ax[nChartIndex].scatter(st.session_state.train_scaled[:, 0],
                                    st.session_state.train_scaled[:, 1],
                                    s=25, alpha=1.0,
                                    label='도미/빙어')
            ax[nChartIndex].scatter(st.session_state.new_fish_scaled[0],
                                    st.session_state.new_fish_scaled[1],
                                    s=25, alpha=1.0, marker='^',
                                    label=f'[{NewLength}, {NewWeight}]')
            ax[nChartIndex].scatter(st.session_state.train_scaled[oNewIndexes, 0],
                                    st.session_state.train_scaled[oNewIndexes, 1],
                                    s=25, alpha=1.0, marker='D',
                                    label=f'[{NewLength}, {NewWeight}] 이웃데이터')

            ax[nChartIndex].set_title('- Scaled 학습데이터 & Scaled New-Fish & 이웃 -', fontsize=7)
            ax[nChartIndex].set_xlabel('길이')
            ax[nChartIndex].set_ylabel('무게')
            ax[nChartIndex].grid(True, alpha=0.3)
            ax[nChartIndex].legend()
            # Com.PrintLog('5-20.그래프 출력(scatter)', 'Scaled 학습데이터 & Scaled New-Fish & 이웃')
            # --------------------------------------------------------------
            # 그래프 출력(scatter) - Scaled 검증데이터 -
            # --------------------------------------------------------------
            nChartIndex = 1
            ax[nChartIndex].clear()

            ax[nChartIndex].scatter(st.session_state.val_scaled[:, 0],
                                    st.session_state.val_scaled[:, 1],
                                    s=25, alpha=1.0,
                                    label='도미/빙어')

            ax[nChartIndex].set_title('- Scaled 검증데이터 -', fontsize=7)
            ax[nChartIndex].set_xlabel('길이')
            ax[nChartIndex].set_ylabel('무게')
            ax[nChartIndex].grid(True, alpha=0.3)
            ax[nChartIndex].legend()
            # Com.PrintLog('5-21.그래프 출력(scatter)', 'Scaled 검증데이터')
            # --------------------------------------------------------------
            # 그래프 출력(scatter) - 검증용정답 & 예측 결과 비교 -
            # --------------------------------------------------------------
            nChartIndex = 2
            ax[nChartIndex].clear()

            ax[nChartIndex].scatter(np.arange(1, len(st.session_state.val_target)+1),
                                    st.session_state.val_target,
                                    s=35, alpha=1.0, color='blue', # edgecolors='blue', linewidths=1.5,
                                    label='검증용정답')
            ax[nChartIndex].scatter(np.arange(1, len(oValScaledPredict)+1),
                                    oValScaledPredict,
                                    s=5, alpha=1.0, color='red', # edgecolors='red', linewidths=1.5,
                                    label='예측 결과')

            ax[nChartIndex].set_title('- 검증용정답 & 예측 결과 비교 -', fontsize=7)
            ax[nChartIndex].set_xlabel('Fish-Index')
            ax[nChartIndex].set_ylabel('Fish')
            ax[nChartIndex].grid(True, alpha=0.3)
            ax[nChartIndex].legend()
            ax[nChartIndex].set_xticks(np.arange(1, len(st.session_state.val_target)+1))
            ax[nChartIndex].set_yticks([-1, 0, 1, 2], ['', '빙어','도미', ''])
            ax[nChartIndex].set_facecolor('lightgray')
            # Com.PrintLog('5-22.그래프 출력(scatter)', '검증용정답 & 예측 결과 비교')
            # Com.PrintLog('5-23.결론', 'k-최근접이웃분류 모델은 학습데이터와 예측데이터의 스케일링이 필요함')
            # --------------------------------------------------------------
            st.pyplot(fig)
            # --------------------------------------------------------------
            st.write(f'📊 분석 - k-최근접이웃분류 모델은 학습데이터와 예측데이터의 스케일링이 필요함')
            # --------------------------------------------------------------
            # self.TrainComplete = True
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
