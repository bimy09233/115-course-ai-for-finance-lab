# HW1 生日五行金融密碼計算器

HW1 實作「生日五行金融密碼計算器」，提供 terminal 與 Jupyter Notebook 操作方式。使用者輸入西元出生年月日後，程式會計算生日數字密碼，並依河圖五行對應規則判斷元素屬性。

## 功能

- 將生日年月日的每一位數字拆開加總。
- 若加總結果大於等於 10，持續拆位相加直到得到 0 到 9 的個位數。
- 依河圖五行對應生日密碼：
  - `1, 6`：木
  - `2, 7`：火
  - `5, 0`：土
  - `4, 9`：金
  - `3, 8`：水
- Terminal 模式輸出文字版河圖五行數字對應表。
- Notebook 模式使用 Matplotlib 顯示河圖五行圖，並高亮使用者的生日密碼。
- 顯示生日數字密碼對應的河圖五行屬性。

## Terminal 操作

在專案根目錄直接帶入生日參數執行：

```bash
uv run python HW1/birthday_wuxing_finance_calculator.py 2000-01-01
```

生日參數支援下列格式：

- `YYYY-MM-DD`，例如 `2000-01-01`
- `YYYYMMDD`，例如 `20000101`
- `YYYY/MM/DD`，例如 `2000/01/01`

也可以不帶生日參數，進入互動輸入模式：

```bash
uv run python HW1/birthday_wuxing_finance_calculator.py
```

Terminal 模式會輸出下列結果：

- 生日數字拆位加總流程
- 最終生日數字密碼
- 河圖五行屬性
- 文字版河圖五行數字對應表

## Jupyter Notebook 操作

在專案根目錄啟動 JupyterLab：

```bash
uv run jupyter lab
```

開啟下列檔案：

```text
HW1/birthday_wuxing_finance_calculator.ipynb
```

依序執行 Notebook 中的儲存格，在「出生日期」欄位選擇西元年月日，再按下「計算生日五行金融密碼」按鈕。

也可以使用傳統 Notebook 介面：

```bash
uv run jupyter notebook
```

Notebook 模式會顯示生日數字拆位加總流程、最終生日數字密碼、河圖五行屬性與 Matplotlib 河圖五行圖。

## 結果欄位說明

- **生日數字密碼**：由出生年月日所有數字反覆加總後得到的 0 到 9 個位數。
- **五行屬性**：依河圖數字對應木、火、土、金、水。
- **Matplotlib 圖表**：外圈顯示 0 到 9，每個數字依五行著色，使用者的生日密碼會放大並加上外框。