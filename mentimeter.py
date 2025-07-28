import requests
from PIL import Image
import os

# Base URL

base_url = "https://images.mentimeter.com/import_transforms/9229298/edkgtp4c-W05_HEFCSProfessionalPractice-"

# Folder to save images
folder = "mentimeter_images"
os.makedirs(folder, exist_ok=True)

images = []
index = 1

while True:
    image_url = f"{base_url}{index}.jpg"
    image_path = os.path.join(folder, f"slide_{index}.jpg")
    
    try:
        print(f"Downloading: {image_url}")
        response = requests.get(image_url)
        if response.status_code != 200:
            print(f"Stopped at index {index} (HTTP {response.status_code})")
            break
        with open(image_path, "wb") as f:
            f.write(response.content)
        images.append(image_path)
        index += 1
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")
        break

# Convert to PDF
if images:
    image_list = [Image.open(img).convert("RGB") for img in images]
    pdf_path = "mentimeter_slides.pdf"
    image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
    print(f"PDF saved as: {pdf_path}")
else:
    print("No images downloaded.")
