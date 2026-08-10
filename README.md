# 📊 SynapseSCM — Procurement Cost Intelligence

<p align="center">

### Enterprise Supply Intelligence Platform

**Procurement Cost Intelligence | Power BI | Data Analytics**

<br>
<img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
<img src="https://img.shields.io/badge/Power%20Query-ETL-742774?style=for-the-badge" />
<img src="https://img.shields.io/badge/DAX-KPI%20Analysis-0078D4?style=for-the-badge" />
<img src="https://img.shields.io/badge/Excel-Data%20Preparation-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" />

</p>


## 📌 Project Summary

**SynapseSCM – Procurement Cost Intelligence** is a data analytics project developed to analyze procurement expenditure and identify the main factors contributing to purchasing costs.

The project brings together supplier, product, purchase order, inventory, shipment, and external market information into a structured Power BI reporting solution.

The main objective is to help procurement teams answer questions such as:

- Where is procurement money being spent?
- Which suppliers contribute the highest expenditure?
- Which products and categories have higher procurement costs?
- How does procurement spending change over time?
- What external market indicators provide additional cost context?

--

# 🎯 Business Problem

Procurement data is often spread across different files and contains information about suppliers, products, purchase orders, inventory, shipments, and costs.

When this information is reviewed separately, it becomes difficult to:

- identify major spending areas,
- compare supplier costs,
- monitor product-level costs,
- track procurement trends,
- understand cost variations,
- and quickly identify areas requiring attention.

### Proposed Approach

Build a centralized Power BI dashboard that transforms the available procurement data into clear and interactive business information.

--

# 🏢 Primary Business Domain

## Procurement Cost Intelligence

The project focuses on understanding procurement expenditure and cost patterns.

Other areas such as supplier, product, inventory, logistics, and market information are used to support the main procurement cost analysis.

---

# 🔎 Business Questions

The dashboard was designed around six major business questions.

### 1. Supplier Spending

Which suppliers contribute the highest procurement expenditure?

### 2. Product Spending

Which products and procurement categories account for the largest share of spending?

### 3. Procurement Trend

How does procurement spending change across different periods?

### 4. Supplier Cost Relationship

How do supplier ratings and supplier characteristics relate to procurement spending?

### 5. Product Cost

Which products have higher unit costs and purchasing quantities?

### 6. Market Context

How do external indicators such as PPI, copper, crude oil, exchange rates, and interest rates provide additional context for procurement cost changes?

--

# 🔄 End-to-End Project Workflow

