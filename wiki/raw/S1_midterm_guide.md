# 高等計算機演算法 期中考複習講義

> 資料來源：`Textbook/ch1 20260906.pdf`、`Textbook/ch2 20261019.pdf`、`Exercises/*.png`、`Past_Midterm_114.png`
> 頁碼標示「ch2 p.N」= PDF 第 N 頁（投影片右下角編號通常是 N+1，例如 PDF p.6 的投影片印的是 7）。

---

## 0. 先看這個：考試情報

1. **ch1 p.10 (Grading)**：期中 35%，而且「期中、期末約 **70~80 分**出自**隨堂練習**」。→ 隨堂練習一定要能**默寫級**地寫出完整過程。
2. **去年考試範圍清單**（Past_Midterm_114.png）共 14 項，對照今年進度：

| # | 去年要求 | 今年隨堂練習有沒有出過 | 本講義位置 |
|---|---|---|---|
| 1 | Big O 定義 | ✅ 9/21 #1 | §1.1、§3-A |
| 2 | 多項式證 O(·)，找 c、n₀ | ✅ 9/21 #2 | §1.2、§3-A |
| 3 | 調和級數 $H_n=O(\lg n)$ | ❌（尚未出） | §1.3 |
| 4 | 指數 / 多項式演算法定義 | ❌ | §1.4 |
| 5–6 | Insertion sort 步驟 + best/worst/avg | ✅ 10/12 | §2.1、§3-B |
| 7–9 | Binary search 步驟、畫樹、三種複雜度 | ✅ 10/19 | §2.2、§3-C |
| 10–11 | Selection sort 步驟 + 比較次數分析 | ⛔ 今年期中範圍外 | §2.3、§4 |
| 12–13 | Quick sort 步驟 + 三種複雜度 | ⛔ 今年期中範圍外 | §2.4、§4 |
| 14 | 由 $\frac{T(n)}{n+1}\le\frac{T(n-1)}{n}+\frac{2}{n}$ 解 T(n) | ⛔ 今年期中範圍外 | §2.4.3 |

> **本次期中範圍（10/20 確認）：上到 Binary Search 為止**＝ch1 + ch2 p.1–36。
> Selection sort、Quick sort、T(n) 遞迴、lower bound、heap sort（§2.3–§2.5、§4）**期中不考**，留到期末再讀。
> 範圍比去年小，考題會更集中在 Big O 證明、Insertion sort、Binary search，也就是隨堂練習那 13 題。
> $H_n=O(\lg n)$（§1.3）在講義裡出現在 quicksort 段落，但它的證法（用積分夾住和）和 binary search 練習 #5 完全相同，建議還是練。

---

## 1. 漸近符號與複雜度（ch2 p.3–16）

### 1.1 定義（**必背，逐字寫得出來**）

- **Big O**（ch2 p.6）：
  $f(n)=O(g(n))$ iff 存在正常數 $c$ 與 $n_0$，使得 $|f(n)|\le c\,|g(n)|,\ \forall n\ge n_0$。（上界 upper bound）
- **Big Ω**（ch2 p.63）：$f(n)=\Omega(g(n))$ iff 存在 $c,n_0>0$，$|f(n)|\ge c\,|g(n)|,\ \forall n\ge n_0$。（下界）
- **Big Θ**（ch2 p.63）：存在 $c_1,c_2,n_0>0$，$c_1|g(n)|\le|f(n)|\le c_2|g(n)|,\ \forall n\ge n_0$。（tight bound）
- **little o**（ch2 p.63，此投影片的定義）：$f(n)=o(g(n))$ 若 $\lim_{n\to\infty}\frac{f(n)}{g(n)}=1$。
  ⚠️ 注意這是這份投影片（李家同課本）的用法，例如 $3n^2+n=o(3n^2)$；和一般教科書（CLRS：極限為 0）不同，作答依老師版本。

### 1.2 多項式 → O(n^m) 的標準證法（ch2 p.9）

$f(n)=a_mn^m+\dots+a_1n+a_0$
$$|f(n)|\le |a_m|n^m+\dots+|a_1|n+|a_0| = n^m\Big(|a_m|+\frac{|a_{m-1}|}{n}+\dots+\frac{|a_0|}{n^m}\Big)\le n^m(|a_m|+\dots+|a_0|),\ \ n\ge1$$
取 $c=|a_m|+\dots+|a_0|$、$n_0=1$ ⇒ $f(n)=O(n^m)$。

**萬用套路**：係數全部取絕對值加起來就是 c，n₀=1。若要更小的 c，就「丟掉負項、把低次項放大成最高次」，但要另外說明 $f(n)\ge0$（因為定義裡有絕對值）。

