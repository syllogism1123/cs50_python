from PIL import Image, ImageDraw


def create_simple_gif(filename):
    # Create multiple frames with clear differences
    images = []
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

    for color in colors:
        # Create a new image for each color
        img = Image.new('RGB', (100, 100), color)

        # Draw a white rectangle in different positions
        draw = ImageDraw.Draw(img)
        draw.rectangle([20, 20, 80, 80], fill=(255, 255, 255))

        images.append(img)

    # Save as animated GIF
    images[0].save(
        filename,
        save_all=True,
        append_images=images[1:],
        duration=200,
        loop=0
    )
    print(f"Created {filename}")


# Create the test GIF
create_simple_gif('test_animation.gif')