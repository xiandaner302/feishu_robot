from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 白名单：先留空，之后我教你填飞书ID
ALLOWED_USERS = {}

@app.route('/', methods=['POST'])
def bot():
    data = request.get_json()
    if not data:
        return "", 403

    event = data.get("event", {})
    msg = event.get("message", {})
    sender = event.get("sender", {})
    user_id = sender.get("sender_id", {}).get("user_id", "")

    try:
        content = json.loads(msg.get("content", "{}"))
        text = content.get("text", "")
    except:
        return "", 403

    return jsonify({
        "msg_type": "text",
        "content": {
            "text": f"我收到啦！你说：{text}"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
