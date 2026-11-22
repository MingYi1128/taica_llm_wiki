---
id: big-o
title: Big O 與複雜度
sources: [S1, S2]
---
# Big O 與複雜度

一句話：Big O 描述「輸入變大時，執行時間（或空間）成長得多快」，只看成長趨勢，不看常數。

## 事實（每條都要有來源與原文引用）
- Big O 用來依輸入大小對執行時間或空間需求的成長方式分類演算法。 [S2] > "big O notation is used to classify algorithms by how their run time or space requirements grow with the input"
- Big O 看的是變數很大時的成長率，成長率相同的函數可以用同一個 O 表示。 [S2] > "different functions with the same asymptotic growth rate may be represented using the same O notation"
- 字母 O 來自 Ordnung，意思是近似的階（order）。 [S2] > "The letter O stands for Ordnung, that is, the order of approximation."
- 課堂定義：存在正常數 c 與 n0，使得 n ≥ n0 時 |f(n)| ≤ c|g(n)|（上界）。 [S1] > "存在正常數 $c$ 與 $n_0$，使得 $|f(n)|\le c\,|g(n)|,\ \forall n\ge n_0$。（上界 upper bound）"
- Big Ω 是下界，Big Θ 是上下界夾住的 tight bound。 [S1] > "（tight bound）"

## 教學範例（由定義推導，非引用；已標示為推論）
- 推論：3n 與 100n 都是 O(n)，因為取 c = 3 或 c = 100，對所有 n ≥ 1 都有 f(n) ≤ c·n。

## 來源之間的差異（教學時必須講清楚）
- ⚠️ 本課講義的 little o 定義是「極限等於 1」，與一般教科書（極限為 0）不同；考試依老師版本，簡報若提到 little o 須註明。 [S1] > "和一般教科書（CLRS：極限為 0）不同，作答依老師版本。"

## 學習者常見誤解
- Big O 只是上界，不等於「最壞情況」；「最壞情況」是輸入的選擇，「Big O」是函數的界，兩者不同。
