# World Happiness Index Analysis
**Python | Excel | Tableau | scikit-learn**

Analysis of the UN World Happiness Report (2015–2019) across 782 observations 
and 155+ countries to identify the key drivers of national wellbeing.

---

## Business Questions
1. Which socioeconomic variables most significantly predict a country's happiness score?
2. Can countries be meaningfully segmented based on their happiness profiles?

---

## Tools
| Tool | Purpose |
|---|---|
| Python (pandas) | Data merging, cleaning, missing value treatment |
| Excel (ToolPak) | Multiple linear regression |
| scikit-learn | K-Means clustering + silhouette scoring |
| Tableau | EDA and interactive visualisations |

---

## Key Findings
- **Freedom** is the strongest happiness predictor (coefficient: 1.478) — ahead of GDP (1.142)
- Model explains **76.4% of variance** in happiness scores (R² = 0.764), all variables significant at p < 0.001
- Global happiness was **stable 2015–2019** (5.354–5.407), suggesting structural rather than policy-driven determinants
- **Nordic nations dominate**: Finland (7.769), Denmark (7.600), Norway (7.554) consistently top-ranked
- K-Means (K=3) identified **three country clusters**: Low, Medium and High Wellbeing

---

## Regression Equation
ŷ = 2.1767 + 1.1419(GDP) + 0.6435(Social Support) + 1.0075(Life Expectancy) + 1.4781(Freedom) + 0.5919(Generosity) + 0.8626(Corruption)


---

## Clusters
| Cluster | Label | Examples |
|---|---|---|
| 0 | Low Wellbeing | Afghanistan, Yemen, Syria |
| 1 | High Wellbeing | Finland, Denmark, Norway |
| 2 | Medium Wellbeing | China, Mexico, Brazil |

---

## Dashboard
🔗 [View on Tableau Public](https://public.tableau.com/views/DBBA_Assignement_AllSheets/Histogram?:language=en-US&:sid=&:redirect=auth&showOnboarding=true&:display_count=n&:origin=viz_share_link)
