from moviepy.editor import VideoFileClip , concatenate_videoclips, clips_array
def divideVid(vid,name,length): #path , name of clips
    # make a clip class
    if length == 0:
        main = VideoFileClip(vid,fps_source="fps")
    else:
        main = VideoFileClip(vid,fps_source="fps")
        main = main.subclip(0,length*60)

    # makes videos by whole minuets
    x = int(main.duration) % 60
    seconds = int(main.duration) - x
    mins = int(seconds/60)
    roundVid = main.subclip(0,seconds)
    roundVid = roundVid.set_fps(24)


    for i in range(0,mins):
        minClip = roundVid.subclip(i*60,(i+1)*60)
        minClip.write_videofile(name+str(i)+".mp4")
    return i

