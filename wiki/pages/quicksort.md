---
id: quicksort
title: 快速排序 Quicksort
sources: [S1, S6]
---
# 快速排序 Quicksort

一句話：選一個 pivot，把其他元素分成「比它小」與「比它大」兩堆，再各自遞迴排序。

## 事實
- 快速排序是分而治之（divide-and-conquer）演算法。 [S6] > "Quicksort is a divide-and-conquer algorithm."
- 平均需要 O(n log n) 次比較，最壞 O(n²)。 [S6] > "on average, the algorithm takes"
- pivot 的選法大幅影響效能，但不影響正確性。 [S6] > "The way the pivot is chosen greatly affects performance, but not correctness."
- 多數實作不穩定。 [S6] > "Most implementations of quicksort are not stable"
- 課堂：最壞情況是資料已排序或反向排序，每次 pivot 都是最小或最大。 [S1] > "資料**已排序或反向排序**，每次 pivot 是最小/最大"
- ⚠️ 課堂要求使用老師版本的 Partition，不要用 Hoare/Lomuto。 [S1] > "一定要照這個版本做"

## 注意
- 同樣不在本次期中範圍，簡報只做概念介紹。