**去年考題**：$7n^4+6n^3-8n^2+5n-9=O(n^4)$
- 套路一：$c=7+6+8+5+9=35,\ n_0=1$。
- 套路二：$n\ge1$ 時 $f(n)\le 7n^4+6n^3+5n\le 7n^4+6n^4+5n^4=18n^4$；且 $f(n)\ge0$（$n=1$ 時 $f=1$；$n\ge2$ 時 $7n^4\ge 28n^2>8n^2+9$）⇒ $c=18,\ n_0=1$。

### 1.3 調和級數 $H_n=O(\lg n)$（去年考題 #3，今年還沒出）

$H_n=1+\frac12+\dots+\frac1n$。因為 $\frac1x$ 遞減，$\frac1k\le\int_{k-1}^{k}\frac{dx}{x}$（$k\ge2$）：
$$H_n = 1+\sum_{k=2}^{n}\frac1k\le 1+\int_1^n\frac{dx}{x}=1+\ln n = 1+(\ln2)\lg n$$
當 $n\ge2$，$\lg n\ge1$，所以 $1\le\lg n$：
$$H_n\le \lg n+(\ln2)\lg n=(1+\ln2)\lg n\approx1.693\lg n\le 2\lg n$$
⇒ **$c=2,\ n_0=2$**，$H_n=O(\lg n)$。（$n=1$ 時 $\lg1=0$ 不行，所以 $n_0$ 不能取 1。）

補充（ch2 p.55）：$H_n=\ln n+\gamma+\frac1{2n}-\dots$，$\gamma\approx0.5772$（Euler 常數）。

> 這題的「用積分夾住和」技巧跟 binary search 練習 #5（$\sum\lg i\le\int\lg x\,dx$）是同一招，老師上課畫過圖（ch2 p.33）。

### 1.4 多項式 vs. 指數演算法（ch2 p.14–15）

- **Polynomial algorithm**：時間複雜度為 $O(p(n))$，$p(n)$ 是多項式。例：$O(n^2)$、$O(n\log n)$（$n\log n\le n^2$，可被多項式 bound 住）。
- **Exponential algorithm**：時間複雜度**無法**被任何多項式 bound 住。例：$O(2^n)$、$O(n!)$、$O(n^n)$。
- 例：$2^n=O(2^n)$ 但 $2^n\ne O(n^2)$；$n^2=O(n^2)$ 也 $=O(2^n)$。
- 成長順序（ch2 p.13）：$O(1)<O(\log n)<O(n)<O(n\log n)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)$
- 觀念題（ch2 p.15）：A 是 $O(n^3)$、B 是 $O(n)$，B 一定比 A 快嗎？**不一定**，只有在 n 夠大時才成立（常數可能很大）。

### 1.5 其他觀念
- 計算步數例（ch2 p.4）：`Sum` 函式 $T(n)=2n+3$（for 迴圈判斷 n+1 次！）。
- Best case 最容易分析，average case 最難（ch2 p.16）。
- 不是任兩個函數都能比大小：$f(n)=n$ vs. $g(n)=n^{1+\sin n}$（ch2 p.7）。
- 注意 $\log_2 n=\log n=\lg n$（ch2 p.55 註）。

---

## 2. 排序與搜尋演算法

### 2.1 Straight Insertion Sort（ch2 p.17–23）

```
For j := 2 to n do
  i := j-1 ; temp := x_j
  While temp < x_i and i > 0 do
     x_{i+1} := x_i ; i := i-1
  x_{i+1} := temp
```
**用「資料搬移次數 M」分析**（ch2 p.21）：每回合 `temp := x_j` 與 `x_{i+1} := temp` 固定 2 次，再加上往右移的次數 $d_j$：
$$M=\sum_{j=2}^n(2+d_j)=2(n-1)+\sum_{j=2}^n d_j$$

| | 資料型態 | $d_j$ | M | 比較次數（補充） |
|---|---|---|---|---|
| Best | 已排序 | 全 0 | $2(n-1)=O(n)$ | $n-1$ |
| Worst | 反向排序 | $d_j=j-1$ | $2(n-1)+\frac{n(n-1)}2=O(n^2)$ | $\frac{n(n-1)}2$ |
| Average | 隨機 | 期望 $\frac{j-1}2$ | $\frac{(n-1)(n+8)}4=O(n^2)$ | 約 $\frac{n^2}4$ |

Average 推導見 §3-B Q4。

### 2.2 Binary Search（ch2 p.24–36）

```
i := 1; m := n
while i <= m do
   j := ⌊(i+m)/2⌋
   if X = a_j then output j and stop
   if X < a_j then m := j-1 else i := j+1
output 0
```
- 「一次比較」= 拿 X 和一個 $a_j$ 比（三向比較算 1 次）＝走到樹上一個節點。
- 對應的**二元搜尋樹**：root 是 $a_{\lfloor(1+n)/2\rfloor}$，左右子陣列遞迴。樹高 $\lfloor\lg n\rfloor+1$。
- Best $O(1)$；Worst $\lfloor\lg n\rfloor+1=O(\log n)$；Average $O(\log n)$。
- 成功搜尋 n 種情況、失敗搜尋 n+1 種情況（樹的 n+1 個外部節點），平均時分母是 $2n+1$（ch2 p.35、老師手寫 p.30）。

