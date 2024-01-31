from moviepy.editor import *
from moviepy.video.fx.all import *
import TranscriptMaker

from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip



#Dokkan.mp4
#movie1.mp4
#DONE\done0.mp4

TranscriptMaker.tranMake("DONE\done0.mp4")
vid =VideoFileClip("DONE\done0.mp4",fps_source="fps")



generator = lambda txt: TextClip(txt, font='arial', fontsize=36, color='white',size= vid.size,method="caption")
sub = SubtitlesClip("output.srt", generator).set_position(("center",-150), relative=False)

final = CompositeVideoClip([vid, sub])
final.write_videofile("test.mp4", fps=vid.fps)
#vid = vid.fx(resize, (1,100))

#vid = vid.set_fps(24)
#vid = vid.fx(rotate, -90)
print(vid.size)
print(vid.fps)

