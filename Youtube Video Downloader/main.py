from pytube import YouTube

start = True
while start:
    try:
        url = input("Enter url of Youtube Video that you would like to download:\n")
        yt = YouTube(url)
        start = False
    except:
        print("Please enter a valid url!")

vd_stream = yt.streams.get_highest_resolution()
video = vd_stream.download(output_path="G:\\Downloads")
print(f"{yt.title} successfully downloaded!")