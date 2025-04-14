import random
import time
from PIL import Image, ImageDraw

def draw_dice_face(value):
    img = Image.new('RGB', (200, 200), 'white')
    draw = ImageDraw.Draw(img)

    draw.rectangle([10, 10, 190, 190], outline='black', fill='white', width=5)

    dot_positions = {
        1: [(100, 100)],
        2: [(70, 70), (130, 130)],
        3: [(70, 70), (100, 100), (130, 130)],
        4: [(70, 70), (70, 130), (130, 70), (130, 130)],
        5: [(70, 70), (70, 130), (100, 100), (130, 70), (130, 130)],
        6: [(70, 70), (70, 100), (70, 130), (130, 70), (130, 100), (130, 130)],
    }

    for pos in dot_positions[value]:
        draw.ellipse([pos[0]-15, pos[1]-15, pos[0]+15, pos[1]+15], fill='black')

    return img

def roll_dice_animation(rolls=10):
    for _ in range(rolls):
        dice_value = random.randint(1, 6)
        
        dice_image = draw_dice_face(dice_value)
        
        dice_image.show()
        
        time.sleep(0.2)  

    final_value = random.randint(1, 6)
    print(f"Final roll: {final_value}")
    final_image = draw_dice_face(final_value)
    final_image.show()

if __name__ == "__main__":
    while True:
        input("Press Enter to roll the dice...")
        roll_dice_animation(10)  