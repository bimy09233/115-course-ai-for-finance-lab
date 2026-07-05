# 115 人工智慧金融投資決策 Lab

本專案整理「人工智慧金融投資決策」課程作業與實作練習。各作業會依序放在 `HW1/`、`HW2/`、`HW3/` 等目錄中，根目錄 README 作為專案總覽、環境建置與執行入口索引。

## Table of Contents

- [專案摘要](#專案摘要)
- [目錄結構](#目錄結構)
- [環境建置](#環境建置)
- [執行方式](#執行方式)
- [作業索引](#作業索引)

## 專案摘要

目前已完成 HW1「生日五行金融密碼計算器」，提供 terminal 與 Jupyter Notebook 操作方式。使用者輸入西元出生年月日後，程式會計算生日數字密碼，並依河圖五行對應規則判斷元素屬性。

後續 HW2、HW3 等作業會持續新增至獨立目錄，並在本 README 的作業索引補上摘要與執行方式。

## 目錄結構

```text
.
├── HW1/
│   ├── README.md
│   ├── birthday_wuxing_finance_calculator.py
│   └── birthday_wuxing_finance_calculator.ipynb
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

## 環境建置

本專案使用 `uv` 管理 Python 版本、虛擬環境與依賴。請先確認已安裝 `uv`：

```bash
uv --version
```

在專案根目錄同步依賴：

```bash
uv sync
```

`uv sync` 會依照 `pyproject.toml` 與 `uv.lock` 建立 `.venv`，並安裝目前作業需要的 JupyterLab、Notebook、ipywidgets 與 Matplotlib。

## 執行方式

### Terminal

HW1 terminal 版執行入口：

```bash
uv run python HW1/birthday_wuxing_finance_calculator.py 2000-01-01
```

若不帶生日參數，程式會進入互動輸入模式：

```bash
uv run python HW1/birthday_wuxing_finance_calculator.py
```

### JupyterLab

在專案根目錄啟動 JupyterLab：

```bash
uv run jupyter lab
```

開啟 `HW1/birthday_wuxing_finance_calculator.ipynb`，依序執行 Notebook cells。

也可以使用傳統 Notebook 介面：

```bash
uv run jupyter notebook
```

## 作業索引

| 作業 | 摘要 | 入口 |
| --- | --- | --- |
| HW1 | 生日五行金融密碼計算器，依生日數字密碼判斷河圖五行屬性。 | [`HW1/README.md`](HW1/README.md) |
| HW2 | 待新增。 | 待新增 |
| HW3 | 待新增。 | 待新增 |
