# 客家幣特約商店爬蟲 (Hakka Coin Store Scraper)

這是一個基於 **Selenium** 的 Python 爬蟲工具，用於自動化抓取 [客家幣官網](https://www.hakkacoin.com.tw/store) 的全台特約商店資訊。

## 🚀 功能特點
* **自動翻頁**：自動偵測並點擊「下一頁」，直到抓取完所有店家。
* **動態載入**：內建 `WebDriverWait` 確保頁面內容完全載入後才執行抓取。
* **異常處理**：具備穩健的 `try-except` 機制，避免因網路波動導致程式中斷。
* **資料清洗**：自動移除重複資料，並匯出為 `utf-8-sig` 編碼的 CSV，確保 Excel 開啟不亂碼。

## 🛠️ 安裝環境
請確保您的電腦已安裝 Python 3.8+，並執行以下指令安裝必要套件：
```bash
pip install selenium webdriver-manager pandas
```

🛠️ 環境準備
在執行程式碼之前，請確保您的環境已安裝 Python 並執行以下指令安裝必要的套件：

Bash
pip install selenium webdriver-manager pandas
系統需求
Google Chrome 瀏覽器：本程式使用 Chrome 執行。

Chrome Driver：由 webdriver-manager 自動管理，無需手動下載。

📂 檔案說明
main.py (或您的程式碼檔名): 主程式邏輯。

hakka_stores_final.csv: 執行完畢後產生的資料檔（包含店名、地址）。

🖥️ 使用方式
複製此專案到本地端。

開啟終端機並執行：

```Bash
python your_filename.py
```
程式會開啟 Chrome 視窗（或取消註解 --headless 以背景執行）並開始運作。

執行流程：

連線至首頁。

抓取每一頁的 <article> 標籤內容。

點擊下一頁，直到按鈕變為 disabled 狀態。

儲存資料至 hakka_stores_final.csv。

📊 輸出範例產出的 CSV 檔案格式如下：

Name              Address
某某客家小館       桃園市龍潭區...
傳統工藝坊         新竹縣竹東鎮...
