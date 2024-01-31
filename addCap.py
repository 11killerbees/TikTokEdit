from moviepy.editor import *
from moviepy.video.fx.all import *
import TranscriptMaker

from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def addCap(input,output):
    TranscriptMaker.tranMake(input)
    vid =VideoFileClip(input,fps_source="fps")



    generator = lambda txt: TextClip(txt, font='arial', fontsize=36, color='white',size= vid.size,method="caption")
    sub = SubtitlesClip("output.srt", generator).set_position(("center",-150), relative=False)

    final = CompositeVideoClip([vid, sub])
    final.write_videofile(output, fps=24)


