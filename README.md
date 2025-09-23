# TfL Northern Line Delay Analysis

This project explores **London Underground performance** using the TfL *Lost Customer Hours* dataset.  
The aim is to analyse **delay** on the tube and compare it with other key lines (Central, Jubilee, Victoria).

---

## 🎯 Objectives

- Understand how **Lost Customer Hours (LCH)** evolve over time.
- Compare **annual totals** across multiple lines.
- Identify which **periods and years** drive the largest spikes in delays.
- Showcase **data cleaning, analysis, and visualisation** skills using Python (pandas, matplotlib, seaborn).

---

## 📊 Dataset

- **Source:** [TfL London Underground Performance Data — London Datastore](https://data.london.gov.uk/dataset/lu-performance-data)  
- **Measure:** *Lost Customer Hours (LCH)* — the total time lost by passengers due to delays, weighted by passenger volumes.  
- **Granularity:** 13 four-week *Periods* per Financial Year (FY).  
- **Coverage:** Northern Line (focus), Central, Jubilee, and Victoria Lines (comparisons).  
- **Licence:** Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

---

## 🛠️ Methods

1. **Data Cleaning**
   - Removed formatting artefacts (commas in numbers, blanks → NaN).
   - Converted all values to numeric.
   - Built a `fy_period` label (e.g., `2019-20 / P03`) for readability.

2. **Data Transformation**
   - Period-level dataset cleaned and saved as `/processed_data/period_clean.csv`.
   - Annual totals aggregated and saved as `/processed_data/annual_totals.csv`.

3. **Analysis & Visualisation**
   - Multi-line trends across periods.
   - Rolling average trends (3-period smoothing).
   - Annual grouped bar charts.
   - Annual stacked bar charts (composition by line).
   - Heatmap experiment (evaluated but not selected for final portfolio).

---

## 📈 Key Visuals

### 1. Period Trends (Raw Data)
![](outputs/figures/linechart_raw.png)

### 2. Rolling Average Trends
![](outputs/figures/linechart_rolling.png)

### 3. Annual Totals (Grouped Bars)
![](outputs/figures/barchart_grouped.png)

### 4. Annual Composition (Stacked Bars)
![](outputs/figures/barchart_stacked.png)

---

## 🔍 Insights

- The **Central Line consistently shows the highest Lost Customer Hours** across years.
- The **Jubilee and Northern Lines show spikes in FY 2019–20**, contributing a growing share to delays.
- Rolling averages reveal **sustained upward trends** prior to 2019–20, smoothing out period-to-period volatility.

---

## 🚀 Next Steps

- **Interactive Dashboard:** A Streamlit app allowing users to:
  - Select lines and year ranges.
  - Explore smoothed vs raw period trends.
  - Compare annual totals dynamically.
- **Extend analysis:** Add more lines and explore cross-modal comparisons (e.g., Overground, Buses).

---

## ⚖️ Licensing

- **Data:** © Transport for London, licensed under [OGL v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
- **Code & Analysis:** MIT Licence.

---

## 👤 Author

Built by *[Sarthak Nanda]* as part of a personal data analysis portfolio project.