> ⛔ **以下 §2.3–§2.5 不在本次期中範圍**，期末再讀。

### 2.3 Straight Selection Sort（ch2 p.37–40）—— 去年考題 #10、#11

```
For j := 1 to n-1 do
   f := j                         // f 是 flag，記目前最小值位置
   For k := j+1 to n do
       If a_k < a_f then f := k   // ← 「flag 改變」
   a_j <-> a_f
```
- **比較次數**：每一回合比 $n-j$ 次，總共 $(n-1)+(n-2)+\dots+1=\frac{n(n-1)}2$，**best = worst = average = $O(n^2)$**（與資料無關！這是去年 #11 問的「in terms of number of comparisons」的答案）。
- **flag 改變次數**：best $O(n)$（其實是 0，已排序）；worst $O(n^2)$；average $O(n\log n)$。
  - 一回合找最小值的平均 flag 改變次數 $=H_n-1$（ch2 p.39–40，用 $P_n(k)=\frac1nP_{n-1}(k-1)+\frac{n-1}nP_{n-1}(k)$ 推）。
  - $A(n)=\sum_{i=2}^n H_i-(n-1)=O(n\log n)$。
- 投影片例子（ch2 p.38）：7 5 1 4 3 → 1 5 7 4 3 → 1 3 7 4 5 → 1 3 4 7 5 → 1 3 4 5 7。

### 2.4 Quick Sort（ch2 p.41–55）—— 去年考題 #12、#13、#14

#### 2.4.1 老師版本的 Partition（**一定要照這個版本做**，不要用網路上的 Hoare/Lomuto）

```
Quicksort(A, f, l)
1  if f < l then
2     x := A[f]                 // pivot = 最左邊
3     i := l+1
4     for j := l downto f+1     // j 由右往左掃
5        if A[j] > x then
6           i := i-1
7           exchange A[i] <-> A[j]
8     exchange A[i-1] <-> A[f]  // pivot 放到中間
9     q := i-1
10    Quicksort(A, f, q-1)
11    Quicksort(A, q+1, l)
```
**i、j 的意義**（ch2 p.43）：`A[f]`=pivot；`A[j+1..i-1]` 是 ≤x；`A[i..l]` 是 >x；`A[f+1..j]` 還沒看。
每個 partition 比較 $l-f$ 次（每個 j 一次）。

**投影片範例**（ch2 p.48）3 6 2 5 4 1，pivot=3：

| 步驟 | j | A[j] vs 3 | 動作 | 陣列 |
|---|---|---|---|---|
| 初始 | | | i=7 | 3 6 2 5 4 1 |
| 1 | 6 | 1 ≤ 3 | 跳過 | 3 6 2 5 4 1 |
| 2 | 5 | 4 > 3 | i=6，交換 A[6],A[5] | 3 6 2 5 1 4 |
| 3 | 4 | 5 > 3 | i=5，交換 A[5],A[4] | 3 6 2 1 5 4 |
| 4 | 3 | 2 ≤ 3 | 跳過 | 3 6 2 1 5 4 |
| 5 | 2 | 6 > 3 | i=4，交換 A[4],A[2] | 3 1 2 6 5 4 |
| 結束 | | | 交換 A[i-1]=A[3] 與 A[1] | **2 1 3 \| 6 5 4**，q=3 |

之後遞迴：[2 1] → pivot 2 → 1 2；[6 5 4] → pivot 6 → 4 5 6 → [4 5] → 4 5。最後 1 2 3 4 5 6（總比較 9 次）。

#### 2.4.2 複雜度
- **Best**（ch2 p.50）：每次切一半，$T(n)=2T(n/2)+O(n)=O(n\log n)$，共 $\log n$ 回合、每回合約 n 次比較。
- **Worst**（ch2 p.51）：資料**已排序或反向排序**，每次 pivot 是最小/最大，$T(n)=T(n-1)+O(n)$，$n+(n-1)+\dots+1=\frac{n(n+1)}2=O(n^2)$。
- **Average**（ch2 p.52–55）：$O(n\log n)$，推導如下（**很可能考**）。

#### 2.4.3 Average case 推導（ch2 p.52–55）

