import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(page_title="학교 자판기 가이드", layout="centered")

# 2. 제목 부분
st.title("🥤 우리 학교 자판기 알뜰 매니저")
st.subheader("합리적인 소비 습관을 만들어봐요!")

# 3. HTML/JavaScript 코드 (안전하게 변수에 담기)
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .box { background: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #ddd; font-family: sans-serif; }
        input { width: 100%; padding: 8px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { width: 100%; padding: 10px; background: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; }
        #result { margin-top: 15px; font-weight: bold; color: #2c3e50; text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; font-size: 14px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <div class="box">
        <label>💰 이번 주 내 용돈 (원):</label>
        <input type="number" id="money" placeholder="예: 30000">
        <button onclick="calc()">적정 횟수 계산하기</button>
        <div id="result">금액을 입력해 주세요.</div>

        <table>
            <tr><th>품목</th><th>자판기</th><th>편의점</th></tr>
            <tr><td>커피</td><td>800원</td><td>1,200원</td></tr>
            <tr><td>이온음료</td><td>1,000원</td><td>1,500원</td></tr>
            <tr><td>생수</td><td>600원</td><td>600원</td></tr>
        </table>
    </div>

    <script>
        function calc() {
            var m = document.getElementById('money').value;
            var res = document.getElementById('result');
            if(m > 0) {
                // 용돈의 10%를 자판기 예산으로 설정, 음료당 1000원 가정
                var count = Math.floor((m * 0.1) / 1000);
                res.innerHTML = "이번 주 권장 횟수는 <span style='color:red'>" + count + "회</span> 입니다!";
            } else {
                res.innerHTML = "숫자를 입력해 주세요!";
            }
        }
    </script>
</body>
</html>
"""

# 4. Streamlit에 HTML 반영
components.html(html_content, height=500)

st.info("💡 팁: 자판기를 이용하기 전, 이 계산기를 통해 이번 주 예산을 확인하세요!")
