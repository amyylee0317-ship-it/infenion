import pandas as pd
import matplotlib.pyplot as plt
import os


# =========================
# 1. 建立原始資料
# =========================
# 說明：
# 這裡先手動放入各部門的歷史營收與 2025 實際值
# FY2021 ~ FY2024 用來做預測
# Actual_2025 用來做最後驗證
# Signal_Assumption 是你自己的假設，不是財報直接給的
segment_data = [
    {
        "Segment": "Automotive",
        "FY2021": 4841,
        "FY2022": 6516,
        "FY2023": 8242,
        "FY2024": 7716,
        "Signal_Assumption": -0.12,
        "Signal_Rationale": "Inventory correction across the automotive value chain.",
        "Actual_2025": 7402,
    },
    {
        "Segment": "Green Industrial Power",
        "FY2021": 1542,
        "FY2022": 1790,
        "FY2023": 2205,
        "FY2024": 1934,
        "Signal_Assumption": -0.14,
        "Signal_Rationale": "Weak industrial demand and elevated inventory.",
        "Actual_2025": 1631,
    },
    {
        "Segment": "Power & Sensor Systems",
        "FY2021": 3268,
        "FY2022": 4070,
        "FY2023": 3798,
        "FY2024": 3795,
        "Signal_Assumption": 0.12,
        "Signal_Rationale": "Positive AI / server demand signal.",
        "Actual_2025": 4208,
    },
    {
        "Segment": "Connected Secure Systems",
        "FY2021": 1397,
        "FY2022": 1822,
        "FY2023": 2046,
        "FY2024": 1506,
        "Signal_Assumption": -0.05,
        "Signal_Rationale": "Recovery is slow although the market is bottoming out.",
        "Actual_2025": 1418,
    },
]


# =========================
# 2. 設定模型權重
# =========================
# 這些不是財報直接給的，是你的模型設計
W_CAGR = 0.25
W_YOY = 0.35
W_SIGNAL = 0.40


# =========================
# 3. 轉成 DataFrame
# =========================
df = pd.DataFrame(segment_data)


# =========================
# 4. 計算 CAGR
# =========================
# CAGR = 複合年成長率
# 公式：
# (FY2024 / FY2021)^(1/3) - 1
# 因為 2021 -> 2024 中間跨了 3 年
df["CAGR_2021_2024"] = (df["FY2024"] / df["FY2021"]) ** (1 / 3) - 1


# =========================
# 5. 計算 2024 年的 YoY
# =========================
# YoY = 年增率
# 公式：
# FY2024 / FY2023 - 1
df["YoY_2024"] = df["FY2024"] / df["FY2023"] - 1


# =========================
# 6. 計算 2025 預測成長率
# =========================
# 預測公式：
# Forecast growth = 25% * CAGR + 35% * YoY + 40% * signal
df["Forecast_Growth_2025"] = (
    W_CAGR * df["CAGR_2021_2024"]
    + W_YOY * df["YoY_2024"]
    + W_SIGNAL * df["Signal_Assumption"]
)


# =========================
# 7. 計算 2025 預測營收
# =========================
# Forecast_2025 = FY2024 * (1 + 預測成長率)
df["Forecast_2025"] = df["FY2024"] * (1 + df["Forecast_Growth_2025"])


# =========================
# 8. 計算預測誤差
# =========================
# Error = 預測值 - 實際值
df["Error"] = df["Forecast_2025"] - df["Actual_2025"]

# 絕對誤差
df["Abs_Error"] = df["Error"].abs()

# APE = 絕對百分比誤差
df["APE"] = df["Abs_Error"] / df["Actual_2025"]


# =========================
# 9. 顯示每個部門的結果
# =========================
summary_cols = [
    "Segment",
    "FY2021",
    "FY2022",
    "FY2023",
    "FY2024",
    "CAGR_2021_2024",
    "YoY_2024",
    "Signal_Assumption",
    "Forecast_Growth_2025",
    "Forecast_2025",
    "Actual_2025",
    "Error",
    "APE",
]

print("\n===== SEGMENT SUMMARY =====")
print(df[summary_cols].round(4).to_string(index=False))


# =========================
# 10. 計算總體結果
# =========================
forecast_total = df["Forecast_2025"].sum()
actual_total = df["Actual_2025"].sum()
total_error = forecast_total - actual_total
total_ape = abs(total_error) / actual_total

print("\n===== TOTAL RESULT =====")
print(f"Forecast total 2025: €{forecast_total:,.1f}m")
print(f"Actual total 2025:   €{actual_total:,.1f}m")
print(f"Total error:         €{total_error:,.1f}m")
print(f"Total APE:           {total_ape:.2%}")

os.makedirs("./output", exist_ok=True)


# =========================
# 11. 輸出詳細 CSV
# =========================
df.to_csv("./output/infineon_forecast_detail.csv", index=False, encoding="utf-8-sig")


# =========================
# 12. 建立 Power BI 用的長格式資料
# =========================
records = []

for _, row in df.iterrows():
    records.append({
        "Segment": row["Segment"],
        "Type": "Historical",
        "Year": 2021,
        "Value": row["FY2021"]
    })
    records.append({
        "Segment": row["Segment"],
        "Type": "Historical",
        "Year": 2022,
        "Value": row["FY2022"]
    })
    records.append({
        "Segment": row["Segment"],
        "Type": "Historical",
        "Year": 2023,
        "Value": row["FY2023"]
    })
    records.append({
        "Segment": row["Segment"],
        "Type": "Historical",
        "Year": 2024,
        "Value": row["FY2024"]
    })
    records.append({
        "Segment": row["Segment"],
        "Type": "Forecast",
        "Year": 2025,
        "Value": row["Forecast_2025"]
    })
    records.append({
        "Segment": row["Segment"],
        "Type": "Actual",
        "Year": 2025,
        "Value": row["Actual_2025"]
    })

powerbi_df = pd.DataFrame(records)
powerbi_df.to_csv("./output/infineon_powerbi_dataset.csv", index=False, encoding="utf-8-sig")


# =========================
# 13. 輸出 Excel
# =========================
with pd.ExcelWriter("./output/infineon_2025_forecast_model.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Model_Detail", index=False)
    powerbi_df.to_excel(writer, sheet_name="PowerBI_Long_Format", index=False)

print("\n檔案已輸出完成：")
print("- ./output/infineon_forecast_detail.csv")
print("- ./output/infineon_powerbi_dataset.csv")
print("- ./output/infineon_2025_forecast_model.xlsx")
