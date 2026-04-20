import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="학교 자판기 알뜰 가이드", layout="wide")

st.title("🥤 학교 자판기 합리적 소비")
st.write("합리적인 소비를 위한 우리들의 가이드")
st.divider()

# 2. 화면 분할 (좌측: 계산기, 우측: 가격 검색)
col1, col2 = st.columns(2)

# --- 왼쪽: 용돈 계산기 ---
with col1:
    st.header("💰 용돈 관리 계산기")
    allowance = st.number_input("이번 주 총 용돈을 입력하세요 (원)", min_value=0, step=1000, value=30000)
    avg_price = st.number_input("자판기 음료 평균 가격 (원)", min_value=0, step=100, value=1000)
    
    # 예산 비중 설정 (예: 용돈의 10%만 자판기에 쓰기)
    ratio = st.slider("용돈 중 자판기에 쓸 비중 (%)", 0, 100, 10)
    
    budget = allowance * (ratio / 100)
    count = int(budget / avg_price) if avg_price > 0 else 0
    
    st.info(f"이번 주 자판기용 예산은 **{budget:,.0f}원**입니다.")
    st.success(f"일주일에 최대 **{count}번** 마시는 것을 추천해요!")

# --- 오른쪽: 품목 검색 및 가격 비교 ---
with col2:
    st.header("🔍 품목 가격 비교")
    
    # 가상의 가격 데이터 (실제 웹 데이터를 대신함)
    item_data = {
        "포카리스웨트": {"자판기": 1000, "편의점": 1500, "마트": 1200},
        "레쓰비": {"자판기": 800, "편의점": 1200, "마트": 900},
        "코카콜라": {"자판기": 1200, "편의점": 1800, "마트": 1500},
        "생수": {"자판기": 600, "편의점": 800, "마트": 500},
        "초코우유": {"자판기": 1000, "편의점": 1600, "마트": 1300}
    }
    
    search_query = st.text_input("궁금한 음료 이름을 입력하세요", placeholder="예: 포카리스웨트")
    
    if search_query:
        # 검색 기능 (이름이 포함되면 출력)
        results = {k: v for k, v in item_data.items() if search_query in k}
        
        if results:
            for item, prices in results.items():
                st.subheader(f"[{item}] 가격 정보")
                
                # 가로로 지표 표시
                c1, c2, c3 = st.columns(3)
                c1.metric("자판기", f"{prices['자판기']}원")
                c2.metric("편의점", f"{prices['편의점']}원", f"{prices['자판기'] - prices['편의점']}원")
                c3.metric("마트", f"{prices['마트']}원", f"{prices['자판기'] - prices['마트']}원")
                
                st.caption("※ 자판기가 편의점보다 얼마나 저렴한지 빨간색 수치로 표시됩니다.")
        else:
            st.error("아직 데이터가 없는 품목입니다. 다른 이름을 검색해 보세요!")
    else:
        st.write("위에 음료 이름을 입력하면 가격을 비교해 드립니다.")

st.divider()
st.caption("© 2026 우리 학교 합리적 소비 동아리 | 데이터는 주기적으로 업데이트됩니다.")
