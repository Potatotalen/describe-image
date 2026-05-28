"""调用阿里云百炼 qwen-vl-max 视觉模型分析图片"""
import base64
import sys
import json
import os
import urllib.request

API_KEY = os.environ.get("DASHSCOPE_API_KEY")
if not API_KEY:
    print("[错误] 请设置环境变量 DASHSCOPE_API_KEY", file=sys.stderr)
    sys.exit(1)
ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
MODEL = "qwen-vl-max"


def describe_image(image_path: str, question: str = "请详细描述这张图片的内容") -> str:
    with open(image_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode("ascii")

    ext = image_path.lower().rsplit(".", 1)[-1]
    mime_map = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "jfif": "image/jpeg",
                "png": "image/png", "gif": "image/gif", "bmp": "image/bmp",
                "webp": "image/webp", "tiff": "image/tiff"}
    mime = mime_map.get(ext, "image/jpeg")

    payload = {
        "model": MODEL,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": {
                    "url": f"data:{mime};base64,{img_data}"
                }}
            ]
        }],
        "max_tokens": 2000
    }

    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    if resp.status != 200:
        error_msg = data.get("error", {}).get("message", str(data))
        return f"[错误] HTTP {resp.status}: {error_msg}"

    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python img_describe.py <图片路径> [问题]")
        sys.exit(1)

    image_path = sys.argv[1]
    question = sys.argv[2] if len(sys.argv) > 2 else "请详细描述这张图片的内容"

    result = describe_image(image_path, question)

    # 直接输出到 stdout，强制 UTF-8
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(result)
