import pytumblr
from math import ceil
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import os

def download(url, pathname):
    # taken from: https://www.thepythoncode.com/article/download-web-page-images-python
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))

key_file = open('./key/key.txt', 'r')
key = key_file.readlines()[0]
blogname = input('Enter your blog identifier <blogname>.tumblr.com (e.g. staff.tumblr.com): \n')

client = pytumblr.TumblrRestClient(key)

posts_data = client.posts(blogname, limit=50)
post_no = 1

if "meta" in posts_data.keys() and posts_data["meta"]["status"] != 200:
    raise ValueError("An error occured! Maybe blogname wrong.")

chunks = ceil(posts_data["blog"]["posts"] / 50)


for i in range(0, chunks):
    posts = posts_data["posts"]

    for post in posts:
        # Scrape text
        f = open("./data/entry_" + str(post_no) + ".txt", "w")
        html_text = post["body"]
        text = BeautifulSoup(html_text, features="html.parser")
        f.write(text.get_text(separator="\n"))
        f.close()

        img_path = "./images/entry_" + str(post_no) + "/"
        # if path not exist => create
        if not os.path.isdir(img_path):
            os.makedirs(img_path)
        # scrape image
        for img in tqdm(text.find_all("img"), "Extracting images"):
            img_url = img.attrs.get("src")
            if not img_url:
                # if img does not contain src attribute, just skip
                continue
            ### oben auf 50 ändern von 1
                
            download(img_url, img_path)
        post_no += 1
    posts_data = client.posts(blogname, limit=50, offset=50*(i+1))





