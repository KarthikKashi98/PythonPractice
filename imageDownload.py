import requests



def download_images(links):
    for i in range(len(links)):
        r = requests.get(links[1])
        image = "image" + str(i) + ".png"
        f = open(image, 'wb')

        f.write(r.content)


links = ["https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1547107887.jpeg",
"https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1548664079.jpeg",
"https://bucketdemotrill.s3-ap-southeast-1.amazonaws.com/1.jpeg_1549956673.jpeg"]
download_images(links)