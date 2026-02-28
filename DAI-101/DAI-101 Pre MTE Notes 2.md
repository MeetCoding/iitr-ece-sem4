### I. Data Foundations & Preparation (The "Pre-Processing" Umbrella)

- **Data Types & Structure**
    
    - **The Data Matrix:** n Rows (Observations) $\times$ m Columns (Features).
        
    - **Data Levels:** Numeric (Discrete/Continuous) vs. Categorical (Nominal/Ordinal).
    - Curse of Dimensionality, Sparcity (Only presence counts), Resolution (Scale defines the pattern)
		
- **Data Cleaning (The "Scrubbing" Phase)**
    
    - **Finding Outliers:** Z-Score ($>3$ or $<-3$), IQR Method (values outside $1.5 \times IQR$), and Scatter plots.
        
    - **Handling Missing Values:** Deletion (Listwise/Pairwise) or Imputation (Mean/Median/Mode, or Predictive modeling).
        
    - **Removing Duplicates:** Exact match identification and "Fuzzy matching" for near-duplicates.
        
    - **Noise Removal:** Equi Width and Equi Depth Binning (Smoothing), Regression (fitting a line to smooth data), and Clustering to find outliers.
        
- **Data Transformation**
    
    - **Normalization/Scaling:** Min-Max scaling (0 to 1) or Z-score Standardization (Mean=0, SD=1).
        
    - **Aggregation:** Summarizing data (e.g., Daily sales $\rightarrow$ Monthly sales).
        
    - **Discretization:** Converting continuous attributes into categorical bins.
        
    - **Generalization:** Replacing low-level concepts with higher-level ones (e.g., "Street" $\rightarrow$ "City").
        
- **Data Reduction**
    
    - **Dimensionality Reduction:** Reducing features via **PCA (Principal Component Analysis)**.
        
    - **Numerosity Reduction:** Replacing data with smaller models (Linear Regression, Multiple Regression, Log-Linear Model, Histograms, or Clustering).
        
    - **Data Compression:** Encoding techniques to reduce file size.
        

---

### II. Statistical Analysis (The "Inference" Umbrella)

- **Descriptive Statistics (Summary Metrics)**
    
    - **Central Tendency:** Arithmetic/Geometric Mean, Median, Mode.
        
    - **Dispersion:** Range, Variance ($\sigma^2$), Standard Deviation ($\sigma$), and Interquartile Range (IQR).
        
- **Inferential Statistics (Generalizing to Population)**
    
    - **Estimates:** Confidence Intervals (CI) and Point Estimates.
        
    - **Theoretical Core:** The **Bias-Variance Trade-off** (Underfitting vs. Overfitting).
        
- **Hypothesis Testing (The Decision Framework)**
    
    - **The Logic:** Null Hypothesis ($H_0$) vs. Alternative ($H_1$), p-values (Threshold usually 0.05). Type I and Type II Errors
        
    - **Parametric Tests (Assumes Normal Distribution):**
        
        - **t-test:** Comparing means of 1 or 2 groups.
            
        - **ANOVA:** Comparing means of $3+$ groups.
            
        - **Correlation Coefficient (Pearson):** Linear relationship between two continuous variables.
            
    - **Non-Parametric Tests (No Distribution Assumption):**
        
        - **Mann-Whitney U Test:** Non-parametric alternative to the t-test (ranks instead of means).
            
        - **Chi-Square ($\chi^2$):** Association between categorical variables.


---

### III. Exploratory Data Analysis (The "Visualization" Umbrella)

- **Univariate Analysis (One Variable)**
    
    - **Plots:** Histograms, Pie Charts, Box-Whisker plots.
        
    - **Goal:** Understand the distribution, spread, and central tendency.
        
- **Bivariate/Multivariate Analysis (Two or More Variables)**
    
    - **Relationship Plots:** Scatterplots (Correlation), Segmented Bar plots, Mosaic plots.
        
    - **Distribution Comparison:** Violin plots (Density + Box plot), Funnel charts.
        
    - **Matrix/High-Dim Visualization:** Heatmaps (Correlation matrices) and PCA plots (Cluster visualization).

---

