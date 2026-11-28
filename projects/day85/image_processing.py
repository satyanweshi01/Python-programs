from PIL import Image, ImageDraw, ImageFont


def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert('RGBA')
    width, height = input_image.size
    # print(type(width),type(height))

    overlay = Image.new('RGBA', input_image.size, (255,255,255,0))

    draw = ImageDraw.Draw(overlay)

    watermark_color_pattern = (255,255,255,50)

    for i in range(0, width+height, 25):
        draw.line([(0,height-i), (i, height)], fill = watermark_color_pattern, width = 10)

    font_size = width/10

    font = ImageFont.truetype('./day85/arial.ttf',font_size)

    left, top, right, bottom = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = right - left, bottom - top

    centerx = (width - text_width) //2
    centery = (height - text_height) //2

    watermark_color_text = (0,0,0,100)

    draw.text((centerx,centery),watermark_text, fill = watermark_color_text, font= font)
    
    watermarked_image = Image.alpha_composite(input_image, overlay)

    watermarked_image.save(output_image_path)




# add_watermark_overlay('./day85/img.jpg','./output.png',"Watermark")