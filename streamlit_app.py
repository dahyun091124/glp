<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>학교 자판기 알뜰 가이드</title>
    <style>
        body { font-family: 'Nanum Gothic', sans-serif; line-height: 1.6; background-color: #f4f7f6; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; text-align: center; }
        .section { margin-bottom: 30px; padding: 15px; border-bottom: 1px solid #eee; }
        label { display: block; margin-bottom: 10px; font-weight: bold; }
        input { width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background-color: #3498db; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #2980b9; }
        #result { margin-top: 15px; padding: 15px; background: #e8f4fd; border-radius: 5px; font-weight: bold; text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #f8f9fa; }
        .price-up { color: #e74c3c; font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <h1>🏫 자판기 알뜰 매니저</h1>

    <div class="section">
        <h3>💰 나의 주간 소비 한도 계산</h3>
        <label>일주일 총 용돈: <input type="number" id="allowance" placeholder="예: 30000"></label>
        <label>음료 1개 평균 가격: <input type="number" id="avgPrice" value="1000"></label>
        <button onclick="calculate()">적정 횟수 확인하기</button>
        <div id="result">용돈을 입력하면 결과가 나옵니다.</div>
    </div>

    <div class="section">
        <h3>📊 편의점 vs 자판기 가격 비교</h3>
        <table>
            <thead>
                <tr>
                    <th>품목</th>
                    <th>자판기</th>
                    <th>편의점</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>캔커피</td>
                    <td>800원</td>
                    <td class="price-up">1,200원</td>
                </tr>
                <tr>
                    <td>이온음료</td>
                    <td>1,000원</td>
                    <td class="price-up">1,500원</td>
                </tr>
                <tr>
                    <td>생수</td>
                    <td>600원</td>
                    <td>600원</td>
                </tr>
            </tbody>
        </table>
        <p style="font-size: 0.8em; color: #7f8c8d; margin-top:10px;">* 학교 자판기가 보통 20~30% 더 저렴합니다!</p>
    </div>
</div>

<script>
    function calculate() {
        const allowance = document.getElementById('allowance').value;
        const avgPrice = document.getElementById('avgPrice').value;
        const resultDiv = document.getElementById('result');

        if(allowance > 0) {
            // 용돈의 10%를 자판기 적정 예산으로 설정 (예시 로직)
            const limit = Math.floor((allowance * 0.1) / avgPrice);
            resultDiv.innerHTML = `이번 주 권장 횟수는 최대 <span style="color:#e67e22">${limit}회</span> 입니다!<br>
                                   (용돈의 10% 사용 기준)`;
        } else {
            resultDiv.innerHTML = "용돈을 올바르게 입력해주세요.";
        }
    }
</script>

</body>
</html>
