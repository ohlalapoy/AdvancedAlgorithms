This Repo is for CS612 - Advanced Computer Algorithms during my Master's degree
- Lecture from CS612 class
- Self Learning from https://www.youtube.com/watch?v=8hly31xKli0&t=345s
- https://tira.mooc.fi/spring-2025/chap01/

# สรุปคณิตศาสตร์สำหรับ Advanced Algorithms CS612  

เอกสารนี้รวบรวมเครื่องมือคณิตศาสตร์หลักที่ใช้บ่อยในการวิเคราะห์ความซับซ้อนของอัลกอริทึม (Complexity Analysis) เช่น Limit, Logarithm, Summation, และ Recurrence Relations

---

## 1. Asymptotic Notation (สัญกรณ์เชิงเส้นกำกับ)

ใช้อธิบายพฤติกรรมของฟังก์ชันเมื่อ input (n) มีค่าเข้าใกล้อนันต์

| สัญกรณ์ | ความหมาย | นิยาม (คร่าวๆ) |
|---|---|---|
| **Big-O** — $O(g(n))$ | ขอบเขตบน (worst case) | มี $c, n_0 > 0$ ที่ $f(n) \le c \cdot g(n)$ สำหรับ $n \ge n_0$ |
| **Big-Omega** — $\Omega(g(n))$ | ขอบเขตล่าง (best case) | มี $c, n_0 > 0$ ที่ $f(n) \ge c \cdot g(n)$ สำหรับ $n \ge n_0$ |
| **Big-Theta** — $\Theta(g(n))$ | ขอบเขตบน-ล่างพร้อมกัน (tight bound) | $f(n) = O(g(n))$ และ $f(n) = \Omega(g(n))$ |
| **Little-o** — $o(g(n))$ | เติบโตช้ากว่าอย่างเคร่งครัด | $\lim_{n\to\infty} \frac{f(n)}{g(n)} = 0$ |
| **Little-omega** — $\omega(g(n))$ | เติบโตเร็วกว่าอย่างเคร่งครัด | $\lim_{n\to\infty} \frac{f(n)}{g(n)} = \infty$ |

**อันดับการเติบโต (จากช้าไปเร็ว):**
$$1 < \log\log n < \log n < n^{\epsilon} < n < n\log n < n^2 < n^3 < 2^n < n! < n^n$$

---

## 2. Limit (ลิมิต) — ใช้เปรียบเทียบอัตราการเติบโต

### 2.1 วิธีใช้ Limit เปรียบเทียบ $f(n)$ กับ $g(n)$

$$\lim_{n\to\infty} \frac{f(n)}{g(n)} = \begin{cases} 0 & \Rightarrow f(n) = o(g(n)) \\ c \ (0 < c < \infty) & \Rightarrow f(n) = \Theta(g(n)) \\ \infty & \Rightarrow f(n) = \omega(g(n)) \end{cases}$$

### 2.2 L'Hôpital's Rule (กฎโลปิตาล)

ใช้เมื่อ limit อยู่ในรูป indeterminate form ($\frac{\infty}{\infty}$ หรือ $\frac{0}{0}$):

$$\lim_{n\to\infty} \frac{f(n)}{g(n)} = \lim_{n\to\infty} \frac{f'(n)}{g'(n)}$$

**ตัวอย่าง:** เทียบ $\log n$ กับ $n$
$$\lim_{n\to\infty} \frac{\log n}{n} = \lim_{n\to\infty} \frac{1/n}{1} = 0 \quad \Rightarrow \quad \log n = o(n)$$

### 2.3 Limit ที่เจอบ่อยในวิชานี้

- $\lim_{n\to\infty} \frac{\log n}{n^\epsilon} = 0$ สำหรับ $\epsilon > 0$ (log โตช้ากว่า polynomial ใดๆ)
- $\lim_{n\to\infty} \frac{n^k}{c^n} = 0$ สำหรับ $c > 1$ (polynomial โตช้ากว่า exponential)
- $\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e$

---

## 3. Logarithm (ลอการิทึม)

### 3.1 กฎพื้นฐาน

| กฎ | สูตร |
|---|---|
| Product | $\log_b(xy) = \log_b x + \log_b y$ |
| Quotient | $\log_b(x/y) = \log_b x - \log_b y$ |
| Power | $\log_b(x^k) = k\log_b x$ |
| Change of base | $\log_b x = \dfrac{\log_k x}{\log_k b}$ |
| Inverse | $b^{\log_b x} = x$, และ $\log_b(b^x) = x$ |

> **หมายเหตุสำคัญ:** ในการวิเคราะห์อัลกอริทึม ฐานของ log มักไม่สำคัญ เพราะ $\log_a n = \Theta(\log_b n)$ เสมอ (ต่างกันแค่ค่าคงที่) — ดังนั้นมักเขียนแค่ $\log n$ โดยไม่ระบุฐาน

### 3.2 ที่มาของ log ใน Algorithm Analysis

