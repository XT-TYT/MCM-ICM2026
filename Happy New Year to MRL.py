from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_fireworks_new_year():
    width, height = 800, 400
    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)
    text = "苗润林新年快乐！"
    font = ImageFont.truetype("STXINGKA.TTF", 72)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    glow_color = (200, 50, 50)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        draw.text((position[0] + dx, position[1] + dy), text, fill=glow_color, font=font)
    for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
        draw.text((position[0] + dx, position[1] + dy), text, fill=(150, 30, 30), font=font)
    draw.text(position, text, fill=(255, 0, 0), font=font)
    np.random.seed(42)
    num_particles = 300
    for _ in range(num_particles):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        if (position[0] - text_width/2 < x < position[0] + text_width*1.5 and position[1] - text_height/2 < y < position[1] + text_height*1.5):
            continue
        color_type = np.random.randint(0, 4)
        if color_type == 0:
            color = (255, np.random.randint(0, 100), 0)
        elif color_type == 1:
            color = (255, 255, np.random.randint(0, 100))
        elif color_type == 2:
            color = (255, np.random.randint(100, 200), 0)
        else:
            color = (255, np.random.randint(200, 255), 0)
        size = np.random.randint(1, 4)
        draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
    firework_centers = [(150, 100), (650, 100), (250, 300), (550, 300), (100, 350), (700, 50), (400, 50), (400, 350)]
    color_options = [(255, 255, 0), (255, 165, 0), (255, 0, 0), (255, 255, 255)]
    for center_x, center_y in firework_centers:
        if (position[0] - text_width/2 < center_x < position[0] + text_width*1.5 and position[1] - text_height/2 < center_y < position[1] + text_height*1.5):
            continue
        num_lines = 12
        for i in range(num_lines):
            angle = 2 * np.pi * i / num_lines
            line_length = np.random.randint(15, 35)
            end_x = int(center_x + np.cos(angle) * line_length)
            end_y = int(center_y + np.sin(angle) * line_length)
            color_index = np.random.randint(0, len(color_options))
            line_color = color_options[color_index]
            draw.line([center_x, center_y, end_x, end_y], fill=line_color, width=2)
        draw.ellipse([center_x-3, center_y-3, center_x+3, center_y+3], fill=(255, 255, 255))
    for _ in range(50):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        if (position[0] - text_width/2 < x < position[0] + text_width*1.5 and position[1] - text_height/2 < y < position[1] + text_height*1.5):
            continue
        star_color = (255, 255, np.random.randint(200, 255))
        size = 1
        draw.line([x-size, y, x+size, y], fill=star_color, width=1)
        draw.line([x, y-size, x, y+size], fill=star_color, width=1)
    filename = "苗润林新年快乐_烟花版.png"
    img.save(filename)
    img.show()
    return img

if __name__ == "__main__":
    create_fireworks_new_year()