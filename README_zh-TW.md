## Readme.md

---

### 專案介紹

這個專案包括兩個 Python 檔案，設計用於向指定的聊天室發送訊息。根據檔案的不同，這可以使用 `requests` 或 `telethon` 套件來實現。

### 檔案介紹

1. **telegram_notify_requests.py**: 使用 `requests` 套件發送訊息。您將需要獲取**bot token 和 chat ID**才能使用此版本。
2. **telegram_notify_telethon.py**: 使用 `telethon` 套件發送訊息。您將需要知道**bot token、chat ID、API ID 和 API hash**才能使用此版本。

### 安裝與使用

#### 環境需求

- Python 3.x

#### 安裝步驟

1. 對於 `telegram_notify_requests.py`，請安裝 `requests` 套件：

   ```bash
   pip install requests
   ```
   對於 `telegram_notify_telethon.py`，請安裝 `telethon` 套件：

   ```bash
   pip install telethon
   ```

3. 克隆專案存儲庫並進入目錄：

   ```bash
   git clone https://github.com/RxChi1d/telegram_notify.git
   cd telegram_notify
   ```

4. 修改 *.py 檔案中的配置，填入您的訊息

5. 執行所需的檔案：

   ```bash
   python telegram_notify_requests.py
   # 或
   python telegram_notify_telethon.py
   ```

### 支援

若有任何問題或建議，歡迎在 GitHub 上開 issue 或透過 email 聯絡。