# Ingest / 變更紀錄

| 步驟 | 動作 | 結果 |
|---|---|---|
| 1 | ingest S1：自己整理的課程講義（沿用 Homework_261103 的 midterm-guide.md） | raw/S1 |
| 2 | ingest S2–S6：Wikipedia 5 篇（API 取純文字，原樣存入 raw/） | raw/S2–S6，共 6 份來源 |
| 3 | 生成 5 個 wiki 頁面，每條事實附 [Sx] 與逐字引用 | pages/*.md |
| 4 | `check_wiki.py` 第 1 次執行 | OK：31 條，引用全部在 raw 中找到 |
| 5 | 生成簡報 → `check_deck.py` 第 1 次執行 | 失敗：slide 4 的 O(n) 沒有 wiki 支持 |
| 6 | 補 wiki 的「教學範例（推論）」，重新建置 | OK |
| 7 | build_deck.py 加入 pre-flight（生成前檢查），並做反向測試 | 移除 wiki 那行後 build 會被擋下，見 logs/ |
