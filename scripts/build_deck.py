#!/usr/bin/env python3
"""Build deck/index.html from the wiki. Examples are computed by algos.py, not typed by hand.
Each slide declares data-wiki="page-id ..."; check_deck.py verifies them."""
import json, pathlib, html
from algos import *

root = pathlib.Path(__file__).resolve().parent.parent
E = html.escape

def row(cells, cls=""): return "".join(f'<span class="cell {cls}">{E(str(c))}</span>' for c in cells)

bs_arr, bs_x = [1, 3, 5, 7, 9, 11, 13], 11
bs_steps, bs_res = binary_search_trace(bs_arr, bs_x)
ins_in = [5, 2, 4, 6, 1, 3]; ins_rows = insertion_trace(ins_in)
sel_in = [7, 5, 1, 4, 3];    sel_rows = selection_trace(sel_in)
ns = [7, 15, 1000, 1000000]

def trace_rows(inp, rows):
    out = f'<div class="trace"><div class="tr">{row(inp, "dim")}<em>原始</em></div>'
    for k, r in enumerate(rows, 1): out += f'<div class="tr">{row(r)}<em>第 {k} 回合後</em></div>'
    return out + "</div>"

DATA = {"bs_arr": bs_arr, "bs_x": bs_x, "bs_steps": bs_steps, "bs_res": bs_res}

slides = [
 # (wiki pages, html)
 ([], f'''<h1>演算法入門</h1><p class="sub">Big O、二元搜尋與基本排序<br>給第一次接觸演算法的你</p>
  <p class="meta">資料來源：LLM Wiki（6 份來源，5 個頁面）</p>'''),
 (["big-o"], '''<h2>學完這份簡報，你能…</h2><ul>
  <li>用一句話說明 <b>Big O</b> 在描述什麼</li><li>說出<b>二元搜尋</b>為什麼快、什麼時候不能用</li>
  <li>手動跑一次<b>插入排序</b>與<b>選擇排序</b></li><li>比較四種演算法的時間複雜度</li></ul>
  <p class="note">先備知識：會讀陣列（a₁, a₂, …, aₙ）即可。</p>'''),
 (["binary-search"], f'''<h2>為什麼要在乎演算法的快慢？</h2>
  <p>在 <b>1,000,000</b> 筆已排序資料中找一個數：</p>
  <div class="two"><div class="card"><h3>從頭一個個找</h3><p class="big">最多 1,000,000 次</p></div>
  <div class="card hi"><h3>二元搜尋</h3><p class="big">最多 {max_comparisons(1000000)} 次</p></div></div>
  <p class="note">{max_comparisons(1000000)} = ⌊lg 1,000,000⌋ + 1，由程式計算，非手填。</p>'''),
 (["big-o"], '''<h2>Big O 是什麼？</h2>
  <p class="quote">描述「輸入變大時，執行時間（或空間）成長得多快」</p>
  <ul><li>只看<b>成長趨勢</b>，忽略常數：3n 與 100n 都是 O(n)</li>
  <li>只是<b>上界</b>：f(n) ≤ c·g(n)，當 n ≥ n₀</li>
  <li>O 來自德文 <i>Ordnung</i>（階、order）</li></ul>'''),
 (["big-o"], '''<h2>三個容易搞混的符號</h2>
  <table><tr><th>符號</th><th>意思</th></tr><tr><td>O（Big O）</td><td>上界</td></tr>
  <tr><td>Ω（Big Omega）</td><td>下界</td></tr><tr><td>Θ（Big Theta）</td><td>上下界夾住（tight bound）</td></tr></table>
  <p class="warn">⚠️ 我們課堂的 little o 定義是「極限 = 1」，和一般教科書（極限 = 0）不同，考試依老師版本。</p>
  <p class="note">常見誤解：Big O ≠ 最壞情況。「最壞情況」是挑輸入，「Big O」是函數的界。</p>'''),
 (["binary-search"], '''<h2>二元搜尋：想法</h2>
  <ol><li>先確認陣列<b>已排序</b></li><li>拿目標 X 和<b>中間</b>元素 aⱼ 比</li>
  <li>X = aⱼ → 找到；X &lt; aⱼ → 只看左半；X &gt; aⱼ → 只看右半</li><li>重複，直到找到或範圍變空</li></ol>
  <pre>i := 1; m := n
while i &lt;= m do
   j := ⌊(i+m)/2⌋
   if X = a_j then output j and stop
   if X &lt; a_j then m := j-1 else i := j+1
output 0</pre>'''),
 (["binary-search"], '''<h2>互動示範：在 [1, 3, 5, 7, 9, 11, 13] 找 11</h2>
  <div id="bs"></div><div class="ctl"><button id="prev">← 上一步</button><button id="next">下一步 →</button></div>
  <p id="bsmsg" class="note"></p>'''),
 (["binary-search"], f'''<h2>最多要比較幾次？</h2>
  <table><tr><th>n</th><th>⌊lg n⌋ + 1</th></tr>{"".join(f"<tr><td>{n:,}</td><td>{max_comparisons(n)}</td></tr>" for n in ns)}</table>
  <p class="note">資料量變 1000 倍，次數只多約 10 次，這就是 O(log n)。<br>⚠️ 次數是 ⌊lg n⌋+1，不是 lg n。</p>
  <p class="warn">對沒排序的陣列用二元搜尋，結果會是錯的，不只是變慢。</p>'''),
 (["insertion-sort"], f'''<h2>插入排序：像整理撲克牌</h2>
  <p>把第 j 張抽出，插入前面已排好的牌中。示範：{", ".join(map(str, ins_in))}</p>{trace_rows(ins_in, ins_rows)}
  <ul><li>已排序 → 很快 O(n)；反向排序 → 最慢 O(n²)</li><li>穩定（相同值不換順序）</li></ul>'''),
 (["selection-sort"], f'''<h2>選擇排序：每回合挑最小的</h2>
  <p>示範：{", ".join(map(str, sel_in))}（與課堂範例一致）</p>{trace_rows(sel_in, sel_rows)}
  <p>比較次數固定為 n(n−1)/2：例如 n=5 時 = {selection_comparisons(5)} 次，<b>與資料內容無關</b>。</p>'''),
 (["quicksort"], '''<h2>快速排序：分而治之（概念）</h2>
  <ol><li>選一個 <b>pivot</b></li><li>分成「比 pivot 小」與「比 pivot 大」兩堆</li><li>兩堆各自遞迴排序</li></ol>
  <ul><li>平均 O(n log n)，最壞 O(n²)</li><li>pivot 的選法影響效能，不影響正確性</li></ul>
  <p class="note">本次期中不考，這裡只建立概念。</p>'''),
 (["big-o", "binary-search", "insertion-sort", "selection-sort", "quicksort"], '''<h2>四種演算法對照</h2>
  <table><tr><th>演算法</th><th>最好</th><th>最壞</th><th>備註</th></tr>
  <tr><td>二元搜尋</td><td>O(1)</td><td>O(log n)</td><td>需已排序</td></tr>
  <tr><td>插入排序</td><td>O(n)</td><td>O(n²)</td><td>穩定、近排序時快</td></tr>
  <tr><td>選擇排序</td><td>O(n²)</td><td>O(n²)</td><td>與資料無關</td></tr>
  <tr><td>快速排序</td><td>平均 O(n log n)</td><td>O(n²)</td><td>pivot 很關鍵</td></tr></table>
  <p class="note">插入、選擇排序的次數依課堂定義：分別是資料搬移數與比較數。</p>'''),
 (["binary-search", "selection-sort", "big-o"], '''<h2>小測驗（點題目看答案）</h2>
  <details><summary>Q1：在 255 筆已排序資料用二元搜尋，最多比較幾次？</summary><p>⌊lg 255⌋ + 1 = 8 次。</p></details>
  <details><summary>Q2：選擇排序排 10 個數，比較幾次？</summary><p>10×9/2 = 45 次，不管資料長怎樣。</p></details>
  <details><summary>Q3：對 [5, 2, 9] 做二元搜尋可以嗎？</summary><p>不行，必須先排序。</p></details>'''),
 (["big-o", "binary-search", "insertion-sort", "selection-sort", "quicksort"], '''<h2>回顧與來源</h2>
  <ul><li>Big O = 成長趨勢的上界</li><li>二元搜尋：已排序 + 每次砍半 → O(log n)</li>
  <li>排序：插入（近排序快）、選擇（次數固定）、快速（平均快）</li></ul>
  <p class="note">來源：自編課程講義；Wikipedia（Big O notation、Binary search、Insertion sort、Selection sort、Quicksort，CC BY-SA）。每個論點在 wiki/pages 都有原文引用。</p>'''),
]

