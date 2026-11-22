# HW 261110｜用 LLM Wiki 做教學 HTML 簡報：演算法入門

國立雲林科技大學 M11517014 王銘億 演算法入門

## 1. LLM Wiki 主題與介紹
主題：**演算法入門（Big O、二元搜尋、插入／選擇／快速排序）**。
6 份來源：自己整理的課程講義（S1）＋ Wikipedia 5 篇（S2–S6），原文放 `wiki/raw/`，整理成 5 個頁面 `wiki/pages/`。
每條事實都有來源編號與逐字引用，由程式驗證。入口：[`wiki/index.md`](wiki/index.md)、[`wiki/log.md`](wiki/log.md)、[`wiki/discussion.md`](wiki/discussion.md)。

## 2. 教學 HTML 簡報
[`deck/index.html`](deck/index.html)（14 張，方向鍵翻頁，含二元搜尋互動示範與小測驗）。
連結：https://mingyi1128.github.io/taica_llm_wiki/deck/ （需在 repo Settings → Pages 啟用 main 分支）

## 3. loop / graph 設計

```
 [取得資料] → [ingest 到 raw/] → [生成 wiki 頁面（附逐字引用）]
                                      │
                         ┌── ✗ ── [Check 1：引用是否真的在 raw 中]
                         │ 修 wiki         │ ✓
                         │                 ▼
                         │        [規劃投影片，每張標 data-wiki]
                         │                 ▼
                         ├── ✗ ── [Pre-flight：O(...) 是否在所引用的 wiki 頁]
                         │                 │ ✓
                         │                 ▼
                         │        [生成 HTML，範例由程式算出]
                         │                 ▼
                         └── ✗ ── [Check 2：投影片對應 wiki＋重算數字] → ✓ → [人工瀏覽] → 完成
```
- **重複的步驟**：「生成 → 檢查 → 失敗就回到上游修 wiki」。修的是 wiki，不是直接改簡報，這樣來源和簡報才一致。
- **為什麼這樣設計**：LLM 容易寫出「看起來對」但來源裡沒有的內容。所以把檢查變成可執行的程式，讓機器比對，不靠自己再看一次。範例（trace、表格）由 `scripts/algos.py` 算出，不手打。

## 4. 一次實際執行的紀錄（`logs/`）
| 次 | 檢查 | 結果 |
|---|---|---|
| 1 | Check 1（wiki） | OK，31 條引用都在 raw 找到（`run1_check_wiki.txt`） |
| 1 | Check 2（簡報） | **失敗**：slide 4 的 `O(n)` 不在 `big-o` 頁（`run1_check_deck.txt`） |
| 2 | 補 wiki「教學範例（推論）」後重跑 | OK，14 張皆有 wiki 對應，數字重算一致（`run2_check_deck.txt`） |
| 2 | Pre-flight 反向測試：刻意移除該行 | build 被擋下（`run2_preflight_negative_test.txt`） |

另外用瀏覽器開啟實測：互動示範第 2 步找到位置 6，與程式計算一致，無 console 錯誤、無橫向捲動。

## 5. 反思
- **最常出錯的節點：生成簡報。** Check 1 一次就過，因為引用是從原文複製的；錯誤出在簡報階段，AI 為了教學順手加了「3n 與 100n 都是 O(n)」這種來源沒有的例子。
- **怎麼調整：** 原本只在簡報完成後（Check 2）才發現。我加了 **pre-flight**，在寫出 HTML 之前就擋下：投影片裡的複雜度式子若不在所引用的 wiki 頁，就中止並要求先補 wiki。這樣錯誤被擋在「生成」之前，而不是「生成」之後。
- **為什麼修改 workflow：** 教學簡報一定會需要來源以外的例子。與其禁止，不如規定「例子要先進 wiki 並標為推論」，讓來源和簡報仍可對應。
- **還沒做到的：** 檢查只涵蓋 `O(...)` 式子與數字，一般敘述句（例如「像整理撲克牌」）仍需人工看。


## 重跑
```bash
python3 scripts/check_wiki.py && python3 scripts/build_deck.py && python3 scripts/check_deck.py
```
