# Hospital Patient Analytics | Databricks

**Independent data analytics portfolio project** | Databricks · PySpark · SQL · Delta Lake · AI/BI Dashboards

## Project overview

This project explores hospital service activity, reported financial performance, admission patterns, and length of stay using a training dataset. The objective is to turn source records into a validated analytical table and present operational and financial comparisons in Databricks dashboards.

## Data and workflow

* **Source:** 8,392 records across 19 original fields (training dataset).
* **Preparation:** Schema review, null and duplicate checks, date and financial-value validation, column-name normalization, text cleanup, and ZIP code standardization.
* **Feature engineering:** Length of stay, admission month, and reported profit-margin percentage.
* **Output:** An 8,392-row, 22-column Delta analytical table (`patient.default.patient\\\\\\\_analytics`).
* **Presentation:** Two Databricks AI/BI dashboards, including an interactive dashboard with shared hospital, priority, region, and admission-date filters.

## Headline metrics (unfiltered)

|Metric|Result|
|-|-:|
|Total reported revenue|$18.63M|
|Total reported profit|$1.52M|
|Distinct patient IDs|5,491|
|Average length of stay|2.04 days|

## Selected observations

* North Hospital accounted for approximately **$9.37M** in reported revenue, compared with **$7.79M** at South Hospital and **$1.48M** at Downtown Hospital.
* Surgical services contributed approximately **$5.45M** in reported revenue, followed by Medical services at **$4.82M**.
* The Low admission-priority category had an average length of stay of **4.24 days**; this is descriptive, not a clinical conclusion.
* Revenue and length of stay had negligible linear correlation (Pearson r approximately **0.0114**).

## Dashboard previews

!\[Executive and hospital performance overview](images/dashboard-overview.png)
!\[Financial performance by hospital and service](images/financial-performance.png)
!\[Admission and length-of-stay analysis](images/admission-length-of-stay.png)
!\[Interactive dashboard with shared filters](images/interactive-filters.png)

More screenshots are in [`images/`](images/). See [Project Overview (PDF)](Project_Overview.pdf) for objectives, methods, observations, and limitations.

## Technical implementation

The repository separates the analytical SQL queries from the PySpark notebook code:

* [**`pyspark/`**](pyspark/)**:** Original Databricks notebook cells covering ingestion, profiling, null/duplicate and financial checks, cleaning, `df\\\\\\\_clean` rebuild, feature engineering, and writing the Delta table.
* [**`sql/`**](sql/)**:** Databricks SQL queries for dashboard datasets, KPIs, and analytical comparisons, including monthly revenue and profit trends.

### PySpark notebook sequence

The complete notebook export was divided into **20 ordered PySpark cells**. Key stages include:

1. Read `patient.default.patient\\\\\\\_info\\\\\\\_raw` and inspect its schema and records.
2. Check nulls, duplicate records, invalid values, and categorical distributions.
3. Standardize column names, ZIP codes, and text values.
4. Examine financial data and test possible revenue/cost/profit relationships.
5. Rebuild `df\\\\\\\_clean` from the raw table (a retained step from the original notebook).
6. Engineer `length\\\\\\\_of\\\\\\\_stay`, `admission\\\\\\\_month`, and `profit\\\\\\\_margin\\\\\\\_pct`.
7. Inspect the results and save `patient.default.patient\\\\\\\_analytics` as a Delta table.

**Execution notes:** Run PySpark cells in numerical order in the same Databricks session; individual files are notebook fragments, not standalone scripts. Run SQL queries after the Delta table exists. If your catalog or schema differs, update the table references. The additional SQL files were extracted from the earlier project guide; the complete notebook export itself contains one SQL cell for monthly revenue and profit trends. These extracted files have not been independently rerun in a fresh Databricks workspace.

## Interpretation and limitations

* Reported profit does not consistently reconcile to simple revenue/cost/discount formulas; financial results are source-reported rather than independently validated.
* Patient IDs may recur across service records, so record count and distinct patient count differ.
* Length of stay is calculated as discharge date minus admission date for each record.
* This is an independent portfolio analysis of a training dataset, not a hospital audit or medical study.
* Raw patient data is not included in this repository.

