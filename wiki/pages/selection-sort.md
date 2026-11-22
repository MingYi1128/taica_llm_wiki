---
id: selection-sort
title: 選擇排序 Selection Sort
sources: [S1, S5]
---
# 選擇排序 Selection Sort

一句話：每一回合從未排序部分挑出最小的，換到前面。

## 事實
- 選擇排序是原地的比較排序，時間複雜度 O(n²)。 [S5] > "It has a O(n2) time complexity"
- 它把清單分成左邊已排序、右邊未排序兩部分。 [S5] > "The algorithm divides the input list into two parts"
- 迴圈不依賴資料內容，所以分析簡單。 [S5] > "none of the loops depend on the data in the array"
- 課堂結論：以比較次數計，best = worst = average = O(n²)，與資料無關。 [S1] > "best = worst = average = $O(n^2)$"
- 課堂的比較總數是 n(n-1)/2。 [S1] > "$(n-1)+(n-2)+\dots+1=\frac{n(n-1)}2$"
- 課堂範例：7 5 1 4 3 → 1 5 7 4 3 → 1 3 7 4 5 → 1 3 4 7 5 → 1 3 4 5 7。 [S1] > "7 5 1 4 3 → 1 5 7 4 3 → 1 3 7 4 5 → 1 3 4 7 5 → 1 3 4 5 7"

## 注意
- 本次期中不在範圍內（講義標示期末再讀），簡報作為「排序家族」的對照介紹即可。 [S1] > "以下 §2.3–§2.5 不在本次期中範圍"
