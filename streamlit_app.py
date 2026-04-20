import streamlit as st

st.set_page_config(page_title="학교 자판기 스마트 매니저", layout="wide")
st.title("🥤 학교 자판기 스마트 매니저")

col1, col2 = st.columns(2)

with col1:
    st.header("💰 용돈 관리 계산기")
    allowance = st.number_input("이번 주 총 용돈 (원)", min_value=0, value=30000, step=1000)
    
    # 1. 예산 설정 (최대치를 제한)
    ratio = st.slider("용돈 중 자판기 예산 비중 (%)", 0, 100, 10)
    budget = allowance * (ratio / 100)
    
    # 2. 횟수 계산
    avg_price = 1000
    raw_count = int(budget / avg_price) if avg_price > 0 else 0
    
    # 3. 🚨 건강 가이드라인 적용 (핵심 수정 부분)
    # 일주일에 5번(평일 1일 1회)을 '건강 적정선'으로 가정
    health_limit = 5 
    
    st.info(f"이번 주 자판기 예산: **{budget:,.0f}원**")
    
    if raw_count > health_limit:
        st.warning(f"계산상으로는 {raw_count}번 마실 수 있지만, 건강을 위해 주 {health_limit}회 이하를 권장해요!")
        final_count = health_limit
    else:
        final_count = raw_count

    st.success(f"이번 주 추천 횟수: **{final_count}회**")
    
    # 시각적 피드백
    if final_count >= 5:
        st.error("⚠️ 당분 섭취가 많을 수 있어요! 물을 더 마셔보는 건 어떨까요?")
    else:
        st.balloons() # 적당히 마시면 축하 풍선!

with col2:
    st.header("🔍 품목 가격 비교")
    # (검색 코드는 이전과 동일하게 유지)
    item_data = {
        "포카리스웨트": {"자판기": 1000, "편의점": 1500, "마트": 1200},
        "레쓰비": {"자판기": 800, "편의점": 1200, "마트": 900},
        "코카콜라": {"자판기": 1200, "편의점": 1800, "마트": 1500}
    }
    search = st.text_input("음료 이름 입력", placeholder="예: 코카콜라")
    if search:
        results = {k: v for k, v in item_data.items() if search in k}
        for item, prices in results.items():
            st.write(f"**{item}**")
            st.metric("자판기 가격", f"{prices['자판기']}원", f"-{prices['편의점']-prices['자판기']}원 (편의점 대비)")