pivot 等機率落在第 s 位（s=1..n）：
$$T(n)=\frac1n\sum_{s=1}^n\big(T(s)+T(n-s)\big)+cn=\frac1n\big(2T(1)+\dots+2T(n-1)+T(n)\big)+cn,\quad T(0)=0$$
1. 兩邊乘 n，把 T(n) 移到左邊：$(n-1)T(n)=2T(1)+\dots+2T(n-1)+cn^2$ …(1)
2. 用 n-1 代入：$(n-2)T(n-1)=2T(1)+\dots+2T(n-2)+c(n-1)^2$ …(2)
3. (1)−(2)：$(n-1)T(n)-(n-2)T(n-1)=2T(n-1)+c(2n-1)$ ⇒ $(n-1)T(n)=nT(n-1)+c(2n-1)$
4. 兩邊除以 $n(n-1)$：$\dfrac{T(n)}{n}=\dfrac{T(n-1)}{n-1}+c\Big(\dfrac1n+\dfrac1{n-1}\Big)$
5. 展開（telescoping）到 $T(1)=0$：
$$\frac{T(n)}n=c\Big(\frac1n+\frac1{n-1}+\dots+\frac12\Big)+c\Big(\frac1{n-1}+\dots+1\Big)=c(H_n-1)+cH_{n-1}$$
6. $T(n)=2cnH_n-c-cn$；因為 $H_n=O(\log n)$ ⇒ **$T(n)=O(n\lg n)$**。

**去年 #14 的變形**：已知 $\dfrac{T(n)}{n+1}\le\dfrac{T(n-1)}{n}+\dfrac2n$，求 T(n)。
令 $S(n)=\frac{T(n)}{n+1}$，則 $S(n)\le S(n-1)+\frac2n$，一路展開：
$$S(n)\le S(1)+2\Big(\frac12+\frac13+\dots+\frac1n\Big)=\frac{T(1)}2+2(H_n-1)$$
$$\Rightarrow T(n)\le (n+1)\Big(\frac{T(1)}2+2H_n-2\Big)\le (n+1)\Big(\frac{T(1)}2+2(1+\ln n)-2\Big)=(n+1)\Big(\frac{T(1)}2+2\ln n\Big)$$
所以 $T(n)=O(n\lg n)$（若 $T(1)=0$，則 $T(n)\le 2(n+1)\ln n\approx1.39(n+1)\lg n$）。
**關鍵動作**：①兩邊都是「T 除以某個東西」→ 換變數 S；②telescoping 加總；③出現 $H_n$ → 用 §1.3 的 $H_n=O(\lg n)$。

### 2.5 ch2 後段（去年清單沒有，但今年有教；至少要知道結論）

| 主題 | 頁 | 重點 |
|---|---|---|
| 2-D rank finding | p.56–61 | A dominates B iff $a_1>b_1$ 且 $a_2>b_2$；rank = 被 x dominate 的點數。暴力 $O(n^2)$；divide & conquer：$T(n)=2T(n/2)+cn\log n=O(n\log^2n)$ |
| Lower bound 定義 | p.62–65 | 問題的 lower bound = 任何能解此問題的演算法所需的最少時間；不唯一；演算法複雜度 = lower bound 時稱 **optimal** |
| 排序 worst-case lower bound | p.66–74 | 比較型排序 = binary decision tree，n! 個葉子，深度 ≥ $\lceil\lg n!\rceil=\Omega(n\log n)$（積分法或 Stirling） |
| Knockout sort | p.75 | $(n-1)+(n-1)(\lceil\log n\rceil-1)=O(n\log n)$ |
| Heap sort | p.76–86 | 建 heap $O(n)$（≤ cn，2≤c≤4）；輸出 $O(n\log n)$；陣列 A(h) 的兒子 A(2h)、A(2h+1)，父 A(⌊h/2⌋)；**worst-case optimal** |
| 排序 average-case lower bound | p.87–91 | 平均 = external path length / n!；balanced tree 最小；$\Omega(n\log n)$ ⇒ quicksort、heapsort 都是 average-case optimal |
| Oracle | p.93–96 | 合併兩個長度 m 的有序序列，最難 case $a_1<b_1<a_2<\dots<b_m$，至少 $2m-1$ 次比較 ⇒ 傳統 merge 是 optimal |
| Problem transformation | p.97–101 | A ∝ B：sorting ∝ convex hull（$x\mapsto(x,x^2)$）、sorting ∝ Euclidean MST（$x\mapsto(x,0)$）⇒ 兩者 lower bound 皆 $\Omega(n\log n)$ |

---

## 3. 隨堂練習詳解

### 3-A. 9/21 隨堂練習

#### Q1. Give the definition of big O function.
**答**：$f(n)=O(g(n))$ if and only if there exist positive constants $c$ and $n_0$ such that $|f(n)|\le c|g(n)|$ for all $n\ge n_0$.
（參考 ch2 p.6）
> 拿分關鍵：①「存在」正常數 c、n₀；②**對所有** n ≥ n₀；③有絕對值；④不等號方向 ≤。

