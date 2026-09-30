---
layout: default
---

## Table of Contents
* TOC
{:toc}

---

## 1. The Project

### What is this project about?
A big retail company sells furniture, office supplies, and technology across the United States. The company wants to know: **where do we make money, where do we lose money, and what should we do about it?**

In this project I took the raw sales data, cleaned it, explored it, and turned it into insights and an interactive dashboard.

### The data
The data comes from one Excel file with three sheets:

| Sheet | What it contains | Size |
|-------|------------------|------|
| **Orders** | Every product sold: dates, customer, location, product, sales, discount, profit | 9,994 rows, 21 columns |
| **People** | The manager of each region | 4 rows |
| **Returns** | Orders that customers sent back | 800 rows |

**Time period:** 3 Jan 2016 to 30 Dec 2019 (4 years).

### Questions I wanted to answer
1. Which category brings the most sales and profit?
2. Which sub-categories sell best, and which lose money?
3. Which region and which states perform best?
4. What affects profit the most?
5. Which category has the most returns?
6. Which shipping mode is fastest, and which is most used?
7. How do sales change over time?

### Business numbers at a glance

| Total Sales | Total Profit | Profit Margin | Orders | Customers | Products |
|:-----------:|:------------:|:-------------:|:------:|:---------:|:--------:|
| **$2.30M** | **$286K** | **12.5%** | **5,009** | **793** | **1,862** |

Other numbers: average discount is **15.6%**, and **296 orders (5.9%)** were returned.

---

## 2. The Workflow

I followed six steps. Click each one to see what I did.

<details markdown="1">
<summary><b>Step 1: Data Profiling (getting to know the data)</b></summary>

Before changing anything, I looked at the data to understand it.

- **Loaded** the three sheets with Python (pandas).
- **Checked the shape, data types, and unique values** of every column.
- **Checked the dates.** Orders run from January 2016 to December 2019.
- **Checked missing values.** Only one column had them: `Postal Code`, with 11 missing rows (0.11%).
- **Checked the correlations** between Sales, Quantity, Discount, and Profit.
- **Looked at the People and Returns sheets.** People has one manager per region. Returns has 800 rows but only 296 different orders, so it has repeated rows.

**What I learned:** the data is in good shape. It needs only small fixes.
</details>

<details markdown="1">
<summary><b>Step 2: Data Cleaning (fixing problems)</b></summary>
</details>

<details markdown="1">
<summary><b>Step 3: Data Manipulation (joining the sheets)</b></summary>
</details>

<details markdown="1">
<summary><b>Step 4: Feature Engineering (creating useful new columns)</b></summary>

</details>

<details markdown="1">
<summary><b>Step 5: Exploratory Data Analysis (asking questions)</b></summary>
</details>

<details markdown="1">
<summary><b>Step 6: Visualization and Dashboard</b></summary>

- Made charts with Matplotlib and Seaborn: pie charts, bar charts, a trend line, and a heatmap.
- Built an **interactive dashboard** with Streamlit and Plotly, so anyone can filter by Region, Category, and Segment. You can use it in [section 4](#4-interactive-dashboard).
</details>

---

## 3. Key Insights

### Insight 1: Technology and Office Supplies earn the money. Furniture does not.

| Category | Sales | Profit | Profit Margin |
|----------|------:|-------:|--------------:|
| Technology | $836,154 | $145,455 | **17.4%** |
| Office Supplies | $719,047 | $122,491 | **17.0%** |
| Furniture | $741,999 | $18,451 | **2.5%** |

Furniture sells almost as much as the others, but keeps very little profit because its costs are very high.

### Insight 2: Tables lose money, and so do some machines

- **Tables** lose more than **$15,000** in total, even though they are a top-5 seller.
- **Phones and Chairs** bring the most sales (over $300,000 each).
- The biggest loss-making product is the **Cubify CubeX 3D Printer (Double Head)**, at **−$8,880**. Lexmark MX611dhe printer (−$4,590) and a Cubify triple-head printer (−$3,840) also lose money.
- The best product is the **Canon imageCLASS 2200 Copier**: **$61,600** in sales and **$25,200** in profit.

### Insight 3: The West is the best region. The Central region is the weakest.

| Region | Sales | Profit | Margin |
|--------|------:|-------:|-------:|
| West | $725,458 | $108,418 | 14.9% |
| East | $678,781 | $91,523 | 13.5% |
| Central | $501,240 | $39,706 | 7.9% |
| South | $391,722 | $46,749 | 11.9% |

Central has more sales than South, but earns less profit. **Furniture in the Central region loses money** (−$2,871).

### Insight 4: A few places drive most of the sales

- **Top states:** California ($458K), New York ($311K), Texas ($170K), Washington ($139K), Pennsylvania ($117K).
- **Top cities:** New York City ($256K), Los Angeles ($176K), Seattle ($120K).

### Insight 5: Discounts hurt profit

- Discount and Profit have a **negative correlation (−0.22)**. Higher discounts usually mean lower profit.
- Discount and Sales have almost **no relationship (−0.03)**. Big discounts do not clearly bring more sales.
- The average discount is 15.6%, but some orders have up to 80% off.

### Insight 6: Sales are growing, with a strong end-of-year season

- Yearly sales: 2016 = $484K, 2017 = $471K, 2018 = $609K, **2019 = $733K**.
- 2019 is **56% higher than 2017**.
- **September, November, and December** are the busiest months. Together they bring about **43% of all sales**.
- January and February are the slowest months.

### Insight 7: Shipping and returns

- **Same Day** is the fastest (0.04 days on average). Then First Class (2.2 days), Second Class (3.2 days), and Standard Class (5.0 days).
- **Standard Class** is used the most: about **60%** of order lines.
- **296 orders (5.9%)** were returned. **Office Supplies** has the most returned orders (234), followed by Furniture (136) and Technology (123). An order can contain more than one category, so these numbers add up to more than 296.

---

## 4. Interactive Dashboard

Use the filters on the left side of the dashboard (Region, Category, Segment) to explore the numbers yourself. If the app is sleeping, wait a few seconds for it to wake up.

<iframe src="https://superstore2019-dashboard.streamlit.app/?embed=true" title="Superstore Dashboard" loading="lazy" style="width:100%; height:850px; border:1px solid #e1e4e8; border-radius:8px;"></iframe>

<p style="text-align:center;"><a href="https://superstore2019-dashboard.streamlit.app/" target="_blank">Open the dashboard in a new tab ↗</a></p>

---

## 5. Recommendations

| # | Problem | What to do |
|---|---------|-----------|
| 1 | Furniture has only a 2.5% margin | Review supplier costs and raise prices. Start with Tables, which lose money. |
| 2 | Heavy discounts lower profit and do not raise sales | Set a **maximum discount** (for example 20%) and ask for approval above it. |
| 3 | Some products lose money (3D printers, some printers, conference tables) | Check their price and cost. Fix them, or stop selling them. |
| 4 | Central region has the lowest margin | Look at Central's discounts and furniture costs. Learn from the West. |
| 5 | Sales peak in September, November, and December | Stock up early. Plan campaigns before these months. |
| 6 | Sales are low in January and February | Run special offers to keep sales steady. |
| 7 | Office Supplies has the most returns | Find the reasons for returns (quality, wrong item, packaging) and fix the top ones. |
| 8 | Most sales come from a few states and cities | Protect these markets. Test small campaigns in weaker states. |

---

## 6. Tools Used

**Python** (pandas, NumPy, Matplotlib, Seaborn) for analysis, **Streamlit + Plotly** for the dashboard, **GitHub Pages** for this report.

---

*Project by Hagar Gamal*