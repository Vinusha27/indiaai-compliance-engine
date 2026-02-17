# 🇮🇳 IndiaAI Financial Compliance Engine (IndAS Focused)

[cite_start]An AI-powered regulatory technology (RegTech) solution designed for the **National Financial Reporting Authority (NFRA)**[cite: 10, 51]. [cite_start]This engine automates the validation of financial documents against **Indian Accounting Standards (IndAS)**[cite: 60].

## 🚀 Key Features
* [cite_start]**Hybrid Extraction**: Uses `pdfplumber` for digital parsing and high-accuracy OCR for scanned documents[cite: 52, 57].
* [cite_start]**Logical Segmentation**: Header-based sectioning (Balance Sheet, P&L, etc.) with metadata tagging for efficient navigation[cite: 52, 58].
* [cite_start]**Explainable AI (XAI)**: Provides specific citations and evidence passages for every compliance flag[cite: 59, 239].
* **Real-time Analytics**: Interactive dashboard with compliance health scoring and data visualization.

## 🛠️ Tech Stack
* **Backend**: Python (Flask)
* **Processing**: pdfplumber, OCR, Heuristic Semantic Mapping
* **Frontend**: HTML5/CSS3 (Government-Branded UI), Chart.js

## 📊 Solution Architecture
![Architecture Diagram](docs/architecture_diagram.png)

## 🎯 Technical Robustness
* [cite_start]**Character Error Rate (CER)**: Target < 0.1% for scanned documents[cite: 227].
* [cite_start]**Segmentation Accuracy (mIoU)**: Targeting > 90% for document region detection[cite: 227].
