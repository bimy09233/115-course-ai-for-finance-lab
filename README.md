# 生日五行金融密碼計算器

本專案實作「生日五行金融密碼計算器」，提供 terminal 與 Jupyter Notebook 兩種操作模式。使用者輸入西元出生年月日後，程式會計算生日數字密碼，依河圖五行對應屬性，同時顯示金融投資風格建議；Notebook 模式另提供 Plotly 互動圖表呈現五行與數字關係。

## 功能

- 使用 `DatePicker` 選擇出生日期。
- 將生日年月日的每一位數字拆開加總。
- 若加總結果大於等於 10，持續拆位相加直到得到 0 到 9 的個位數。
- 依河圖五行對應生日密碼：
  - `1, 6`：木
  - `2, 7`：火
  - `5, 0`：土
  - `4, 9`：金
  - `3, 8`：水
- Terminal 模式輸出文字版河圖五行數字對應表。
- Notebook 模式使用 Plotly 顯示互動式河圖五行圖，並高亮使用者的生日密碼。
- 顯示五行金融投資建議與風險提醒。

## 使用 uv 安裝依賴

本專案使用 `uv` 管理 Python 版本、虛擬環境與依賴。請先確認已安裝 `uv`：

```bash
uv --version
```

在專案資料夾中同步依賴：

```bash
uv sync
```

`uv sync` 會依照 `pyproject.toml` 與 `uv.lock` 建立 `.venv`，並安裝 JupyterLab、ipywidgets 與 Plotly。

## 使用方式

### Option 1：Terminal 操作模式

在專案資料夾中直接帶入生日參數執行：

```bash
uv run python main.py 2000-01-01
```

生日參數支援下列格式：

- `YYYY-MM-DD`，例如 `2000-01-01`
- `YYYYMMDD`，例如 `20000101`
- `YYYY/MM/DD`，例如 `2000/01/01`

也可以不帶生日參數，進入互動輸入模式：

```bash
uv run python main.py
```

Terminal 模式會輸出下列結果：

- 生日數字拆位加總流程
- 最終生日數字密碼
- 河圖五行屬性
- 文字版河圖五行數字對應表
- 金融投資風格建議
- 風險提醒

### Option 2：Jupyter Notebook 操作模式

在專案資料夾中啟動 JupyterLab：

```bash
uv run jupyter lab
```

開啟下列檔案：

```text
birthday_wuxing_finance_calculator.ipynb
```

依序執行 Notebook 中的儲存格，在「出生日期」欄位選擇西元年月日，再按下「計算生日五行金融密碼」按鈕。

也可以使用傳統 Notebook 介面：

```bash
uv run jupyter notebook
```

Notebook 模式會顯示生日數字拆位加總流程、最終生日數字密碼、河圖五行屬性、Plotly 河圖五行互動圖與金融投資風格建議。

## 結果欄位說明

- **生日數字密碼**：由出生年月日所有數字反覆加總後得到的 0 到 9 個位數。
- **五行屬性**：依河圖數字對應木、火、土、金、水。
- **Plotly 圖表**：外圈顯示 0 到 9，每個數字依五行著色，使用者的生日密碼會放大並加上外框。
- **金融建議**：依五行屬性提供投資風格、適合關注方向與風險提醒。

## 常見問題

### Widget 沒有顯示

請確認已安裝 `ipywidgets`，並重新啟動 Jupyter kernel：

```bash
uv sync
```

### Plotly 圖表沒有出現

請確認已安裝 `plotly`，並重新執行 Notebook 儲存格：

```bash
uv sync
```

### 按下計算後顯示未選擇日期

請先在「出生日期」欄位選擇日期，再按下計算按鈕。

## 投資風險聲明

本 Notebook 內容僅供課堂學習、資料視覺化與投資風格分析練習，不構成任何投資建議、買賣推薦或收益保證。實際投資前，應自行評估市場風險、資金配置、投資期限與個人承受能力。