- **Divide and Conquer**: ถ้าปัญหาขนาด $n$ ถูกแบ่งครึ่งทุกครั้ง จะได้ความลึก $\log_2 n$ level (เช่น Binary Search, Merge Sort)
- **Binary representation**: จำนวน bit ที่ใช้แทนเลข $n$ คือ $\lceil \log_2 n \rceil + 1$
- **Balanced tree height**: ต้นไม้ balanced ที่มี $n$ nodes จะมีความสูง $O(\log n)$

---

## 4. Summation (ผลรวม / Series)

### 4.1 Arithmetic Series (อนุกรมเลขคณิต)
$$\sum_{i=1}^{n} i = 1 + 2 + \cdots + n = \frac{n(n+1)}{2} = \Theta(n^2)$$

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} = \Theta(n^3)$$

### 4.2 Geometric Series (อนุกรมเรขาคณิต)
$$\sum_{i=0}^{n} x^i = \frac{x^{n+1}-1}{x-1} \quad (x \ne 1)$$

กรณี $|x| < 1$ และ $n \to \infty$:
$$\sum_{i=0}^{\infty} x^i = \frac{1}{1-x}$$

### 4.3 Harmonic Series
$$\sum_{i=1}^{n} \frac{1}{i} \approx \ln n + \gamma = \Theta(\log n)$$

### 4.4 เทคนิคการประมาณผลรวมด้วย Integral
$$\int_{1}^{n} f(x)\,dx \le \sum_{i=1}^{n} f(i) \le f(1) + \int_{1}^{n} f(x)\,dx$$

---

## 5. Recurrence Relations (สมการเวียนบังเกิด)

ใช้วิเคราะห์อัลกอริทึมแบบ recursive เช่น Divide and Conquer

### 5.1 Master Theorem

สำหรับ $T(n) = aT(n/b) + f(n)$ โดยที่ $a \ge 1, b > 1$:

ให้ $c_{crit} = \log_b a$ แล้วเทียบ $f(n)$ กับ $n^{c_{crit}}$:

| กรณี | เงื่อนไข | ผลลัพธ์ |
|---|---|---|
| Case 1 | $f(n) = O(n^{c_{crit} - \epsilon})$ | $T(n) = \Theta(n^{c_{crit}})$ |
| Case 2 | $f(n) = \Theta(n^{c_{crit}})$ | $T(n) = \Theta(n^{c_{crit}} \log n)$ |
| Case 3 | $f(n) = \Omega(n^{c_{crit} + \epsilon})$ (+ regularity condition) | $T(n) = \Theta(f(n))$ |

**ตัวอย่าง:** Merge Sort — $T(n) = 2T(n/2) + \Theta(n)$
- $a=2, b=2 \Rightarrow c_{crit} = \log_2 2 = 1$
- $f(n) = \Theta(n) = \Theta(n^1)$ → เข้า **Case 2**
- ผลลัพธ์: $T(n) = \Theta(n\log n)$

### 5.2 วิธี Substitution
เดาคำตอบ แล้วพิสูจน์ด้วย induction ว่า $T(n) \le c \cdot g(n)$

### 5.3 วิธี Recursion Tree
วาดต้นไม้ของการเรียก แล้วรวมค่า cost ทีละ level แล้วบวกทุก level เข้าด้วยกัน

---

## 6. Exponent Rules (กฎเลขยกกำลัง)

| กฎ | สูตร |
|---|---|
| Product | $x^a \cdot x^b = x^{a+b}$ |
| Quotient | $x^a / x^b = x^{a-b}$ |
| Power of power | $(x^a)^b = x^{ab}$ |
| Negative | $x^{-a} = 1/x^a$ |

---

## 7. ตารางเทียบ Growth Rate ที่ใช้บ่อย

| ชื่อ | Notation | ตัวอย่าง Algorithm |
|---|---|---|
| Constant | $O(1)$ | Array access |
| Logarithmic | $O(\log n)$ | Binary Search |
| Linear | $O(n)$ | Linear Search |
| Linearithmic | $O(n\log n)$ | Merge Sort, Heap Sort |
| Quadratic | $O(n^2)$ | Bubble Sort, Insertion Sort |
| Cubic | $O(n^3)$ | Matrix Multiplication (naive) |
| Exponential | $O(2^n)$ | Brute-force Subset Sum |
| Factorial | $O(n!)$ | Brute-force TSP |

---

## 8. Tips ในการสอบ/แก้โจทย์

1. เวลาเจอ recurrence ให้เช็คก่อนว่าเข้ารูป Master Theorem ได้ไหม ถ้าไม่ได้ (เช่น $f(n)$ ไม่ polynomial) ให้ใช้ Recursion Tree หรือ Substitution แทน
2. เวลาเปรียบเทียบฟังก์ชัน 2 ตัวว่าใครโตเร็วกว่า ให้ใช้ limit ของอัตราส่วน (ข้อ 2.1) เป็นวิธีที่เชื่อถือได้ที่สุด
3. อย่าลืมว่า log ไม่ต้องระบุฐานในการวิเคราะห์ Big-O เพราะฐานต่างกันแค่คูณด้วยค่าคงที่
4. เวลาคำนวณ summation ที่ซับซ้อน ลองแตกเป็น arithmetic + geometric ผสมกัน หรือใช้ integral bound ประมาณ
