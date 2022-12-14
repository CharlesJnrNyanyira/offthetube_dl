from flask import Flask, render_template, request, flash
import time
import youtube_dl


app = Flask(__name__)
app.secret_key = "hubba"

@app.route("/offTube")
def index():
    #flash("Enter the youtube URL below")
    return render_template("index.html")

@app.route("/load", methods=["POST", "GET"])
def send():
    #request.form['link_input']
    flash(str(request.form['link_input']))
    time.sleep(3)
    flash("Download started!")
    link = request.form['link_input']
    #video_url = input("enter url of youtube video:")
    video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    flash("Download complete! Try another download? ")
    return render_template("index.html")
    #return render_template("load.html")
                            