```text
┌─────────────────────┐
│   DATA COLLECTION   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ DATA UNDERSTANDING  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   DATA QUALITY      │
│     ASSESSMENT      │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    DATA CLEANING    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│         EDA         │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   DATA MODELING     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│    DAX MEASURES     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   POWER BI REPORT   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ BUSINESS INSIGHTS   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│  RECOMMENDATIONS    │
└─────────────────────┘
``

---

## 📂 1. Data Sources

The project uses 11 datasets covering internal procurement information and external supporting market information.

### 🏢 Internal Procurement Data

| Dataset | Purpose |
| --- | --- |
| **Suppliers.xlsx** | Supplier master information including supplier details, rating, status, country, and payment terms. |
| **Products.xlsx** | Product master information including product details and categories. |
| **Inventory.xlsx** | Inventory and stock information used to understand product availability and stock levels. |
| **Warehouses.xlsx** | Warehouse master information and warehouse-related details. |
| **Purchase_Orders.xlsx** | Procurement transaction information used to analyze purchase orders, quantities, unit costs, and procurement expenditure. |
| **Shipments.xlsx** | Shipment and logistics information used to review delivery and transportation-related information. |

### 🌍 External Supporting Data

| Dataset | Purpose |
| --- | --- |
| **ExchangeRates.xlsx** | Currency exchange rate information used to provide currency-related cost context. |
| **Copper.xlsx** | Copper market price information used as supporting market information for procurement cost analysis. |
| **CrudeOil.xlsx** | Crude oil market price information used to provide additional cost context. |
| **InterestRates.xlsx** | Interest rate information used as supporting economic information. |
| **ProducerPriceIndex.xlsx** | Producer Price Index information used to review producer-level price movements. |

> **Note:** External datasets are used as supporting market information. The primary focus of this project remains **Procurement Cost Intelligence**.

---

## 🔍 2. Data Understanding & Data Quality Assessment

Before developing the Power BI report, the datasets were reviewed to understand their structure, fields, formats, and data quality.

### Checks performed

* Row and column counts
* Missing and blank values
* Duplicate records
* Date formats
* Data types
* Negative values
* Invalid numerical values
* Currency formatting
* Unit formatting
* Inconsistent text values
* Unusual or extreme values
* Business-rule validation

### 📋 Data Quality Assessment

| Data Issue | Column / Area | Treatment |
| --- | --- | --- |
| **Missing values** | `SupplierRating` | Missing values were replaced according to the defined business rule. |
| **Missing values** | `FacilityManager` | Blank values were replaced with `Unknown`. |
| **Duplicate records** | Supplier and purchase order records | Duplicate occurrences were removed while retaining the valid record. |
| **Invalid date format** | Order, shipment, and delivery dates | Date values were standardized. |
| **Missing required values** | Business-related fields | Values were reviewed and replaced where sufficient information was available. |
| **Negative cost values** | Cost-related fields | Values were checked and corrected where identified as invalid. |
| **Currency symbols** | Financial fields | Symbols such as `$` and `₹` were removed before numeric conversion. |
| **Unit strings** | Quantity and numerical fields | Unnecessary unit text was removed before numeric conversion. |
| **Inconsistent text** | Status, currency, payment terms, carrier, and transport fields | Text values were standardized. |
| **Quantity values** | Inventory-related fields | Values were validated using applicable business rules. |

The data-quality assessment helped identify the main issues in the source datasets before they were used for analysis.

---

## 🧹 3. Data Cleaning

The identified data-quality issues were addressed before the data was used for analysis and reporting.

### Main cleaning activities

* Removed duplicate records
* Handled missing values
* Standardized date formats
* Corrected data types
* Cleaned numerical fields
* Checked and corrected invalid negative values
* Removed currency symbols
* Removed unnecessary units
* Standardized text values
* Applied business validation rules
* Checked quantity-related values
* Verified the cleaned datasets
* Prepared the data for Power BI

The cleaned data was then used for exploratory analysis and data modeling.

---

## 📊 4. Exploratory Data Analysis

Exploratory analysis was performed to understand the main procurement patterns before developing the final dashboard.

### Areas analyzed

* Procurement spend distribution
* Supplier spending
* Supplier rating distribution
* Product spending
* Category-wise spending
* Procurement quantity
* Unit cost
* Freight cost
* Monthly procurement spending
* Supplier country analysis
* Inventory-related information
* External market indicators

The results from EDA were used to determine the KPIs, charts, filters, and analysis included in the Power BI report.

---

## 🔗 5. Data Modeling

The cleaned datasets were organized into a structured Power BI data model.

### Modeling activities

* Created fact and dimension tables
* Defined relationships between tables
* Created a date dimension
* Connected procurement transactions with supplier and product information
* Established relationships required for analysis
* Prepared the model for DAX calculations
* Validated relationships using report results

### 📸 Data Model

*(Insert Data Model Diagram / Screenshot Here)*

---

## 🧮 6. DAX Measures & KPI Development

DAX was used to create the main procurement metrics and analytical calculations.

### Main KPI Areas

* Total Procurement Spend
* Total Purchase Orders
* Total Suppliers
* Active Suppliers
* Supplier Spend Contribution %
* Procurement Quantity
* Average Unit Cost
* Average Freight Cost
* Procurement Spend Trend
* Target-based KPIs

### Example DAX Measures

#### Total Procurement Spend

```dax
Total Procurement Spend = 
SUM(Fact_Purchase_Orders[TotalPOValue])

```

#### Total Suppliers

```dax
Total Suppliers = 
DISTINCTCOUNT(Dim_Suppliers[SupplierID])

```

#### Active Suppliers

```dax
Active Suppliers = 
CALCULATE(
    [Total Suppliers],
    Dim_Suppliers[Status] = "Active"
)

```

#### Supplier Spend Contribution %

```dax
Supplier Spend Contribution % = 
DIVIDE(
    [Total Procurement Spend],
    CALCULATE(
        [Total Procurement Spend],
        ALL(Dim_Suppliers[SupplierName])
    ),
    0
)

```

#### Average Unit Cost

```dax
Average Unit Cost = 
AVERAGE(Fact_Purchase_Orders[UnitCost])

