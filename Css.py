# ══════════════════════════════════════════════════════════════════════════════════════════
# CSS 영역
# ══════════════════════════════════════════════════════════════════════════════════════════
# ======================================================================================
# Main Expander/Container CSS 관리
# ======================================================================================
# --------------------------------------------------------------
# Main Expander CSS
# --------------------------------------------------------------
ExpMainStyle = \
    '''
        <style>
            .st-key-expPrintString  summary p,
            .st-key-expInputText    summary p,
            .st-key-expInputTextNum summary p,
            .st-key-expMakeTabs     summary p,
            .st-key-expGugudan      summary p,
            .st-key-expKnnc         summary p
            {
                font-family: consolas;          /* 글자 */
                font-size: 24px;                /* 글자 크기 */
                font-weight: normal;            /* 굵게 */
                color: cyan;                    /* 글자 색상 */
            }
        </style>
    '''
# --------------------------------------------------------------
# Tab Container CSS
# --------------------------------------------------------------
ContTabStyle = \
    '''
        <style>
            .st-key-contTabMain * {
                font-size: 24px;                /* 글자 크기 */
                font-weight: bold;              /* 굵게 */
                color: orange;                  /* 글자 색상 */
            }
            .st-key-contTab-1 * {
                font-size: 24px;                /* 글자 크기 */
                font-weight: bold;              /* 굵게 */
                color: green;                   /* 글자 색상 */
            }
            .st-key-contTab-2 * {
                font-size: 24px;                /* 글자 크기 */
                font-weight: bold;              /* 굵게 */
                color: yellow;                  /* 글자 색상 */
            }
            .st-key-contTab-3 * {
                font-size: 24px;                /* 글자 크기 */
                font-weight: bold;              /* 굵게 */
                color: brown;                   /* 글자 색상 */
            }
            .st-key-contTabCommon * {
                font-size: 24px;                /* 글자 크기 */
                font-weight: bold;              /* 굵게 */
                color: lime;                    /* 글자 색상 */
            }
        </style>
    '''
# ======================================================================================
# 고급 구구단 Container CSS 관리
# ======================================================================================
# --------------------------------------------------------------
# Gugudan Scroll Container CSS
# --------------------------------------------------------------
ContGugudanScrollStyle = \
    '''
        <style>
            .st-key-contGugudanTopScroll *,
            .st-key-contGugudanBottomScroll * {
                border: none;                   /* 테두리 박스 숨기기 */
            }
            .st-key-contGugudanTopScroll > div,
            .st-key-contGugudanBottomScroll > div {
                max-height: 650px;              /* 원하는 고정 높이 지정 (예: 250픽셀) */
                max-width: 100%;                /* 원하는 고정 넓이 지정 (max-content: 내용기준) */
                overflow-y: auto;               /* 내용이 넘치면 세로 스크롤바 자동 생성 */
                overflow-x: auto;               /* 내용이 넘치면 가로 스크롤바 자동 생성 */
            }
            .st-key-contGugudanTopScroll p,
            .st-key-contGugudanBottomScroll p {
                white-space: nowrap;            /* 줄바꿈 금지 */
            }
            .st-key-contGugudanTopScroll pre,
            .st-key-contGugudanTopScroll span,
            .st-key-contGugudanBottomScroll pre,
            .st-key-contGugudanBottomScroll span {
                white-space: pre;               /* pre는 \n 일때 다음줄, 그 외에는 내려쓰기 않함 */
            }
        </style>
    '''
# --------------------------------------------------------------
# Gugudan Print Container CSS
# --------------------------------------------------------------
ContGugudanPrintStyle = \
    '''
        <style>
            .st-key-contGugudanPrintSlow * {
                font-family: Consolas;          /* 글자 */
                font-weight: bold;              /* 굵게 */
                color: orange;                  /* 글자 색상 */
            }
            .st-key-contGugudanPrintFast * {
                font-family: Consolas;          /* 글자 */
                font-weight: bold;              /* 굵게 */
                color: yellow;                  /* 글자 색상 */
            }
            .st-key-contGugudanPrintFile * {
                font-family: Consolas;          /* 글자 */
                font-weight: bold;              /* 굵게 */
                color: green;                   /* 글자 색상 */
            }
        </style>
    '''
# ======================================================================================
# k-최근접이웃분류(k-Nearest Neighbors Classification) Container CSS 관리
# ======================================================================================
# --------------------------------------------------------------
# Gugudan Scroll Container CSS
# --------------------------------------------------------------
ContKnncStyle = \
    '''
        <style>
            .st-key-contDataCollect *,
            .st-key-contDataAnalyze *,
            .st-key-contDataPreProcess *,
            .st-key-contDataTrain *,
            .st-key-contDataPredict * {
                font-family: Consolas;          /* 글자 */
                font-weight: normal;            /* 굵게 */
                color: orange;                  /* 글자 색상 */
            }
        </style>
    '''
# ══════════════════════════════════════════════════════════════════════════════════════════
# <END>
# ══════════════════════════════════════════════════════════════════════════════════════════
