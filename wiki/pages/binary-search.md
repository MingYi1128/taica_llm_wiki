---
id: binary-search
title: 二元搜尋 Binary Search
sources: [S1, S3]
---
# 二元搜尋 Binary Search

一句話：在「已排序」的陣列中，每次拿目標和中間元素比，一次丟掉一半，所以很快。

## 事實
- 二元搜尋把目標值與陣列中間元素比較。 [S3] > "Binary search compares the target value to the middle element of the array."
- 前提：陣列必須先排序。 [S3] > "the array must be sorted first to be able to apply binary search"
- 最壞情況是對數時間；除了很小的陣列，比線性搜尋快。 [S3] > "Binary search is faster than linear search except for small arrays."
- 課堂版本：樹高為 ⌊lg n⌋+1，最好 O(1)、最壞與平均 O(log n)。 [S1] > "Best $O(1)$；Worst $\lfloor\lg n\rfloor+1=O(\log n)$；Average $O(\log n)$。"
- 課堂的「一次比較」＝拿 X 和一個 a_j 比（三向比較算 1 次）。 [S1] > "「一次比較」= 拿 X 和一個 $a_j$ 比（三向比較算 1 次）＝走到樹上一個節點。"
- 課堂虛擬碼：j := ⌊(i+m)/2⌋，X < a_j 則 m := j-1，否則 i := j+1。 [S1] > "if X < a_j then m := j-1 else i := j+1"

## 學習者常見誤解
- 對沒排序的陣列用二元搜尋會得到錯誤結果，不是只有變慢。
- n 個元素，最多比較 ⌊lg n⌋+1 次，不是 lg n 次（例：n=7 最多 3 次）。
