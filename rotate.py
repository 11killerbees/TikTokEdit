from moviepy.editor import *
from moviepy.video.fx.all import *

def start(top,bot,name):

    # make a clip class
    top = VideoFileClip(top,fps_source="fps")
    bot = VideoFileClip(bot,fps_source="fps")

    top = top.set_fps(24)
    bot = bot.set_fps(24)

   # test = AudioFileClip("movie1.mp4")
    #test.write_audiofile("test.mp3")


    # makes a sub clip from t1 to t2
    topClip = top
    botClip = bot


    num = topClip.size[1]
    num2 = botClip.size[1]
    botClip = botClip.fx(crop,  y_center= 700,  height=num2-num,x_center= botClip.size[0]/2, width= botClip.size[0])
    topClip = topClip.fx(crop,  x_center= (num/2)+100, width=botClip.size[0])




    #topClip = topClip.fx(resize,num)

    topClip = topClip.fx(even_size)
    botClip = botClip.fx(even_size)
    #rotates the clips ccw by 90
    topClip = topClip.fx(rotate,-90)
    botClip = botClip.fx(rotate,-90)



    # this adds the clips together side by side
    tempClip = clips_array([[botClip,topClip]])


    #makes a new mp4 file
    tempClip.write_videofile("tempClip.mp4")


    # new clip to fix glitch
    finalClip = VideoFileClip("tempClip.mp4")

    # rotated clip
    finalClip = finalClip.fx(rotate,90)

    finalClip = finalClip.fx(even_size)


    finalClip.write_videofile(name+".mp4")


