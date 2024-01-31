from moviepy.editor import VideoFileClip , concatenate_videoclips, clips_array

# make a clip class
clip1 = VideoFileClip("movie1.mp4")



# makes a sub clip from t1 to t2
clip2 = clip1.subclip(0,20)
clip3 = clip1.subclip(0,20)

clip2.set_position("center","top")
#clip3.set_position(1000,1000)


#adds two clips together
combinedClips = concatenate_videoclips([clip2,clip3])

# this adds the clips together side by side
combinedClips2 = clips_array([[clip2,clip3]])


#makes a new mp4 file
combinedClips2.write_videofile("testClip.mp4")

