# Hypothesis Testing Summary

## Project
Sales Data Storytelling & Statistical Validation

## Objective
The objective of this hypothesis test is to determine whether there is a statistically significant difference in average order sales between male and female customers.

---

## Business Question
Does customer gender have a significant impact on average order sales?

---

## Hypotheses

### Null Hypothesis (H₀)
There is no statistically significant difference in average order sales between male and female customers.

### Alternative Hypothesis (H₁)
There is a statistically significant difference in average order sales between male and female customers.

---

## Statistical Test Used
An independent samples Welch's t-test was used because:

- The analysis compares two independent customer groups: Male and Female.
- Total Sales is a numerical variable.
- Welch's t-test does not require equal variance between the two groups.

---

## Significance Level

**α = 0.05**

If the p-value is less than 0.05, the null hypothesis will be rejected.

---

## Results

| Metric | Result |
|---|---:|
| Male Orders | 511 |
| Female Orders | 489 |
| Male Average Sales | ₹141,807.34 |
| Female Average Sales | ₹136,883.21 |
| Mean Difference | ₹4,924.13 |
| T-Statistic | 0.6826 |
| P-Value | 0.4950 |
| Significance Level | 0.05 |
| Decision | Fail to Reject H₀ |

---

## Confidence Interval

The 95% confidence interval for the difference in average sales is approximately:

**-₹9,231.58 to ₹19,079.85**

The confidence interval includes zero, which supports the conclusion that the observed difference between male and female customers is not statistically significant.

---

## Statistical Conclusion

Since the p-value of **0.4950** is greater than the significance level of **0.05**, the null hypothesis is not rejected.

Therefore, there is not enough statistical evidence to conclude that average order sales differ significantly between male and female customers.

---

## Business Interpretation

Although male customers have slightly higher average order sales than female customers, the difference is not statistically significant.

This means gender alone should not be considered a strong factor for developing sales or customer targeting strategies.

---

## Business Recommendation

Instead of focusing primarily on gender-based targeting, the business should prioritize stronger customer and sales drivers such as:

- Customer value segments
- Product preferences
- Product categories
- Geographic performance
- Customer purchasing behavior

These factors can provide more meaningful opportunities for revenue growth and customer engagement.