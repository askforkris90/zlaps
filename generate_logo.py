"""
Simple PNG logo generator for ZLAPS
Creates a favicon-sized logo representing phone communication via frequency signals
"""

from PIL import Image, ImageDraw, ImageFont
import io
import base64

def create_zlaps_logo(size=256, format='PNG'):
    """
    Create ZLAPS logo - frequency waves representing phone communication
    
    Args:
        size: Image size (default 256x256 for favicon)
        format: Image format ('PNG', 'ICO')
    
    Returns:
        Bytes of the image
    """
    # Create a new image with white background
    img = Image.new('RGB', (size, size), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Background gradient effect (using rectangles)
    # Dark blue gradient background
    for i in range(size):
        color_intensity = int(30 + (i / size) * 20)
        draw.rectangle([(0, i), (size, i+1)], fill=(20, 100, color_intensity))
    
    # Draw frequency waves
    center_x = size // 2
    center_y = size // 2
    wave_color = (0, 220, 255)  # Cyan
    accent_color = (255, 100, 200)  # Magenta
    
    # Draw 3 concentric circular waves
    for wave_num in range(3):
        radius = 30 + (wave_num * 25)
        # Draw wave as circle
        draw.ellipse(
            [(center_x - radius, center_y - radius), 
             (center_x + radius, center_y + radius)],
            outline=wave_color,
            width=3
        )
    
    # Draw phone icon in center
    phone_width = 40
    phone_height = 60
    phone_x = center_x - phone_width // 2
    phone_y = center_y - phone_height // 2
    
    # Phone body
    draw.rounded_rectangle(
        [(phone_x, phone_y), (phone_x + phone_width, phone_y + phone_height)],
        radius=5,
        outline=accent_color,
        width=2
    )
    
    # Phone screen
    screen_margin = 3
    draw.rounded_rectangle(
        [(phone_x + screen_margin, phone_y + screen_margin), 
         (phone_x + phone_width - screen_margin, phone_y + phone_height - 12)],
        radius=2,
        fill=(0, 150, 200),
        outline=wave_color,
        width=1
    )
    
    # Add text "ZLAPS" at bottom
    try:
        # Try to use a system font, fallback to default
        font = ImageFont.truetype("arial.ttf", size=24)
    except:
        font = ImageFont.load_default()
    
    text = "ZLAPS"
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (size - text_width) // 2
    text_y = size - 40
    
    draw.text((text_x, text_y), text, fill=(0, 220, 255), font=font)
    
    return img

def save_logo(filename="zlaps_logo.png"):
    """Create and save the logo"""
    img = create_zlaps_logo(256)
    img.save(filename, 'PNG')
    print(f"✓ Logo saved to {filename}")
    return img

def create_favicon(filename="favicon.ico"):
    """Create favicon version (32x32)"""
    img = create_zlaps_logo(32)
    img.save(filename, 'ICO')
    print(f"✓ Favicon saved to {filename}")
    return img

if __name__ == "__main__":
    # Generate both logo and favicon
    save_logo("zlaps_logo.png")
    create_favicon("favicon.ico")
    print("\\n✓ Logo generation complete!")
    print("  - zlaps_logo.png (256x256) - Use in README/docs")
    print("  - favicon.ico - Use in browser tab")