# --- pre-flight (check moved earlier): refuse to write a slide whose O(...) claims are not in its cited wiki pages
import re
def _sq(t): return re.sub(r"[\s\\]", "", t).replace("²", "^2").replace("lg", "log")
for i, (w, h) in enumerate(slides, 1):
    corpus = "".join((root / f"wiki/pages/{p}.md").read_text(encoding="utf-8") for p in w)
    for expr in set(re.findall(r"O\([^()]*(?:\([^()]*\))?[^()]*\)", re.sub(r"<[^>]+>", "", h))):
        if _sq(expr) not in _sq(corpus):
            raise SystemExit(f"PRE-FLIGHT FAIL slide {i}: {expr} not in wiki pages {w} -> add it to the wiki first")

secs = "\n".join(
    f'<section class="slide" data-wiki="{" ".join(w)}">{h}<footer>{"Wiki：" + "、".join(w) if w else ""}</footer></section>'
    for w, h in slides)

tpl = (root / "scripts/deck_template.html").read_text(encoding="utf-8")
out = tpl.replace("<!--SLIDES-->", secs).replace("/*DATA*/", "const DATA=" + json.dumps(DATA, ensure_ascii=False) + ";")
(root / "deck").mkdir(exist_ok=True)
(root / "deck/index.html").write_text(out, encoding="utf-8")
print(f"built deck/index.html with {len(slides)} slides")
