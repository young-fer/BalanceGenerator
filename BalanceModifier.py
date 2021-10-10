import base64
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

# 默认参数
font_size = 42  # 字体大小
balance = 999.99  # 余额
balance_str = "￥" + str(balance)  # 余额字符串

# PIL操作微信截图
we_chat_balance_url = "WeChatBalance.jpg"
we_chat_balance_img = Image.open(we_chat_balance_url)
we_chat_balance_draw = ImageDraw.Draw(we_chat_balance_img)
we_chat_balance_font = ImageFont.truetype('simkai.ttf', font_size)

# 位置参数
# box参数左下右上
wallet_box = (583, 603, 972, 255)
wallet_number_box = (583, 557, 972, 526)


def screenshot_base64():
    f = BytesIO()
    we_chat_balance_img.save(f, 'jpeg')
    # 从内存中取出bytes类型的图片
    data = f.getvalue()
    # 将bytes转成base64
    data = base64.b64encode(data).decode()
    return data


# 覆盖原有余额
def cover_up_balance():
    we_chat_balance_draw.rectangle(xy=wallet_number_box, fill="#2aad67")


# 逐个字符画余额
def draw_text(draw, xy, font, text=balance_str):
    x = xy[0]
    y = xy[1]
    for i in range(0, len(text)):
        draw.text((x, y), text[i], font=font, fill="#92cdad")
        font_width = font.getsize(text[i])[0]
        if text[i] == '.':
            x += font_width * 0.6
        elif text[i] == '￥':
            x += font_width * 0.85
        else:
            x += font_width


# 计算余额字符串长度
def calculate_text_length(font, text=balance):
    text_length = 0
    for i in range(0, len(text)):
        font_width = font.getsize(text[i])[0]
        if text[i] == '.':
            text_length += font_width * 0.6
        elif text[i] == '￥':
            text_length += font_width * 0.85
        else:
            text_length += font_width
    return text_length + 10


# 画余额
def we_chat_balance_change(text=balance):
    text = "￥" + str(text)
    text_length = calculate_text_length(we_chat_balance_font, text=text)
    x = 583 + ((972 - 583) - text_length) / 2 - 5
    y = 526 - 6
    draw_text(we_chat_balance_draw,xy=(x, y), font=we_chat_balance_font, text=text)


def balance_show():
    we_chat_balance_img.show()