| **Concept**          | **Formula / Definition**               | **Use Case**                                |
| -------------------- | -------------------------------------- | ------------------------------------------- |
| **Mean ($\bar{x}$)** | $\frac{\sum x_i}{n}$                   | Average value; sensitive to outliers.       |
| **Median**           | Middle value of sorted data            | Robust measure of center for skewed data.   |
| **Mode**             | Most frequent value                    | Used for categorical or discrete data.      |
| **Variance ($s^2$)** | $\dfrac{\sum (x_i - \bar{x})^2}{n-1}$  | Average squared deviation from the mean.    |
| **Std. Dev ($s$)**   | $\sqrt{s^2}$                           | Average distance of data from the mean.     |
| **Z-Score**          | $z = \dfrac{x - \mu}{\sigma}$          | Standardizing data; identifies outliers ($  |
| **IQR**              | $Q3 - Q1$                              | Measures spread of middle 50% of data.      |
| **Outlier (IQR)**    | $[Q1 - 1.5(IQR)]$ OR $[Q3 + 1.5(IQR)]$ | Standard "fences" to detect extreme values. |

| **Test**                      | **Formula / Test Statistic**                                                                            | **Solved Example Snippet**                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **One-Sample t-test**         | $t = \dfrac{\bar{x} - \mu}{s / \sqrt{n}}$                                                               | **Ex:** Average height is claimed to be 170cm. Sample mean is 175cm. Test if the claim is wrong. |
| **Indep. 2-Sample t-test**    | $t = \dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$                     | **Ex:** Group A (Red bull) vs Group B (Coffee) reaction times. Compare their means.              |
| **Paired t-test**             | $t = \dfrac{\bar{d}}{s_d / \sqrt{n}}$ ($d$ = difference)                                                | **Ex:** Blood pressure of same patient _Before_ and _After_ a pill.                              |
| **ANOVA (F-test)**            | $F = \dfrac{MS_{between}}{MS_{within}}$                                                                 | **Ex:** Testing if 3 different fertilizers result in different crop yields.                      |
| **Pearson Correlation ($r$)** | $r = \dfrac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$ | **Ex:** Relationship between hours studied and marks obtained (-1 to +1 scale).                  |
| **Mann-Whitney U**            | $U = n_1n_2 + \dfrac{n_1(n_1+1)}{2} - R_1$                                                              | **Ex:** Comparing "Happiness score" (1-10) between two cities where data isn't normal.           |
| **Chi-Square ($\chi^2$)**     | $\chi^2 = \sum \dfrac{(O - E)^2}{E}$                                                                    | **Ex:** Is there a link between Gender (M/F) and Choice of Major (CS/Math)?                      |

---

## 1. One-Sample t-test

**Scenario:** A company claims their lightbulbs last **2000 hours** ($\mu$). You test **16 bulbs** ($n$) and find a sample mean of **1950 hours** ($\bar{x}$) with a standard deviation ($s$) of **100 hours**.

- **Hypotheses:** $H_0: \mu = 2000$; $H_1: \mu \neq 2000$
    
- **Formula:** $t = \frac{\bar{x} - \mu}{s / \sqrt{n}}$
    
- **Calculation:**
    
    1. Standard Error: $SE = 100 / \sqrt{16} = 100 / 4 = 25$
        
    2. $t = \frac{1950 - 2000}{25} = \frac{-50}{25} = -2.0$
        
- **Decision:** If critical $t$ (from table) at $df=15$ is $2.131$, and our $|-2.0| < 2.131$, we **Fail to Reject $H_0$**. The claim holds.
    

---

## 2. Independent Two-Sample t-test

**Scenario:** Comparing exam scores of Group A (10 students) and Group B (10 students).

- **Group A:** Mean ($\bar{x}_1$) = 85, Variance ($s_1^2$) = 25
    
- **Group B:** Mean ($\bar{x}_2$) = 80, Variance ($s_2^2$) = 16
    
- **Hypotheses:** $H_0: \mu_1 = \mu_2$; $H_1: \mu_1 \neq \mu_2$
    
- **Formula:** $t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$
    
- **Calculation:**
    
    1. Denominator: $\sqrt{\frac{25}{10} + \frac{16}{10}} = \sqrt{2.5 + 1.6} = \sqrt{4.1} \approx 2.02$
        
    2. $t = \frac{85 - 80}{2.02} = \frac{5}{2.02} = 2.47$
        
- **Decision:** Since $2.47 > 2.10$ (approx critical value), we **Reject $H_0$**. Group A performed significantly better.
    

---

## 3. Paired t-test

**Scenario:** Weight of 5 people before and after a 1-week diet.

- **Differences (Before - After):** 2kg, 3kg, 1kg, 4kg, 0kg.
    
- **Mean Difference ($\bar{d}$):** $(2+3+1+4+0)/5 = 2.0$
    
- **Std Dev of Differences ($s_d$):** Let's assume calculated $s_d = 1.58$
    
- **Formula:** $t = \frac{\bar{d}}{s_d / \sqrt{n}}$
    
- **Calculation:**
    
    1. $t = \frac{2.0}{1.58 / \sqrt{5}} = \frac{2.0}{1.58 / 2.23} = \frac{2.0}{0.70} = 2.85$
        
- **Decision:** Reject $H_0$ if $2.85 >$ critical table value. The diet is effective.
    

---

## 4. Chi-Square ($\chi^2$) Test of Independence

**Scenario:** Is "Drinking Coffee" related to "Passing the Exam"?

|               | Pass     | Fail     | Total   |
| :------------ | :------- | :------- | :------ |
| **Coffee**    | 40 (Obs) | 10 (Obs) | **50**  |
| **No Coffee** | 20 (Obs) | 30 (Obs) | **50**  |
| **Total**     | **60**   | **40**   | **100** |

- **Step 1 (Expected Value for Coffee-Pass):** $E = \frac{RowTotal \times ColTotal}{GrandTotal} = \frac{50 \times 60}{100} = 30$
    
- **Step 2 (Apply $\sum \frac{(O-E)^2}{E}$ to all 4 cells):**
    
    1. (Coffee-Pass): $(40-30)^2 / 30 = 100/30 = 3.33$
        
    2. (Coffee-Fail): $(10-20)^2 / 20 = 100/20 = 5.00$
        
    3. (NoCoffee-Pass): $(20-30)^2 / 30 = 100/30 = 3.33$
        
    4. (NoCoffee-Fail): $(30-20)^2 / 20 = 100/20 = 5.00$
        
- **Sum:** $\chi^2 = 3.33 + 5.00 + 3.33 + 5.00 = 16.66$
    
- **Decision:** The critical value for $df=1$ is 3.84. Since **16.66 > 3.84**, we **Reject $H_0$**. Coffee and Passing are related.
    

---

## 5. ANOVA (One-Way)

**Scenario:** Testing 3 study methods (A, B, C) with 3 students each.

- **SST (Total Sum of Squares):** 100 (Variance of all scores)
    
- **SSW (Within-Group Variance):** 40 (Variance inside each study group)
    
- **SSB (Between-Group Variance):** $SST - SSW = 60$
    
- **Calculation:**
    
    1. $df_{between} = k - 1 = 3 - 1 = 2$
        
    2. $df_{within} = N - k = 9 - 3 = 6$
        
    3. $MSB = 60 / 2 = 30$; $MSW = 40 / 6 = 6.67$
        
    4. $F = MSB / MSW = 30 / 6.67 = 4.49$
        
- **Decision:** Compare $F=4.49$ to F-table. If $F > F_{crit}$, at least one method is different.
    

---

## 6. Mann-Whitney U Test (Non-Parametric)

**Scenario:** Comparing "Happiness Rank" of Group A (3 people) and Group B (3 people).

- **Data (Ranks):** Group A: [1, 2, 4] | Group B: [3, 5, 6]
    
- **Sum of Ranks ($R_1$ for A):** $1+2+4 = 7$
    
- **Calculation:**
    
    1. $U_1 = n_1n_2 + \frac{n_1(n_1+1)}{2} - R_1$
        
    2. $U_1 = (3 \times 3) + \frac{3(4)}{2} - 7 = 9 + 6 - 7 = 8$
        
    3. $U_2 = (n_1 \times n_2) - U_1 = 9 - 8 = 1$
        
- **Final $U$:** Use the **smaller** value, so $U = 1$.
    
- **Decision:** Consult the U-table. A very small $U$ (like 1) usually means the groups are significantly different.