import streamlit as st
import pandas as pd
import altair as alt

# 1. 스트림릿 페이지 설정
st.set_page_config(
    page_title="GLP 4조 | 가치소비 가이드북",
    page_icon="🌱",
    layout="wide"
)

# --- 2. 실제 데이터로 막대 그래프 그리기 (스트림릿 네이티브 차트) ---
st.title("🌿 GLP 4조 | 소비 가이드북 : 특별편")
st.caption("지속가능한 생산과 소비를 위한 가이드")
st.markdown("---")

st.header("📊 설문 결과 분석")
st.subheader("우리가 가장 많이 소비하는 분야와 장소는 어디일까요?")

# 차트용 컬럼 배치
col1, col2 = st.columns(2)

with col1:
    st.write("### 가장 많이 소비한 분야는?")
    # 실제 데이터셋 생성
    category_data = pd.DataFrame({
        '분야': ['음식', '여가활동', '의류', '교육'],
        '비율 (%)': [65, 25, 12, 5]
    })
    # Altair를 이용한 세련된 막대 그래프 정의
    chart1 = alt.Chart(category_data).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8, color='#166534').encode(
        x=alt.X('분야:N', sort=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y('비율 (%):Q', scale=alt.Scale(domain=[0, 80])),
        tooltip=['분야', '비율 (%)']
    ).properties(height=350)
    
    st.altair_chart(chart1, use_container_width=True)

with col2:
    st.write("### 가장 많이 소비한 장소는?")
    place_data = pd.DataFrame({
        '장소': ['백마', '마두', '집 동네'],
        '비율 (%)': [58, 42, 22]
    })
    chart2 = alt.Chart(place_data).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8, color='#15803d').encode(
        x=alt.X('장소:N', sort=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y('비율 (%):Q', scale=alt.Scale(domain=[0, 80])),
        tooltip=['장소', '비율 (%)']
    ).properties(height=350)
    
    st.altair_chart(chart2, use_container_width=True)


# --- 3. 하단 콘텐츠 및 MANUS 연동 (HTML 컴포넌트 처리) ---
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
        body {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: #fcfbf7;
        }
        .accent-color { color: #166534; }
        .bg-accent { background-color: #166534; }
        .market-card:hover { transform: translateY(-4px); transition: all 0.2s ease; }
    </style>
</head>
<body class="text-gray-800">

    <section class="max-w-6xl mx-auto px-4 py-12">
        <h2 class="text-2xl font-bold mb-2 flex items-center gap-2">
            <span class="accent-color">📍</span> 지역 플리마켓 가이드
        </h2>
        <p class="text-sm text-gray-500 mb-8">위치를 클릭하면 실제 지도 화면으로 연결되어 길을 찾을 수 있습니다.</p>
        
        <div class="grid md:grid-cols-2 gap-6">
            <div class="market-card bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col justify-between">
                <div>
                    <span class="bg-green-100 text-green-800 text-xs px-2.5 py-1 rounded-full font-bold">진행 예정</span>
                    <h3 class="font-bold text-xl mt-3 text-gray-900">가정의 달 플리마켓 in 고양</h3>
                    <p class="text-sm text-gray-600 mt-2"><b>날짜:</b> 2026년 5월 5일 ~ 15일</p>
                    <p class="text-sm text-gray-600"><b>품목:</b> 핸드메이드 소품, 어린이 장난감, 중고책</p>
                </div>
                <div class="mt-6 pt-4 border-t border-gray-100">
                    <a href="https://map.naver.com/v5/search/%EB%B0%B1%EB%A7%88%EA%B5%90%ED%9A%8C" target="_blank" class="inline-flex items-center gap-2 text-sm font-semibold text-green-700 hover:text-green-900">
                        <i class="fa-solid fa-map-location-dot"></i> 위치: 백마교회 옆 공원 (지도 보기) →
                    </a>
                </div>
            </div>

            <div class="market-card bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col justify-between">
                <div>
                    <span class="bg-green-100 text-green-800 text-xs px-2.5 py-1 rounded-full font-bold">진행 예정</span>
                    <h3 class="font-bold text-xl mt-3 text-gray-900">고양시청년센터 청년 플리마켓</h3>
                    <p class="text-sm text-gray-600 mt-2"><b>날짜:</b> 2026년 6월 15일 ~ 17일</p>
                    <p class="text-sm text-gray-600"><b>품목:</b> 빈티지 의류, 중고책, CD, LP 등</p>
                </div>
                <div class="mt-6 pt-4 border-t border-gray-100">
                    <a href="https://map.naver.com/v5/search/%EB%A7%88%EB%91%90%EC%97%AD" target="_blank" class="inline-flex items-center gap-2 text-sm font-semibold text-green-700 hover:text-green-900">
                        <i class="fa-solid fa-map-location-dot"></i> 위치: 마두역 사거리 (지도 보기) →
                    </a>
                </div>
            </div>
        </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 py-8">
        <div class="bg-gray-900 text-white rounded-3xl p-8 md:p-12 grid md:grid-cols-2 gap-8 items-center shadow-xl">
            <div class="space-y-4">
                <span class="text-xs font-bold uppercase tracking-widest bg-green-500 text-neutral-900 px-3 py-1 rounded-full">Next-Gen Lifestyle App</span>
                <h2 class="text-2xl md:text-3xl font-bold tracking-tight">
                    나의 가치 소비와 일상을<br>
                    <span class="text-green-400">MANUS</span> 에 기록하세요
                </h2>
                <p class="text-gray-400 text-sm leading-relaxed">
                    브로셔에서 확인한 지속 가능한 가치들, 매번 기억하기 어려우셨나요? <br>
                    <strong>MANUS(마누스)</strong> 앱을 이용해 여러분이 실천한 친환경 리필, 플리마켓 방문, 업사이클 브랜드 소비 기록을 나만의 특별한 아카이브로 남겨보세요.
                </p>
                <div class="pt-2">
                    <a href="https://manus.im/app-preview/i7zPuB3unvW8Ks9MGw6dVT?sessionId=bjA7pGHJXXQ7LHfXgBiYgW" target="_blank" class="inline-flex items-center gap-2 bg-green-600 text-white px-5 py-3 rounded-xl font-bold text-xs hover:bg-green-500 transition shadow-lg">
                        📱 MANUS 앱 미리보기 / 다운로드
                    </a>
                </div>
            </div>
            <div class="flex justify-center">
                <div class="bg-gray-800 w-56 h-80 rounded-2xl border-4 border-gray-700 shadow-2xl flex flex-col justify-between p-5 text-center">
                    <div class="w-12 h-2.5 bg-gray-700 rounded-full mx-auto"></div>
                    <div class="space-y-2 my-auto">
                        <span class="text-3xl block">✨</span>
                        <h4 class="font-bold text-base text-white">MANUS</h4>
                        <p class="text-[11px] text-gray-400 px-1">당신의 가치 있는 하루를 한눈에 정리하는 스마트 라이프 앱</p>
                    </div>
                    <div class="bg-gray-700 text-[11px] py-1 px-3 rounded-full text-green-300 font-medium">지금 시작하기</div>
                </div>
            </div>
        </div>
    </section>

    <footer class="max-w-6xl mx-auto px-4 py-8 text-center text-gray-400 text-xs border-t border-gray-100 mt-12">
        <p>© 2026 GLP 4조 Project. All rights reserved.</p>
    </footer>

</body>
</html>
"""

# HTML 컴포넌트 호출
st.components.v1.html(html_code, height=1200, scrolling=True)