```

---

## 📌 7. Main KPIs

| KPI | Purpose |
| --- | --- |
| **Total Procurement Spend** | Measures total procurement expenditure. |
| **Total Purchase Orders** | Shows the number of procurement transactions. |
| **Total Suppliers** | Shows the total supplier base. |
| **Active Suppliers** | Shows the number of currently active suppliers. |
| **Supplier Spend Contribution %** | Shows each supplier's contribution to total procurement spend. |
| **Total Procurement Quantity** | Shows the total quantity purchased. |
| **Average Unit Cost** | Shows the average purchasing cost per unit. |
| **Average Freight Cost** | Helps monitor transportation-related costs. |
| **Procurement Spend Trend** | Shows how procurement spending changes over time. |

---

## 📊 8. Power BI Dashboard

The final Power BI report contains five analytical pages.

### 🟦 Page 1 — Procurement Overview

The Procurement Overview page provides a high-level view of the overall procurement position.

* **Main components:**
* Total Procurement Spend
* Total Purchase Orders
* Total Suppliers
* Active Suppliers
* Procurement Spend Trend
* Supplier Contribution
* Product Contribution
* Procurement Category Analysis
* Date and business filters


* **Purpose:** To provide management with a quick understanding of procurement expenditure and major spending areas.
* **📸 Screenshot:** *(Insert Page 1 Screenshot Here)*

---

### 🟩 Page 2 — Procurement Spend Analysis

This page focuses specifically on procurement spending and cost patterns.

* **Main components:**
* Total Procurement Spend
* Procurement Quantity
* Average Unit Cost
* Freight Cost
* Category-wise Procurement Spend
* Payment Terms Analysis
* Spending Trends
* Cost Comparison
* Detailed procurement information


* **Purpose:** To understand where procurement expenditure is concentrated and identify major cost areas.
* **📸 Screenshot:** *(Insert Page 2 Screenshot Here)*

---

### 🟨 Page 3 — Supplier Cost Analysis

This page focuses on supplier-related procurement expenditure and supplier characteristics.

* **Main components:**
* Total Suppliers
* Active Suppliers
* High Rated Suppliers
* Supplier Procurement Spend
* Supplier Rating Distribution
* Supplier Spend Comparison
* Supplier Rating vs Procurement Cost
* Supplier Country Analysis
* Supplier Details


* **Filters:** Supplier Name, Country, Supplier Rating Group, Status, Payment Terms, Date
* **Purpose:** To identify major suppliers, compare supplier expenditure, and understand supplier-related cost patterns.
* **📸 Screenshot:** *(Insert Page 3 Screenshot Here)*

---

### 🟧 Page 4 — Product Cost Analysis

This page focuses on product-level procurement expenditure and cost patterns.

* **Main components:**
* Total Procurement Spend
* Total Procurement Quantity
* Average Unit Cost
* Product-wise Procurement Spend
* Category-wise Procurement Spend
* Quantity vs Unit Cost
* Product Cost Distribution
* Product Details


* **Filters:** Product Name, Product Category, Currency, Date, Supplier
* **Purpose:** To identify high-cost products and categories and understand purchasing quantity and unit-cost variations.
* **📸 Screenshot:** *(Insert Page 4 Screenshot Here)*

---

### 🟥 Page 5 — Market Intelligence

This page provides external market information connected to the procurement cost environment.

* **Main components:**
* Average PPI
* Average Copper Price
* Average Crude Oil Price
* Average Exchange Rate
* Interest Rate
* PPI Trend
* Copper Price Trend
* Crude Oil Price Trend
* Exchange Rate Trend
* Interest Rate Trend


* **Filters:** Date, Currency, Market Indicator, Year, Month
* **Purpose:** To provide supporting market information that can be considered when reviewing procurement cost movements.

> **Important:** Market Intelligence is a supporting section of the Procurement Cost Intelligence project, not a separate primary business domain.

* **📸 Screenshot:** *(Insert Page 5 Screenshot Here)*

---

### 🎨 Dashboard Design

The dashboard was designed to make procurement information easy to review.

* **Design elements:**
* KPI cards
* Bar charts
* Column charts
* Line charts
* Donut charts
* Treemaps
* Tables
* Trend analysis
* Interactive slicers
* Supplier comparisons
* Product comparisons
* Consistent currency formatting
* Consistent number formatting



The report uses filters to allow users to analyze procurement information based on supplier, country, rating, status, product, category, currency, payment terms, and date.

---

## 💡 9. Key Findings

The analysis provides visibility into several important procurement patterns:

* **Supplier Spending:** The dashboard identifies suppliers contributing the highest share of procurement expenditure.
* **Product Spending:** High-spending products and categories can be identified for further review.
* **Supplier Rating:** Supplier ratings can be compared with procurement spending to understand spending patterns across different supplier groups.
* **Cost Variation:** Unit cost and freight cost variations can be reviewed to identify transactions requiring attention.
* **Procurement Trends:** Spending trends show how procurement expenditure changes over time.
* **Market Context:** External indicators provide additional information that can be considered when reviewing procurement cost movements.

---

## 📈 10. Business Impact

The project provides practical value in several areas:

* 💰 **Cost Visibility:** Provides a clear view of total procurement expenditure and major spending areas.
* 🏢 **Supplier Review:** Helps procurement teams compare suppliers based on spending, rating, status, country, and payment terms.
* 📦 **Product Cost Monitoring:** Helps identify products and categories with higher procurement expenditure.
* 🚚 **Freight Cost Monitoring:** Provides visibility into transportation-related procurement costs.
* 📊 **Purchasing Planning:** Combines spending, quantity, supplier, and product information to support purchasing decisions.
* ⚡ **Faster Reporting:** Reduces the need to manually review multiple datasets separately.

---

## 🎯 11. Business Recommendations

Based on the analysis, the following actions can be considered:

1. **Review High-Spending Suppliers:** Regularly review suppliers contributing a large share of procurement expenditure and compare pricing and payment terms.
2. **Review High-Cost Products:** Identify products with higher unit costs and compare purchasing costs across suppliers and categories.
3. **Monitor Supplier Performance:** Consider supplier rating along with procurement spending when reviewing supplier relationships.
4. **Control Freight Costs:** Review transactions with higher freight costs and evaluate possible opportunities to reduce transportation expenditure.
5. **Improve Purchasing Planning:** Use procurement trends, quantities, and inventory information to support purchasing decisions.
6. **Monitor Market Indicators:** Track relevant market indicators when reviewing procurement cost changes, especially where raw-material prices or currency movements may influence purchasing costs.

---

## ⚠️ 12. Challenges Faced

During project development, several challenges were addressed:

* Working with multiple datasets
* Different dataset structures
* Missing values
* Duplicate records
* Inconsistent date formats
* Invalid numerical values
* Negative values
* Currency symbols and units
* Inconsistent text categories
* Establishing relationships between datasets
* Creating accurate DAX measures
* Validating KPI results
* Designing multiple dashboard pages
* Maintaining consistent filters and calculations

---

## ⚠️ 13. Limitations

The current project has some limitations:

* The analysis depends on the quality and completeness of the available source data.
* The analysis is limited to the available historical period.
* External market indicators provide supporting context but do not independently establish the cause of every procurement cost change.
* The current solution is primarily focused on descriptive and comparative analysis.
* Advanced predictive forecasting has not been included in the current version.
* The project currently focuses on Procurement Cost Intelligence rather than the complete supply-chain function.

---

## 🚀 14. Future Scope

The current project focuses on one primary business domain: **Procurement Cost Intelligence**.
The solution can be expanded in future versions with additional modules.

| Future Area | Possible Development |
| --- | --- |
| **Supplier Intelligence** | Supplier risk scoring and deeper supplier performance analysis. |
| **Product Intelligence** | Product demand, cost variation, and purchasing pattern analysis. |
| **Inventory Intelligence** | Stock monitoring, reorder analysis, and inventory planning. |
| **Logistics Intelligence** | Shipment performance, freight analysis, and transportation monitoring. |
| **Advanced Market Intelligence** | More detailed analysis of external economic and commodity indicators. |

These areas represent future extensions of the current procurement analytics solution.

---

## 🛠️ Technology Stack

| Technology | Usage |
| --- | --- |
| **Microsoft Excel** | Initial data review and quality assessment |
| **Power Query** | Data cleaning and transformation |
| **Power BI** | Dashboard development and reporting |
| **DAX** | KPI and analytical calculations |
| **Data Modeling** | Connecting datasets and creating relationships |
| **GitHub** | Project version control and documentation |

---

## 📁 Repository Structure

```text
SynapseSCM-Procurement-Cost-Intelligence/
│
├── 📊 powerbi/
│   └── Procurement_Cost_Intelligence.pbix
│
├── 📂 data/
│   ├── internal/
│   ├── external/
│   └── README.md
│
├── 📷 screenshots/
│   ├── procurement-overview.png
│   ├── procurement-spend-analysis.png
│   ├── supplier-cost-analysis.png
│   ├── product-cost-analysis.png
│   ├── market-intelligence.png
│   └── data-model.png
│
├── 📄 documentation/
│   └── Project_Report.pdf
│
├── 🧮 dax/
│   └── DAX_Measures.txt
│
└── README.md

```

---

## 📸 Dashboard Screenshots

* Procurement Overview
* Procurement Spend Analysis
* Supplier Cost Analysis
* Product Cost Analysis
* Market Intelligence
* Data Model

---

## 📄 Project Documentation

The complete project documentation contains:

* Introduction
* Problem Statement
* Business Objectives
* Dataset Information
* Data Understanding
* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Data Modeling
* DAX Measures
* Dashboard Development
* Key Findings
* Business Insights
* Business Impact
* Recommendations
* Challenges
* Limitations
* Future Scope
* Conclusion
* References
* Appendix

```

```
