import streamlit as st

# 1. 스트림릿 페이지 설정
st.set_page_config(
    page_title="GLP 4조 | 가치소비 가이드북",
    page_icon="🌱",
    layout="wide"
)

# 2. HTML 및 차트 로직 정의
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            padding: 0;
            font-family: 'Lato', sans-serif;
            background-color: #f8fafc;
            color: #334155;
        }

        /* 공통 섹션 스타일 */
        .section-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 80px 20px;
        }

        .accent-color { color: #166534; }
        .bg-accent { background-color: #166534; }

        /* 헤더 디자인 */
        header {
            background: white;
            border-bottom: 1px solid #e2e8f0;
            padding: 20px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-content {
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }

        .logo { font-size: 24px; font-weight: 700; color: #166534; font-family: 'Poppins'; }

        /* 메인 비주얼 */
        .hero { text-align: center; padding: 100px 20px; background-color: #f1f5f9; }
        .hero h1 { font-size: 56px; margin-bottom: 20px; font-family: 'Poppins'; color: #0f172a; }
        .hero p { font-size: 20px; color: #64748b; max-width: 700px; margin: 0 auto 40px; }

        /* 설문 결과 그래프 레이아웃 */
        .chart-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-top: 50px;
        }

        .chart-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            text-align: center;
        }

        .chart-card h3 {
            font-size: 20px;
            margin-bottom: 30px;
            color: #1e293b;
            font-family: 'Poppins';
        }

        /* 실제 막대 그래프 구현 */
        .bar-container {
            display: flex;
            align-items: flex-end;
            justify-content: space-around;
            height: 250px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
        }

        .bar-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 60px;
        }

        .bar {
            width: 100%;
            background: linear-gradient(to top, #166534, #22c55e);
            border-radius: 8px 8px 0 0;
            transition: height 1s ease-in-out;
            position: relative;
        }

        .bar-value {
            position: absolute;
            top: -25px;
            font-weight: 700;
            font-size: 14px;
            color: #166534;
        }

        .bar-label {
            margin-top: 15px;
            font-size: 14px;
            font-weight: 500;
            color: #64748b;
        }

        /* 플리마켓 리스트 */
        .flea-market-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        .market-item {
            background: #fff;
            padding: 25px;
            border-left: 5px solid #166534;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        /* 앱 홍보 섹션 */
        .app-section {
            background: #0f172a;
            color: white;
            border-radius: 30px;
            padding: 60px;
            display: flex;
            align-items: center;
            gap: 50px;
            margin-top: 50px;
        }

        .app-text { flex: 1; }
        .app-preview { flex: 1; text-align: center; }
        .app-btn {
            display: inline-block;
            background: #22c55e;
            color: #0f172a;
            padding: 15px 30px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            margin-top: 20px;
        }

    </style>
</head>
<body>

    <header>
        <div class="header-content">
            <div class="logo">🌿 GLP 4조</div>
            <div style="font-size: 14px; color: #64748b; font-weight: 500;">지속가능한 생산과 소비를 위한 가이드</div>
        </div>
    </header>

    <section class="hero">
        <div class="section-container">
            <h1>다시 쓰는 순간, <span class="accent-color">가치</span>가 된다</h1>
            <p>우리의 소비 습관을 돌아보고, 더 나은 미래를 위해 일상을 기록하는 습관. GLP 4조와 MANUS가 함께합니다.</p>
        </div>
    </section>

    <section class="section-container" id="survey">
        <div style="text-align: center; margin-bottom: 60px;">
            <h2 style="font-size: 32px; font-family: 'Poppins';">📊 설문 결과 분석</h2>
            <p style="color: #64748b;">우리가 가장 많이 소비하는 분야와 장소는 어디일까요?</p>
        </div>

        <div class="chart-grid">
            <div class="chart-card">
                <h3>가장 많이 소비한 분야는?</h3>
                <div class="bar-container">
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 65%;">
                            <span class="bar-value">65%</span>
                        </div>
                        <span class="bar-label">음식</span>
                    </div>
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 25%; opacity: 0.7;">
                            <span class="bar-value">25%</span>
                        </div>
                        <span class="bar-label">여가</span>
                    </div>
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 12%; opacity: 0.5;">
                            <span class="bar-value">12%</span>
                        </div>
                        <span class="bar-label">의류</span>
                    </div>
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 5%; opacity: 0.3;">
                            <span class="bar-value">5%</span>
                        </div>
                        <span class="bar-label">교육</span>
                    </div>
                </div>
            </div>

            <div class="chart-card">
                <h3>가장 많이 소비한 장소는?</h3>
                <div class="bar-container">
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 58%;">
                            <span class="bar-value">58%</span>
                        </div>
                        <span class="bar-label">백마</span>
                    </div>
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 42%; opacity: 0.7;">
                            <span class="bar-value">42%</span>
                        </div>
                        <span class="bar-label">마두</span>
                    </div>
                    <div class="bar-wrapper">
                        <div class="bar" style="height: 22%; opacity: 0.4;">
                            <span class="bar-value">22%</span>
                        </div>
                        <span class="bar-label">집 동네</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-container" id="flea-market">
        <h2 style="font-size: 28px; font-family: 'Poppins'; margin-bottom: 30px;">📍 지역 플리마켓 가이드</h2>
        <div class="flea-market-grid">
            <div class="market-item">
                <h4 style="margin: 0; font-size: 18px;">가정의 달 플리마켓</h4>
                <p style="font-size: 14px; color: #64748b; margin-top: 8px;">백마교회 옆 공원 | 5월 5일 ~ 15일</p>
                <p style="font-size: 13px; margin-top: 10px;">핸드메이드 소품, 어린이 장난감, 중고책 나눔</p>
            </div>
            <div class="market-item">
                <h4 style="margin: 0; font-size: 18px;">청년 센터 플리마켓</h4>
                <p style="font-size: 14px; color: #64748b; margin-top: 8px;">마두역 사거리 | 6월 15일 ~ 17일</p>
                <p style="font-size: 13px; margin-top: 10px;">빈티지 의류, 중고책, CD/LP 컬렉션</p>
            </div>
        </div>
    </section>

    <section class="section-container">
        <div class="app-section">
            <div class="app-text">
                <h2 style="font-size: 36px; margin-bottom: 20px;">기록의 힘, MANUS</h2>
                <p style="color: #cbd5e1; line-height: 1.6;">
                    여러분이 실천한 가치 있는 소비와 일상의 순간들을 놓치지 마세요. <br>
                    <strong>MANUS 앱</strong>을 통해 플리마켓 방문 기록, 업사이클 제품 구매 기록을 나만의 특별한 타임라인으로 만들 수 있습니다.
                </p>
                <a href="https://manus.im/app-preview/i7zPuB3unvW8Ks9MGw6dVT?sessionId=bjA7pGHJXXQ7LHfXgBiYgW" class="app-btn" target="_blank">
                    <i class="fa-solid fa-mobile-screen-button"></i> 앱에서 시작하기
                </a>
            </div>
            <div class="app-preview">
                <div style="background: #1e293b; width: 220px; height: 400px; border-radius: 30px; margin: 0 auto; border: 5px solid #334155; padding: 20px;">
                    <div style="width: 50px; height: 5px; background: #334155; border-radius: 10px; margin: 0 auto 30px;"></div>
                    <div style="text-align: left;">
                        <div style="width: 100%; height: 10px; background: #22c55e; margin-bottom: 10px; border-radius: 5px;"></div>
                        <div style="width: 80%; height: 10px; background: #475569; margin-bottom: 20px; border-radius: 5px;"></div>
                        <div style="width: 100%; height: 100px; background: #334155; border-radius: 10px;"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer style="text-align: center; padding: 60px 0; color: #94a3b8; font-size: 13px; border-top: 1px solid #e2e8f0;">
        <p>© 2026 GLP 4조 Project. All rights reserved.</p>
    </footer>

</body>
</html>
"""

# 3. 컴포넌트 렌더링 (높이는 내용에 맞춰 충분히 2600으로 설정)
st.components.v1.html(html_code, height=2600, scrolling=True)
