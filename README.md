# Mentimeter-Slide-Saver
# 📥 Mentimeter File Downloader

This Python script automates the process of downloading read-only PDFs or slides hosted on the Mentimeter platform by scraping and reconstructing image URLs.

---

## 💡 Project Overview

Mentimeter often hosts slide decks as read-only PDFs. This project allows you to reconstruct and download the individual slide images and compile them into a single PDF—essentially giving you access to the presentation in offline, printable form.

---

## 🚀 Features

- 🔗 Fetches and downloads all slide images from a given Mentimeter presentation
- 📄 Combines images into a high-quality PDF
- ⚡ Fast and minimal setup

---

## 🛠️ How It Works

1. **Open** the Mentimeter slide deck in your browser.
2. **Inspect** the webpage:
   - Right-click → Inspect
   - Go to the **Network** tab
   - Reload the page
3. **Locate one of the image links** under Network (look for `.jpg` or `.webp`).
   Example full link:
https://images.mentimeter.com/import_transforms/9229298/xgzbzqse-ABC-11.jpg?auto=compress%2Cformat&fm=jpg&w=400&expires=1756339199&s=a02b50c594d79dac6c7e32c080269bde

pgsql
Copy
Edit

4. **Copy the base URL** up to the slide index (just before the number):
https://images.mentimeter.com/import_transforms/9229298/edkgtp4c-ABC-

yaml
Copy
Edit

5. **Paste the base URL into the script**, and run it.
6. The script will:
- Download all slide images
- Merge them into a PDF
- Save the final file locally 🎉

---

## 🧑‍💻 Usage

1. Clone the repository or download the script.
2. Install dependencies:
```bash
pip install -r requirements.txt
Run the script:

bash
Copy
Edit
python mentimeter.py
Enter the base URL when prompted (or paste it directly in the code as instructed).

