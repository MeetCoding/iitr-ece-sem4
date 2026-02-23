Since you're preparing for a high-level exam on these topics, we need to move beyond just "knowing" the definitions and focus on the **mathematical intuition** and **decision-making logic** behind each tool.

Here is your master roadmap, broken down into logical Units, Chapters, and Bite-sized Lessons.

---

## Unit 1: The Bedrock (Data Analysis Foundation)

*Focus: Understanding the "physics" of your data before you touch a single formula.*

### Chapter 1: Data Anatomy

* **Lesson 1.1: The Data Matrix.** Understanding rows (observations) vs. columns (features/variables) and the  dimensionality.
* **Lesson 1.2: Numerical Data.** Discrete (countable) vs. Continuous (measurable).
* **Lesson 1.3: Categorical Data.** Nominal (labels) vs. Ordinal (ranked labels).
* **Lesson 1.4: Dataset Structures.** Wide vs. Long formats and when to use each.

### Chapter 2: Data Preparation & Pre-processing

* **Lesson 2.1: Data Cleaning.** Identifying and handling missing values (Imputation vs. Deletion) and outliers.
* **Lesson 2.2: Data Reduction.** Concept of Feature Selection (keeping the best) vs. Feature Extraction (creating new ones).
* **Lesson 2.3: Transformation - Scaling.** Standardizing (Z-score) vs. Normalizing (Min-Max).
* **Lesson 2.4: Transformation - Distribution.** Log transformations and Box-Cox to handle skewed data.

---

## Unit 2: Descriptive & Inferential Statistics

*Focus: Moving from "What does the data look like?" to "What does the data mean?"*

### Chapter 3: Measures of Central Tendency & Dispersion

* **Lesson 3.1: The Means.** Arithmetic Mean () vs. Geometric Mean (for growth rates/ratios).
* **Lesson 3.2: Median & Mode.** When the median is more "honest" than the mean (robustness to outliers).
* **Lesson 3.3: Range & Variance.** Calculating  and understanding the "average squared deviation."
* **Lesson 3.4: Standard Deviation (SD).** Interpreting  in the context of the Normal Distribution (68-95-99.7 rule).
* **Lesson 3.5: Interquartile Range (IQR).** Calculating  and its role in boxplot construction.

### Chapter 4: Hypothesis Testing & Intervals

* **Lesson 4.1: The Null () vs. Alternative ().** Framing the "burden of proof."
* **Lesson 4.2: P-values.** Understanding the probability of seeing your data if  is true.
* **Lesson 4.3: Type I and Type II Errors.**  (False Positive) vs.  (False Negative).
* **Lesson 4.4: Confidence Intervals (CI).** Calculating the margin of error: .
* **Lesson 4.5: Bias-Variance Trade-off.** Understanding underfitting (high bias) vs. overfitting (high variance).

### Chapter 5: Parametric vs. Non-Parametric Tests

* **Lesson 5.1: The T-test.** One-sample, Independent two-sample, and Paired T-tests.
* **Lesson 5.2: ANOVA (Analysis of Variance).** Comparing means across  groups using the F-statistic.
* **Lesson 5.3: Chi-Square Test.** Test of Independence and Goodness-of-fit for categorical data.
* **Lesson 5.4: Mann-Whitney U Test.** The non-parametric alternative to the T-test when data isn't normal.

---

## Unit 3: Exploratory Data Analysis (EDA) & Visualization

*Focus: Visualizing relationships and reducing complexity.*

### Chapter 6: Bivariate & Multivariate Analysis

* **Lesson 6.1: Correlation Coefficient ().** Pearson (linear) vs. Spearman (rank-based) correlation.
* **Lesson 6.2: Scatterplots.** Identifying clusters, non-linear trends, and heteroscedasticity.
* **Lesson 6.3: Contingency Tables.** Calculating marginal and conditional probabilities.

### Chapter 7: The Visualization Catalog

* **Lesson 7.1: Distribution Visuals.** Histograms vs. Violin Plots (showing density + IQR).
* **Lesson 7.2: Categorical Visuals.** Segmented Bar Plots, Mosaic Plots, and the "danger" of Pie Charts.
* **Lesson 7.3: Comparison Visuals.** Box-and-Whisker (identifying outliers) and Funnel Charts (systematic bias).
* **Lesson 7.4: Specialized Plots.** Heatmaps (correlation matrices) and Volcano Plots (significance vs. fold-change).
* **Lesson 7.5: Venn Plots.** Visualizing set intersections and overlaps.

### Chapter 8: Dimensionality Reduction

* **Lesson 8.1: Principal Component Analysis (PCA).** The intuition of "rotating" data to maximize variance.
* **Lesson 8.2: Eigenvalues & Eigenvectors.** The mathematical engines behind PCA.
* **Lesson 8.3: Scree Plots.** Determining the optimal number of components to keep.

---

