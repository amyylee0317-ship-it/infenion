# Demand Planning Simulation (VRFC-based)

## Project Overview
This project is a simplified demand planning simulation inspired by the VRFC (Volume Ramp-up & Forecast) concept in the semiconductor industry.

The main idea of this project is to use public financial report data to build a simple forecasting logic and see how historical trends can be turned into demand planning assumptions.  
Instead of making a highly accurate prediction model, this project focuses more on the thinking process behind forecasting, including how assumptions are made, how formulas are derived, and why forecast bias may happen.

---

## Motivation
I made this project because I am interested in supply chain and data analysis roles, especially in the semiconductor industry.

Through this project, I wanted to:
- learn more about how demand planning works
- practice using Python and Excel for analysis
- try turning public business information into a forecasting model
- build a side project that is more related to real business situations

---

## Tools
- Python (Pandas, NumPy)
- Excel
- Power BI

---

## Data Source
This project mainly uses Infineon’s financial reports from 2021 to 2024 as the historical data source.

Besides that, I also referred to information from the 2025 financial report when thinking about external factors that may affect the company, such as market conditions, industry trends, and business environment changes.

Because the available structured data is very limited, I used the 2025 report mainly to help me make more reasonable assumptions, not to directly “train” the model.

---

## Method
My overall process was:

1. Read Infineon’s financial reports from 2021 to 2024
2. Observe the changes and overall trend in the data
3. Build a simplified forecasting logic based on those trends
4. Refer to the 2025 report to think about possible external influences
5. Compare forecast results with actual outcomes and look at the differences

So this project is better understood as a **simulation with informed assumptions**, instead of a fully data-driven forecasting model.

---

## Model Logic
The logic of this project is quite simple.

I started from the historical data and tried to identify whether the business was showing growth, decline, or other noticeable changes over time. Based on that, I built a simplified forecasting formula to project future demand.

This means the model is not based on a complicated machine learning method or advanced statistical model.  
Instead, it is based on:
- historical trend observation
- simple growth/decline logic
- business interpretation from the reports
- manual assumption adjustment

I chose this approach because the amount of available data is small, and I wanted the model to be easier to explain and understand.

---

## How the Formula Was Derived
The formula in this project does not come from one standard textbook model.  
It was derived step by step from my own observations of the historical data.

My basic idea was:

- use 2021–2024 data as the base
- look at year-to-year changes
- use those changes to estimate the overall direction of future demand
- adjust the forecast based on business context mentioned in the reports

So the formula is more like a **heuristic formula** built from trend observation and business reasoning.

This also means the formula is not meant to be “perfect.”  
Its purpose is to show how I translate limited public information into a forecasting process.

---

## Why Forecast Bias Happens
There are several reasons why the forecast may be different from the actual result.

### 1. Limited data
The project mainly uses only a few years of annual report data, so it cannot fully capture long-term cycles, short-term changes, or more detailed patterns.

### 2. External uncertainty
The semiconductor industry is affected by many outside factors, such as market demand, industry cycles, macroeconomic conditions, and customer changes. These are hard to fully include in a simple model.

### 3. Qualitative judgment
Part of my assumptions about external influence came from reading the 2025 financial report. This helps make the forecast more reasonable, but it can also introduce bias because some interpretation is done manually.

### 4. Simplified model structure
The model does not include deeper business variables such as product mix, customer segmentation, inventory strategy, production capacity, or regional demand differences.

### 5. Difference between simulation and reality
In real business situations, many factors interact at the same time. In this project, I simplified those interactions so the model would stay understandable.

---

## What This Project Can Show
Although this project is not a complete decision-making model, it can still show some useful ideas.

For example:
- if the forecast trend goes up, it may suggest a possible need to increase production or review supply planning
- if the forecast trend goes down, it may suggest possible inventory adjustment
- if the forecast is very different from the actual result, it suggests the assumptions should be reviewed again

So I think this project is more suitable as a **starting point for demand planning analysis**, rather than a final decision-support tool.

---

## Visualization
I used Power BI to create charts for:
- demand trend
- forecast vs actual comparison
- possible forecast deviation

These charts help make the results easier to understand.

---

## Project Structure
```text
project/
│
├── data/
│   └── demand_data.xlsx
│
├── src/
│   └── simulation.py
│
├── output/
│   └── forecast_result.csv
│
├── images/
│   └── dashboard.jpg
│
└── README.md