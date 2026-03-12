import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

# 1. 初始化
chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

all_stores = []

def logger(msg):
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    print(f"[{timestamp}] {msg}")

try:
    logger("開始連線至客家幣店家網頁...")
    driver.get("https://www.hakkacoin.com.tw/store")
    wait = WebDriverWait(driver, 20)

    page = 1
    while True:
        logger(f"=== 正在處理第 {page} 頁 ===")
        
        # A. 等待載入
        try:
            wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))
            time.sleep(2)
        except Exception as e:
            logger(f"等待頁面載入逾時: {e}")

        # B. 抓取資料
        articles = driver.find_elements(By.TAG_NAME, "article")
        current_page_names = []
        
        for art in articles:
            try:
                name = art.find_element(By.TAG_NAME, "h3").text.strip()
                addr = art.find_element(By.TAG_NAME, "address").text.strip()
                if name:
                    all_stores.append({"Name": name, "Address": addr})
                    current_page_names.append(name)
            except:
                continue
        
        logger(f"本頁抓取完畢，目前總累計: {len(all_stores)} 筆")
        first_name_before = current_page_names if current_page_names else "NONE"

        # C. 翻頁邏輯 (加上 Try-Except 保護，不讓它跳出 while)
        try:
            next_li = driver.find_element(By.CSS_SELECTOR, "li.v-pagination__next")
            next_btn = next_li.find_element(By.TAG_NAME, "button")
            
            if "v-btn--disabled" in next_btn.get_attribute("class"):
                logger("偵測到最後一頁，結束任務。")
                break

            # 執行點擊
            actions = ActionChains(driver)
            actions.move_to_element(next_btn).perform()
            time.sleep(0.5)
            next_btn.click()
            logger("已點擊下一頁，開始偵測頁面更新...")

            # D. 偵測更新 (優化版：比對整頁文字)
            is_changed = False
            for i in range(5): # 最多等 5 秒
                time.sleep(1)
                # 重新抓取當前頁面所有 article 的文字
                new_articles = driver.find_elements(By.TAG_NAME, "article")
                if len(new_articles) > 0:
                    # 抓取新頁面第一筆店名的文字內容
                    new_first_name = new_articles.text.split('\n') # 直接取第一行文字，通常是店名
                    
                    if new_first_name != first_name_before:
                        logger(f"頁面更新成功: {first_name_before} -> {new_first_name}")
                        is_changed = True
                        break
                else:
                    logger("偵測中... 頁面暫時沒有 article 標籤")


            
            if not is_changed:
                logger("警告：8秒內未偵測到內容變化，將強制繼續下一頁。")
            
            page += 1

        except Exception as e:
            logger(f"翻頁過程發生異常 (已捕獲): {e}")
            logger("嘗試強制進入下一循環...")
            time.sleep(3) # 發生錯誤時停頓一下，避免無限快速報錯
            page += 1
            continue # 關鍵：不中斷，繼續嘗試下一頁

    # 4. 儲存結果
    df = pd.DataFrame(all_stores)
    df.drop_duplicates(subset=['Name', 'Address'], inplace=True)
    df.to_csv('hakka_stores_final.csv', index=False, encoding='utf-8-sig')
    logger(f"任務完成！檔案已存檔，共計 {len(df)} 筆。")

finally:
    driver.quit()
