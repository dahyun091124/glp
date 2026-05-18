import streamlit as st

# 1. 스트림릿 페이지 설정 (브라우저 탭 이름 및 아이콘)
st.set_page_config(
    page_title="GLP 2조 | 소비 가이드북 & MANUS",
    page_icon="🌱",
    layout="wide"
)

# 2. HTML 콘텐츠 정의
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
        body {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: #fcfbf7;
        }
        .accent-color { color: #b85a38; }
        .bg-accent { background-color: #b85a38; }
    </style>
</head>
<body class="text-gray-800">

    <header class="sticky top-0 bg-white border-b border-gray-100 z-50 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="font-bold text-xl tracking-wider accent-color flex items-center gap-2">
                <span>🌱</span> GLP 2조
            </div>
            <nav class="hidden md:flex space-x-8 font-medium text-sm">
                <a href="#intro" class="hover:text-amber-700 transition">소개</a>
                <a href="#survey" class="hover:text-amber-700 transition">소비 분석</a>
                <a href="#fleamarket" class="hover:text-amber-700 transition">플리마켓 지도</a>
                <a href="#brands" class="hover:text-amber-700 transition">가치소비 브랜드</a>
                <a href="#manus-app" class="hover:text-amber-700 transition">MANUS 앱</a>
            </nav>
            <a href="https://manus.im/app-preview/i7zPuB3unvW8Ks9MGw6dVT?sessionId=bjA7pGHJXXQ7LHfXgBiYgW" target="_blank" class="bg-accent text-white px-4 py-2 rounded-full text-xs font-semibold hover:bg-amber-800 transition">
                앱 다운로드
            </a>
        </div>
    </header>

    <section id="intro" class="max-w-6xl mx-auto px-4 py-16 text-center">
        <span class="text-xs font-bold uppercase tracking-widest bg-yellow-100 text-amber-800 px-3 py-1 rounded-full">소비 가이드북 : 특별편</span>
        <h1 class="text-4xl md:text-5xl font-bold mt-4 mb-2 tracking-tight">다시 쓰는 순간, <span class="accent-color">가치</span>가 된다</h1>
        <p class="text-gray-500 max-w-xl mx-auto text-sm md:text-base mt-2">
            SDGs 12번 '지속가능한 생산과 소비'를 위해 GLP 2조가 제안하는 올바른 소비 가이드와 일상 기록 솔루션.
        </p>
        <div class="mt-8 flex justify-center space-x-4">
            <a href="#brands" class="border border-gray-300 px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-gray-50 transition">브랜드 보러가기</a>
            <a href="#manus-app" class="bg-accent text-white px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-amber-800 transition shadow-lg">MANUS 만나기</a>
        </div>
    </section>

    <hr class="max-w-6xl mx-auto border-gray-200">

    <section id="survey" class="max-w-6xl mx-auto px-4 py-16">
        <div class="text-center mb-12">
            <h2 class="text-2xl font-bold">📊 설문 결과 분석</h2>
            <p class="text-gray-500 text-sm mt-1">우리가 가장 많이 소비하는 분야와 장소는 어디일까요?</p>
        </div>
        <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
            <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col items-center">
                <h3 class="font-bold text-gray-700 mb-6 text-sm">가장 많이 소비한 분야는?</h3>
                <div class="flex items-end space-x-6 h-48 w-full justify-center px-4 border-b border-gray-200">
                    <div class="flex flex-col items-center w-12"><div class="bg-accent w-full rounded-t" style="height: 65%;"></div><span class="text-xs mt-2 font-medium">음식</span></div>
                    <div class="flex flex-col items-center w-12"><div class="bg-yellow-600 w-full rounded-t" style="height: 25%;"></div><span class="text-xs mt-2 font-medium">여가</span></div>
                    <div class="flex flex-col items-center w-12"><div class="bg-yellow-500 w-full rounded-t" style="height: 12%;"></div><span class="text-xs mt-2 font-medium">의류</span></div>
                    <div class="flex flex-col items-center w-12"><div class="bg-yellow-300 w-full rounded-t" style="height: 5%;"></div><span class="text-xs mt-2 font-medium">교육</span></div>
                </div>
            </div>
            <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col items-center">
                <h3 class="font-bold text-gray-700 mb-6 text-sm">가장 많이 소비한 장소는?</h3>
                <div class="flex items-end space-x-6 h-48 w-full justify-center px-4 border-b border-gray-200">
                    <div class="flex flex-col items-center w-12"><div class="bg-accent w-full rounded-t" style="height: 58%;"></div><span class="text-xs mt-2 font-medium">백마</span></div>
                    <div class="flex flex-col items-center w-12"><div class="bg-yellow-600 w-full rounded-t" style="height: 42%;"></div><span class="text-xs mt-2 font-medium">마두</span></div>
                    <div class="flex flex-col items-center w-12"><div class="bg-yellow-400 w-full rounded-t" style="height: 22%;"></div><span class="text-xs mt-2 font-medium">집 동네</span></div>
                </div>
            </div>
        </div>
    </section>

    <section id="fleamarket" class="bg-gray-100 py-16">
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-2xl font-bold">📍 지역 플리마켓 지도</h2>
                <p class="text-gray-500 text-sm mt-1">우리 동네에서 열리는 가치 있는 중고 나눔의 장</p>
            </div>
            <div class="grid md:grid-cols-2 gap-8 items-center max-w-4xl mx-auto">
                <div class="bg-yellow-50 p-6 rounded-2xl border border-yellow-200 flex items-center justify-center min-h-[250px]">
                    <div class="text-center">
                        <span class="text-4xl">🗺️</span>
                        <p class="text-xs text-gray-400 mt-2">고양시 플리마켓 지도 정보</p>
                    </div>
                </div>
                <div class="space-y-6">
                    <div class="bg-white p-5 rounded-xl border border-gray-100 shadow-sm">
                        <span class="bg-accent text-white text-[10px] px-2 py-0.5 rounded font-bold">1</span>
                        <h3 class="font-bold text-base mt-2">가정의 달 플리마켓 in 고양</h3>
                        <p class="text-xs text-gray-500 mt-2"><b>위치:</b> 백마교회 옆 공원</p>
                        <p class="text-xs text-gray-500"><b>날짜:</b> 2026년 5월 5일 ~ 15일</p>
                        <p class="text-xs text-gray-600 mt-1"><b>품목:</b> 핸드메이드 소품, 어린이 장난감, 중고책</p>
                    </div>
                    <div class="bg-white p-5 rounded-xl border border-gray-100 shadow-sm">
                        <span class="bg-yellow-700 text-white text-[10px] px-2 py-0.5 rounded font-bold">2</span>
                        <h3 class="font-bold text-base mt-2">고양시청년센터 청년 플리마켓</h3>
                        <p class="text-xs text-gray-500 mt-2"><b>위치:</b> 마두역 사거리</p>
                        <p class="text-xs text-gray-500"><b>날짜:</b> 2026년 6월 15일 ~ 17일</p>
                        <p class="text-xs text-gray-600 mt-1"><b>품목:</b> 빈티지 의류, 중고책, CD, LP 등</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="brands" class="max-w-6xl mx-auto px-4 py-16">
        <div class="text-center mb-12">
            <h2 class="text-2xl font-bold">💡 어떻게 실천하지?</h2>
            <p class="text-gray-500 text-sm mt-1">윤리적 소비와 친환경을 실천하는 멋진 브랜드들</p>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col justify-between">
                <div>
                    <h3 class="text-xs font-bold text-amber-800 tracking-wider mb-4">윤리 & 친환경</h3>
                    <div class="mb-6">
                        <h4 class="font-bold text-base">3. 119REO (110레오)</h4>
                        <p class="text-xs text-gray-600 mt-2" style="line-height: 1.6;">폐방화복을 활용해 가방과 액세서리를 제작하고, 그 수익금을 통해 암 투병 소방관을 지원하는 사회적 기업입니다.</p>
                    </div>
                    <div class="border-t border-dashed my-4"></div>
                    <div>
                        <h4 class="font-bold text-base">4. 노플라스틱선데이</h4>
                        <p class="text-xs text-gray-600 mt-2" style="line-height: 1.6;">버려지는 플라스틱을 수거해 생활용품으로 재탄생시키는 업사이클링 브랜드입니다.</p>
                    </div>
                </div>
                <div class="mt-6 text-2xl text-right">🎒♻️</div>
            </div>
            <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col justify-between">
                <div>
                    <h3 class="text-xs font-bold text-amber-800 tracking-wider mb-4">윤리적 가치</h3>
                    <div class="mb-6">
                        <h4 class="font-bold text-base">1. LUSH (러쉬)</h4>
                        <p class="text-xs text-gray-600 mt-2" style="line-height: 1.6;">자연에서 얻은 신선한 재료와 동물 실험을 하지 않는 정직한 재료를 사용하여 모든 제품을 손으로 만듭니다. 성분의 90%는 식물성 원료인 비건입니다.</p>
                    </div>
                    <div class="border-t border-dashed my-4"></div>
                    <div>
                        <h4 class="font-bold text-base">2. 신이어마쾍</h4>
                        <p class="text-xs text-gray-600 mt-2" style="line-height: 1.6;">폐지 수거 노인을 넘어 일하고 싶은 시니어까지 즐겁고 따뜻한 일자리로 청년과 노년이 함께 일하는 브랜드입니다.</p>
                    </div>
                </div>
                <div class="mt-6 text-2xl text-right">🐰👵</div>
            </div>
            <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm flex flex-col justify-between">
                <div>
                    <h3 class="text-xs font-bold text-amber-800 tracking-wider mb-4">친환경 실천</h3>
                    <div class="mb-6">
                        <h4 class="font-bold text-base">1. 리필 스테이션</h4>
                        <p class="text-xs text-gray-600 mt-2" style="line-height: 1.6;">용기를 재사용하여 세제, 샴푸, 화장품 등의 내용물만 소분 구매하는 친환경 매장 (예: 아모레퍼시픽, 아로마티카)</p>
                    </div>
                    <div class="border-t border-dashed my-4"></div>
                    <div>
                        <h4 class="font-bold text-base">2. 플리츠 마마</h4>
                        <p class="text-xs text-gray-600 mt-2" style="line-height: 1.6;">페트병 리사이클 원사로 니트 가방을 제작하는 국내 친환경 패션 브랜드입니다.</p>
                    </div>
                </div>
                <div class="mt-6 text-2xl text-right">🧴👜</div>
            </div>
        </div>
    </section>

    <section id="manus-app" class="bg-gray-900 text-white py-20">
        <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12 items-center">
            <div class="space-y-6">
                <span class="text-xs font-bold uppercase tracking-widest bg-yellow-500 text-neutral-900 px-3 py-1 rounded-full">Next-Gen Lifestyle App</span>
                <h2 class="text-3xl md:text-4xl font-bold tracking-tight mt-4">
                    나의 가치 소비와 일상을<br>
                    <span class="text-yellow-400">MANUS</span> 에 기록하세요
                </h2>
                <p class="text-gray-400 text-sm md:text-base mt-2">
                    브로셔에서 확인한 지속 가능한 가치들, 매번 기억하기 어려우셨나요? <br>
                    <strong>MANUS(마누스)</strong> 앱을 이용해 여러분이 실천한 친환경 리필, 플리마켓 방문, 업사이클 브랜드 소비 기록을 나만의 특별한 아카이브로 남겨보세요.
                </p>
                <div class="pt-4">
                    <a href="https://manus.im/app-preview/i7zPuB3unvW8Ks9MGw6dVT?sessionId=bjA7pGHJXXQ7LHfXgBiYgW" target="_blank" class="inline-block bg-yellow-500 text-gray-900 px-6 py-3 rounded-xl font-bold text-sm hover:bg-yellow-400 transition shadow-lg">
                        📱 MANUS 앱 미리보기 / 다운로드
                    </a>
                </div>
            </div>
            <div class="flex justify-center">
                <div class="bg-gray-800 w-64 h-96 rounded-3xl border-4 border-gray-700 shadow-2xl flex flex-col justify-between p-6 text-center">
                    <div class="w-16 h-3 bg-gray-700 rounded-full mx-auto"></div>
                    <div class="space-y-3 my-auto">
                        <span class="text-4xl block">✨</span>
                        <h4 class="font-bold text-lg text-white">MANUS</h4>
                        <p class="text-xs text-gray-400 px-2">당신의 가치 있는 하루를 한눈에 정리하는 스마트 라이프 앱</p>
                    </div>
                    <div class="bg-gray-700 text-xs py-1.5 px-4 rounded-full text-yellow-300 font-medium">지금 시작하기</div>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-gray-950 text-gray-500 text-xs py-8 border-t border-gray-900">
        <div class="max-w-6xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
            <div>
                <p class="font-medium text-gray-400">GLP 2조 | 지속 가능한 소비 프로젝트</p>
                <p class="mt-1">본 페이지는 브로셔 배포 및 가치 실천 확산을 위해 제작되었습니다.</p>
            </div>
            <div class="flex space-x-4">
                <a href="https://manus.im" target="_blank" class="hover:underline">Manus 공식 홈</a>
            </div>
        </div>
    </footer>

</body>
</html>
"""

# 3. 스트림릿 컴포넌트로 HTML 렌더링 (스크롤바 없이 꽉 차게 띄우기)
st.components.v1.html(html_code, height=2200, scroller=True)
