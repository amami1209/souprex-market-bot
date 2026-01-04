import streamlit as st
import pandas as pd
from collectors.yahoo import fetch_yahoo_items

st.set_page_config(page_title="Souprex Market Bot (Demo)", layout="wide")

st.title("📊 Souprex Market Bot")
st.caption("ヤフオク / eBay 市場観測デモ（分析専用・自動購入なし）")

st.subheader("🔍 検索条件")
keyword = st.text_input("検索キーワード（型番など）", placeholder="例：Nintendo Switch 有機EL")

run = st.button("市場データ取得")
st.divider()

if run:
    if not keyword:
        st.warning("キーワードを入力してください")
    else:
        with st.spinner("市場データを取得中..."):
            items = fetch_yahoo_items(keyword, limit=30)

        df = pd.DataFrame([{"title": x.title, "price": x.price, "url": x.url} for x in items])

        st.success("取得完了")

        col1, col2 = st.columns(2)
        col1.metric("件数", len(df))
        col2.metric("中央値", f"¥{int(df['price'].median()):,}")

        st.subheader("📋 取得結果（デモ）")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            label="CSVダウンロード",
            data=csv,
            file_name=f"yahoo_{keyword}.csv",
            mime="text/csv",
        )

        st.info("※ 本デモはヤフオクのみ対応。eBayは採用後に統合予定です。")
