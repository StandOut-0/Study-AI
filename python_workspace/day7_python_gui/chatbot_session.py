import streamlit as st
import pandas as pd
import time

st.title("🧠 Cache Data vs Cache Resource Demo")

# =========================
# 1. 데이터 캐시 (CSV 로딩)
# =========================
@st.cache_data
def load_sales_data():
    st.write("📦 CSV 로딩 실행됨 (cache_data)")
    time.sleep(2)  # 느리게 만들어서 차이 보이게
    return pd.DataFrame({
        "product": ["A", "B", "C", "A"],
        "price": [100, 200, 300, 150],
        "qty": [1, 2, 1, 3]
    })


# =========================
# 2. 리소스 캐시 (무거운 객체)
# =========================
@st.cache_resource
def load_fake_model():
    st.write("🤖 모델 생성 실행됨 (cache_resource)")
    time.sleep(3)  # 일부러 느리게
    return {
        "name": "demo-model",
        "version": 1
    }


# =========================
# 버튼으로 강제 테스트
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("📊 CSV 로드"):
        df = load_sales_data()
        st.dataframe(df)
        st.write("총 매출:", (df["price"] * df["qty"]).sum())


with col2:
    if st.button("🤖 모델 로드"):
        model = load_fake_model()
        st.write(model)


st.divider()
st.caption("💡 새로고침(F5)해도 cache_data / cache_resource는 다시 실행되지 않음")