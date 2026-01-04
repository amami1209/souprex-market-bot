import streamlit as st

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
            # TODO: ここにSouprexの取得/分析を差し込む
            result = {"keyword": keyword, "count": 42, "median_price": 29800}

        st.success("取得完了")
        col1, col2 = st.columns(2)
        col1.metric("件数", result["count"])
        col2.metric("中央値", f"¥{result['median_price']:,}")
        st.info("※ 本デモはヤフオクのみ対応。eBayは採用後に統合予定です。")