#### Q2. Show that $f(n)=4n^5-3n^4+12n^3-8n^2+4=O(n^5)$.
（參考 ch2 p.6 範例、p.9 多項式一般證明）

**證法一（投影片 p.9 套路，最安全）**：對 $n\ge1$，由三角不等式
$$|f(n)|\le4n^5+3n^4+12n^3+8n^2+4\le4n^5+3n^5+12n^5+8n^5+4n^5=31n^5$$
（因為 $n\ge1$ 時 $n^k\le n^5,\ k\le5$）。取 $c=31,\ n_0=1$，則 $|f(n)|\le c\,n^5,\ \forall n\ge n_0$ ⇒ $f(n)=O(n^5)$。∎

**證法二（c 比較小）**：先說明 $n\ge1$ 時 $f(n)>0$：$4n^5-3n^4=n^4(4n-3)>0$，$12n^3-8n^2=4n^2(3n-2)>0$，再加 4 > 0。所以 $|f(n)|=f(n)$，且丟掉負項：
$$f(n)\le4n^5+12n^3+4\le4n^5+12n^5+4n^5=20n^5,\quad n\ge1$$
取 $c=20,\ n_0=1$。∎

**證法三（投影片 p.6 的「猜 c 再驗證」法）**：猜 $c=5$，要證 $5n^5-f(n)\ge0$：
$$5n^5-f(n)=n^5+3n^4-12n^3+8n^2-4=n^3(n^2+3n-12)+(8n^2-4)$$
$n\ge3$ 時 $n^2+3n-12\ge9+9-12=6>0$、$8n^2-4>0$ ⇒ 成立。取 $c=5,\ n_0=3$。∎

> c、n₀ 不唯一，只要**有找到一組並證明成立**就對。考試建議用證法一或二，最不會出錯。

### 3-B. 10/12 隨堂練習（Insertion sort，參考 ch2 p.17–23）

#### Q1. 對 5, 2, 4, 6, 1, 3 做 insertion sort（step by step）
（這組數字和 ch2 p.17 投影片一模一樣）

| 回合 j | 插入 temp | 和誰比較（比較次數） | 右移次數 $d_j$ | 結果（`[ ]` 為已排序部分） |
|---|---|---|---|---|
| 初始 | | | | [5] 2 4 6 1 3 |
| j=2 | 2 | 2<5 移；i=0 停（1 次） | 1 | [2 5] 4 6 1 3 |
| j=3 | 4 | 4<5 移；4≥2 停（2 次） | 1 | [2 4 5] 6 1 3 |
| j=4 | 6 | 6≥5 停（1 次） | 0 | [2 4 5 6] 1 3 |
| j=5 | 1 | 1<6、1<5、1<4、1<2 皆移；i=0 停（4 次） | 4 | [1 2 4 5 6] 3 |
| j=6 | 3 | 3<6、3<5、3<4 移；3≥2 停（4 次） | 3 | [1 2 3 4 5 6] |

總比較 12 次；搬移次數 $M=2\times5+(1+1+0+4+3)=19$ 次。

#### Q2. Worst / best case 是什麼？
- **Best case**：輸入**已經由小到大排好**。每個 $x_j$ 只比一次就停，不需右移。
- **Worst case**：輸入**由大到小（反向）排好**。每個 $x_j$ 都要和前面全部 $j-1$ 個比、全部右移。

#### Q3. 給一個 best (worst) case 的資料序列
- Best：1, 2, 3, 4, 5, 6
- Worst：6, 5, 4, 3, 2, 1

#### Q4. 分析 best / worst / average 時間複雜度（以資料搬移數 M，ch2 p.21–23）
$M=\sum_{j=2}^n(2+d_j)=2(n-1)+\sum_{j=2}^n d_j$，其中 2 是 `temp:=x_j` 和 `x_{i+1}:=temp`，$d_j$ 是插入 $x_j$ 時往右搬的個數。

- **Best**：已排序，$d_j=0$ ⇒ $M=2(n-1)=O(n)$。
- **Worst**：反向排序，$d_j=j-1$ ⇒ $\sum_{j=2}^n(j-1)=\frac{n(n-1)}2$ ⇒ $M=2(n-1)+\frac{n(n-1)}2=O(n^2)$。
- **Average**（ch2 p.22）：插入 $x_j$ 時前面 $x_1..x_{j-1}$ 已排序，$x_j$ 是這 j 個數中第 1 大、第 2 大、…、最小的機率都是 $\frac1j$，對應搬移數 $2+0,\ 2+1,\ \dots,\ 2+(j-1)$：
$$\text{插入 }x_j\text{ 的期望搬移數}=\frac{2+3+\dots+(j+1)}{j}=\frac{1}{j}\Big(\frac{(j+1)(j+2)}{2}-1\Big)=\frac{j+3}{2}$$
$$M=\sum_{j=2}^n\frac{j+3}{2}=\frac12\Big[\Big(\frac{n(n+1)}2-1\Big)+3(n-1)\Big]=\frac{(n-1)(n+8)}{4}=O(n^2)$$

