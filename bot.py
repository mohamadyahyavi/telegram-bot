import time
import httpx

TOKEN = "8973074463:AAG1OwoUQf7d7MduUTF06hJX7kC-6h-99KI"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = 0


def get_updates():
    global last_update_id

    res = httpx.get(f"{BASE_URL}/getUpdates").json()

    return res.get("result", [])


def send_message(chat_id, text):
    httpx.get(
        f"{BASE_URL}/sendMessage",
        params={
            "chat_id": chat_id,
            "text": text
        }
    )


while True:
    updates = get_updates()

    for update in updates:

        update_id = update["update_id"]

        if update_id <= last_update_id:
            continue

        last_update_id = update_id

        if "message" in update:
            message = update["message"]
            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            print("User said:", text)

            send_message(chat_id, f"You said: {text}")

    time.sleep(1)