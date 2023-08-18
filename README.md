## Readme.md

---

### Project Introduction

This project includes two Python files designed to send messages to a specified chat room. Depending on the file, this is achieved using either the `requests` or `telethon` package.

### File Description

1. **telegram_notify_requests.py**: Sends messages using the `requests` package. You will need to obtain a **bot token and chat ID** to use this version.
2. **telegram_notify_telethon.py**: Sends messages using the `telethon` package. You will need to know the **bot token, chat ID, API ID and API hash** to use this version.

### Installation and Usage

#### Requirements

- Python 3.x

#### Installation Steps

1. For `telegram_notify_requests.py`, install the `requests` package:

   ```bash
   pip install requests
   ```
   For `telegram_notify_telethon.py`, install the `telethon` package:

   ```bash
   pip install telethon
   ```

3. Clone the project repository and enter the directory:

   ```bash
   git clone https://github.com/RxChi1d/telegram_notify.git
   cd telegram_notify
   ```

4. Modify the config in *.py file with your information

5. Execute the desired file:

   ```bash
   python telegram_notify_requests.py
   # or
   python telegram_notify_telethon.py
   ```

### Support

If you have any questions or suggestions, feel free to open an issue on GitHub or contact via email.