**結論**：best $O(n)$、worst $O(n^2)$、average $O(n^2)$（ch2 p.23）。
> 補充：用比較次數分析也一樣：best $n-1$、worst $\frac{n(n-1)}2$、average 約 $\frac{n^2}4$ ⇒ $O(n)$、$O(n^2)$、$O(n^2)$。

### 3-C. 10/19 隨堂練習（Binary search，參考 ch2 p.24–36，老師手寫 p.25–33）

陣列（index 1..8）：

| index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 值 | 1 | 3 | 5 | 7 | 9 | 10 | 12 | 16 |

#### Q1. 搜尋 0、3、17
**搜 0**：
| 步驟 | i | m | j=⌊(i+m)/2⌋ | a_j | 比較結果 |
|---|---|---|---|---|---|
| 1 | 1 | 8 | 4 | 7 | 0<7 → m=3 |
| 2 | 1 | 3 | 2 | 3 | 0<3 → m=1 |
| 3 | 1 | 1 | 1 | 1 | 0<1 → m=0 |
| | 1 | 0 | | | i>m，迴圈結束，輸出 **0（找不到）**，共 3 次比較 |

**搜 3**：
| 步驟 | i | m | j | a_j | 結果 |
|---|---|---|---|---|---|
| 1 | 1 | 8 | 4 | 7 | 3<7 → m=3 |
| 2 | 1 | 3 | 2 | 3 | 3=3 → **輸出 j=2**，共 2 次比較 |

**搜 17**：
| 步驟 | i | m | j | a_j | 結果 |
|---|---|---|---|---|---|
| 1 | 1 | 8 | 4 | 7 | 17>7 → i=5 |
| 2 | 5 | 8 | 6 | 10 | 17>10 → i=7 |
| 3 | 7 | 8 | 7 | 12 | 17>12 → i=8 |
| 4 | 8 | 8 | 8 | 16 | 17>16 → i=9 |
| | 9 | 8 | | | i>m，輸出 **0（找不到）**，共 4 次比較 |

#### Q2. 建立對應的二元搜尋樹並 level-order 編號
root = $a_{\lfloor(1+8)/2\rfloor}=a_4=7$；左子陣列 [1,3,5] 的中間 $a_2=3$；右子陣列 [9,10,12,16]（index 5..8）中間 $a_{\lfloor13/2\rfloor}=a_6=10$；依此類推。

```
level 1:               7 (1)
                     /       \
level 2:         3 (2)        10 (3)
                 /   \        /    \
level 3:     1 (4)  5 (5)  9 (6)  12 (7)
                                     \
level 4:                             16 (8)
```
括號內為編號 i：7→1, 3→2, 10→3, 1→4, 5→5, 9→6, 12→7, 16→8。

#### Q3. 驗證編號 i 的元素成功搜尋需要 $\lfloor\lg i\rfloor+1$ 次比較
比較次數 = 該節點所在 level（從 root 一路比下去）。

| 元素 | 編號 i | $\lfloor\lg i\rfloor+1$ | 實際比較路徑 | 次數 |
|---|---|---|---|---|
| 7 | 1 | 0+1=1 | 7 | 1 ✓ |
| 3 | 2 | 1+1=2 | 7→3 | 2 ✓ |
| 10 | 3 | 1+1=2 | 7→10 | 2 ✓ |
| 1 | 4 | 2+1=3 | 7→3→1 | 3 ✓ |
| 5 | 5 | 2+1=3 | 7→3→5 | 3 ✓ |
| 9 | 6 | 2+1=3 | 7→10→9 | 3 ✓ |
| 12 | 7 | 2+1=3 | 7→10→12 | 3 ✓ |
| 16 | 8 | 3+1=4 | 7→10→12→16 | 4 ✓ |

**原因**：binary search 樹是平衡的，第 k 層的編號範圍是 $2^{k-1}\sim2^k-1$，所以編號 i 在第 $k$ 層 ⇔ $2^{k-1}\le i<2^k$ ⇔ $k-1=\lfloor\lg i\rfloor$。

#### Q4. 成功/失敗搜尋的 worst case，並驗證最大比較次數 = $\lfloor\lg n\rfloor+1$
- **成功搜尋 worst case**：搜 **16**，路徑 7→10→12→16，**4 次**。
- **失敗搜尋 worst case**：X 落在 12 與 16 之間或大於 16（例如 **13** 或 **17**），一樣比到 16 才確定找不到，**4 次**。（若 X 落在其他空隙，如 X<1、1<X<3…，只要 3 次。）
- 驗證：$n=8$，$\lfloor\lg8\rfloor+1=3+1=4$ ✓ = 樹高。

