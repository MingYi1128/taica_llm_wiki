---
id: insertion-sort
title: 插入排序 Insertion Sort
sources: [S1, S4]
---
# 插入排序 Insertion Sort

一句話：像整理手上的撲克牌，一張一張抽出來，插到前面已排好的牌裡正確的位置。

## 事實
- 對小資料集有效率，和其他二次時間排序同類。 [S4] > "Efficient for (quite) small data sets, much like other quadratic (i.e., O(n2)) sorting algorithms"
- 具適應性：資料已大致排序時很快。 [S4] > "Adaptive, i.e., efficient for data sets that are already substantially sorted"
- 穩定：相同鍵值的相對順序不變。 [S4] > "Stable; i.e., does not change the relative order of elements with equal keys"
- 最壞情況輸入是反向排序的陣列。 [S4] > "The simplest worst case input is an array sorted in reverse order."
- 課堂分析用「資料搬移次數 M」：已排序時 M = 2(n-1) = O(n)。 [S1] > "| Best | 已排序 | 全 0 | $2(n-1)=O(n)$ | $n-1$ |"
- 課堂分析：反向排序時 M = O(n²)。 [S1] > "$2(n-1)+\frac{n(n-1)}2=O(n^2)$"

## 學習者常見誤解
- 「插入排序一定比選擇排序慢」不一定：資料接近排序時插入排序快很多。
