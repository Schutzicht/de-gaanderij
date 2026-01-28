import urllib.request
import os
import ssl
import time

# Bypass SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

image_urls = [
    "https://nl-prod.bbimages.eu/images/e/2/0/e20a3217-bd45-40c8-814e-b21779df5215_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/1/6/d/16d799c3-4a1d-4c14-94a7-2a192741ce5f_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/0/6/0/0609d702-4af9-4a65-b3be-4f16a7b3ff6a_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/9/f/e/9feb7396-55e2-4087-add8-efc05c28682d_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/b/3/8/b389d34e-4866-482e-adc4-b45ce5b130c6_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/1/f/e/1fe0bfef-039a-43e7-8e11-24bf9ef9a7de_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/2/3/b/23beaf58-27e3-4550-b751-26d466330da1_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/8/2/7/827d102d-67df-4073-9eb1-a0500eb4289d_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/e/b/4/eb4a379d-d22a-414d-9d3e-15931660f740_mw1280.webp",
    "https://nl-prod.bbimages.eu/images/5/f/4/5f41df62-bb52-4f46-8b7f-6c5905952a1f_mw1280.webp"
]

output_dir = "public/images/de-gaanderij"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def download_image(img_url, filename):
    try:
        req = urllib.request.Request(
            img_url, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
        )
        print(f"Downloading {filename}...")
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(response.read())
        print(f"Saved {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")
        return False

# Download Hero (First image)
download_image(image_urls[0], "hero-main.webp")

# Download others
for i, url in enumerate(image_urls[1:]):
    download_image(url, f"gallery_{i+1:02d}.webp")

print("Done downloading images.")