#### Q5. 證明成功搜尋總比較次數 $\sum_{i=1}^n(\lfloor\lg i\rfloor+1)\le n\lg n+(1-\frac1{\ln2})n+\lg n+\frac1{\ln2}$
（老師手寫推導 ch2 p.27–29，圖解 p.33）
$$\sum_{i=1}^n(\lfloor\lg i\rfloor+1)=\sum_{i=1}^n\lfloor\lg i\rfloor+n\le\sum_{i=1}^{n}\lg i+n=\Big(\sum_{i=1}^{n-1}\lg i\Big)+\lg n+n$$
因為 $\lg x$ 遞增，寬度 1 的矩形 $\lg i\le\int_i^{i+1}\lg x\,dx$（p.33 的圖），所以
$$\sum_{i=1}^{n-1}\lg i\le\int_1^n\lg x\,dx=\frac1{\ln2}\int_1^n\ln x\,dx=\frac1{\ln2}\Big[x\ln x-x\Big]_1^n=\frac1{\ln2}(n\ln n-n+1)$$
$$=n\frac{\ln n}{\ln2}-\frac{n}{\ln2}+\frac1{\ln2}=n\lg n-\frac1{\ln2}n+\frac1{\ln2}$$
代回：
$$\text{總和}\le n\lg n-\frac{1}{\ln2}n+\frac1{\ln2}+\lg n+n=n\lg n+\Big(1-\frac1{\ln2}\Big)n+\lg n+\frac1{\ln2}\quad\text{…①}$$
∎
> 要會：①換底 $\lg x=\frac{\ln x}{\ln2}$；②$\int\ln x\,dx=x\ln x-x$（分部積分）。

#### Q6. 證明失敗搜尋總比較次數 $\le(\lfloor\lg n\rfloor+1)(n+1)\le n\lg n+n+\lg n+1$
（老師手寫 ch2 p.29 下半）
- n 個元素的有序陣列，失敗的情況共 **n+1 種**（X 落在 n+1 個空隙：小於 $a_1$、$a_1\sim a_2$ 之間、…、大於 $a_n$），對應樹的 n+1 個外部節點。
- 每一種失敗搜尋都從 root 比到某個葉子為止，最多比 樹高 $=\lfloor\lg n\rfloor+1$ 次。
$$\text{總和}\le(\lfloor\lg n\rfloor+1)(n+1)\le(\lg n+1)(n+1)=n\lg n+n+\lg n+1\quad\text{…②}$$
（用到 $\lfloor\lg n\rfloor\le\lg n$。）∎

#### Q7. 證明平均複雜度 $O(\lg n)$
（老師手寫 ch2 p.30–32）總共 $n+(n+1)=2n+1$ 種情況，平均 = (① + ②) / (2n+1)：
$$A(n)\le\frac{2n\lg n+\big(2-\frac1{\ln2}\big)n+2\lg n+\big(1+\frac1{\ln2}\big)}{2n+1}$$
當 $n\ge2$ 時 $\lg n\ge1$，所以 $n\le n\lg n$、$\lg n\le n\lg n$、$1\le n\lg n$（且各係數皆為正：$2-\frac1{\ln2}\approx0.557>0$），把每一項都放大成 $n\lg n$，分母縮小成 $2n$：
$$A(n)<\frac{\big[2+(2-\frac1{\ln2})+2+(1+\frac1{\ln2})\big]n\lg n}{2n}=\frac{7n\lg n}{2n}=\frac72\lg n$$
取 $c=\frac72,\ n_0=2$ ⇒ $A(n)=O(\lg n)$。∎
> 漂亮之處：$\frac1{\ln2}$ 正負抵消，c 剛好是 7/2。另外 Best $O(1)$、Worst $\lfloor\lg n\rfloor+1=O(\lg n)$。
> 投影片另一種做法（p.35–36）：假設 $n=2^k-1$，$\sum_{i=1}^ki2^{i-1}=2^k(k-1)+1$，$A(n)\approx k=O(\log n)$。

---

## 4. 預測題（去年考過、今年隨堂還沒出的）

> ⛔ 本節的 selection sort、quick sort **不在本次期中範圍**，留給期末。

### 4-1. Selection sort：5, 2, 4, 6, 1, 3 step by step
| 回合 j | 在 a_j..a_6 找最小 | flag 改變 | 交換 | 結果 |
|---|---|---|---|---|
| 1 | f:1(5)→2(2)→5(1)，最小 1 | 2 | a1↔a5 | 1 2 4 6 5 3 |
| 2 | f:2(2)，沒更小 | 0 | 不動 | 1 2 4 6 5 3 |
| 3 | f:3(4)→6(3)，最小 3 | 1 | a3↔a6 | 1 2 3 6 5 4 |
| 4 | f:4(6)→5(5)→6(4)，最小 4 | 2 | a4↔a6 | 1 2 3 4 5 6 |
| 5 | f:5(5)，6>5 | 0 | 不動 | 1 2 3 4 5 6 |

