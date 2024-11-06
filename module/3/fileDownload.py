from requests import get

def fileDownload(url, fileName):
    response = get(url=url, stream=True)
    print(f"Download Started : {fileName}")
    with open(fileName, mode="wb") as f:
        for streamData in response.iter_content(chunk_size=1024):
            f.write(streamData)
    print(f"Download completed {fileName}")
    return

# fileDownload("https://kannan-s3-bucket.s3.ap-south-1.amazonaws.com/Vilangu+.+2022+.+S01+EP01%EA%9E%89+Section+174.mkv", "demo.mkv")


# https://kannan-s3-bucket.s3.ap-south-1.amazonaws.com/images/pngwing.com+(1).png
# https://kannan-s3-bucket.s3.ap-south-1.amazonaws.com/images/pngwing.com+(10).png
for num in range(1,14):
    fileDownload(
        url=f"https://kannan-s3-bucket.s3.ap-south-1.amazonaws.com/images/pngwing.com+({num}).png",
        fileName=f"{num}.png"
    )