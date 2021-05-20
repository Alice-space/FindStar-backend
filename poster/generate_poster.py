# from io import BytesIO
# import base64
# import requests
from PIL import Image, ImageFont, ImageDraw, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

poster_width = 640
padding = 50
background_color = (0, 0, 0)
text_color = (204, 204, 204)
bottom_text = '''扫描二维码，后台回复“521”，一起寻找属于
你的星星！

数据来源：北京大学青年天文学会（学生社团）
图片来源：cseligman.com
北京大学物理学院团委'''
crop_radius = 20
font_path = './NotoSansSC-Regular.otf'
text_size = 24
bottom_text_size = 18
qrcode_path = './qrcode.png'


def mask_round_crop(image, radius):
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius, fill=255)

    return mask


def generate_poster(text, image_set, output):
    images = []
    for path in image_set:
        images.append(Image.open(path))
    # for url in image_set:
        # r = requests.get(url, stream=True)
        # r.raw.decode_content = True
        # images.append(Image.open(r.raw))
    font = ImageFont.truetype(font_path, text_size)
    bottom_font = ImageFont.truetype(font_path, bottom_text_size)

    draw = ImageDraw.Draw(Image.new("RGB", (0, 0)))

    poster_height = padding * (len(images) + 3)

    multiline = []
    str = ''
    for c in text:
        str += c
        text_width = draw.textsize(str, font)[0]
        if text_width > poster_width - 2 * padding:
            multiline.append(str[:-1])
            str = c
    multiline.append(str)
    text_height = draw.multiline_textsize('\n'.join(multiline), font)[1]
    bottom_text_height = draw.multiline_textsize(bottom_text, bottom_font)[1]
    poster_height += text_height + bottom_text_height
    poster_height += sum(
        map(lambda image: image.size[1] * (poster_width - 2 * padding) // image.size[0], images))
    poster = Image.new("RGB", (poster_width, poster_height), background_color)
    draw = ImageDraw.Draw(poster)

    draw.multiline_text((padding, padding), '\n'.join(
        multiline), font=font, fill=text_color)

    image_top = text_height + 2 * padding
    for image in images:
        image_width, image_height = image.size
        target_width = poster_width - 2 * padding
        image_height = image_height * target_width // image_width
        image_width = target_width
        image = image.resize((image_width, image_height))
        poster.paste(image,
                     (padding, image_top), mask_round_crop(image, crop_radius))
        image_top = image_top + image_height + padding

    draw.multiline_text((padding, image_top), bottom_text,
                        font=bottom_font, fill=text_color)
    qrcode = Image.open(qrcode_path)
    qrcode = qrcode.resize((bottom_text_height, bottom_text_height))
    poster.paste(qrcode,
                 (poster_width - padding - bottom_text_height, image_top), mask=mask_round_crop(qrcode, 10))

    # buffer = BytesIO()
    # poster.save(buffer, format="JPEG")
    # return "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode()
    poster.save(output)