比較次數 = 5+4+3+2+1 = 15 = $\frac{6\cdot5}2$（不管資料怎麼排都一樣）。

### 4-2. Quick sort：5, 2, 4, 6, 1, 3（用 §2.4.1 的版本）
**第一次 partition**，pivot x=5，i=7：
| j | A[j] | 動作 | 陣列 |
|---|---|---|---|
| 6 | 3 ≤ 5 | 跳過 | 5 2 4 6 1 3 |
| 5 | 1 ≤ 5 | 跳過 | 5 2 4 6 1 3 |
| 4 | 6 > 5 | i=6，A[6]↔A[4] | 5 2 4 3 1 6 |
| 3 | 4 ≤ 5 | 跳過 | 5 2 4 3 1 6 |
| 2 | 2 ≤ 5 | 跳過 | 5 2 4 3 1 6 |
| 結束 | | A[i-1]=A[5] ↔ A[1] | **1 2 4 3 \| 5 \| 6**，q=5 |

**遞迴左半 [1 2 4 3]**，pivot=1：j=4,3,2 皆 >1，i 依序變 4,3,2（都是自己跟自己交換），最後 A[1]↔A[1] → `1 | 2 4 3`，q=1。
**遞迴 [2 4 3]**，pivot=2：同理 → `2 | 4 3`。
**遞迴 [4 3]**，pivot=4：j=4，3≤4 跳過；A[i-1]=A[4]↔A[3] → `3 4`。
右半 [6] 只有一個元素，不用做。結果 **1 2 3 4 5 6**，總比較 5+3+2+1 = 11 次。

> 觀察：左半 [1 2 4 3] 幾乎排好，pivot 每次都是最小 → 只切掉一個 → 這就是 worst case 的行為。對 1 2 3 4 5 6 做 quicksort 總比較 5+4+3+2+1=15=$\frac{n(n-1)}2$。

### 4-3. 其他可能考的定義題
- 「什麼時候 quicksort 是 worst case？」→ 已排序或反向排序（pivot 永遠最小/最大）。
- 「quick sort best case？」→ 每次 pivot 剛好是中位數，切成等大兩半。
- 「什麼是 optimal algorithm？」→ 時間複雜度等於該問題的 lower bound（ch2 p.65）。

---

## 5. 考前 Checklist 與建議

**計算技巧必練**
- [ ] 證 O(·)：寫出定義 → 不等式放大 → **明確寫出 c 與 n₀** → 寫「∀n≥n₀」。
- [ ] $\sum_{i=1}^n i=\frac{n(n+1)}2$、$\sum_{j=2}^n(j-1)=\frac{n(n-1)}2$
- [ ] 換底：$\lg x=\frac{\ln x}{\ln 2}$；$\int\ln x\,dx=x\ln x-x$；$\int\frac1x dx=\ln x$
- [ ] 用積分夾和：遞增函數 $\sum_{i=1}^{n-1}f(i)\le\int_1^nf(x)dx$；遞減函數 $\sum_{k=2}^nf(k)\le\int_1^nf(x)dx$
- [ ] $\lfloor\lg i\rfloor$ 快速算：$\lfloor\lg 1\rfloor=0$，2~3→1，4~7→2，8~15→3

**容易丟分的地方**
1. **用老師版本的演算法**做 step by step：binary search 是 $j=\lfloor(i+m)/2\rfloor$（向下取整），每一步把 i、m、j 都寫出來。網路/其他課本版本中間過程會不一樣。
2. **計數單位要講清楚**：insertion sort 投影片是用「資料搬移次數」（含 temp 進出 2 次）；題目若問比較次數，就用比較次數分析（best $n-1$、worst $\frac{n(n-1)}2$）。
3. Big O 證明最後一定要寫出 c、n₀ 的具體數值，且 n₀ 要讓所有用到的不等式成立（例如用到 $1\le\lg n$ 就要 n₀≥2）。
4. 題目用英文，作答可用中文，但定義建議背英文原句。

**時間分配建議（若剩一週左右）**
1. 第 1–2 天：§3 全部隨堂練習自己蓋住答案重寫一次（佔 70–80 分）。
2. 第 3 天：binary search 換不同長度的陣列（n=7、9、10、12、15）練畫樹、編號、數比較次數；insertion sort 換數列練。
3. 第 4 天：binary search 的 #5、#6、#7 三個證明和 $H_n=O(\lg n)$ 各默寫一次。
4. 剩下時間：寫模擬考，錯的題目回頭重寫。
