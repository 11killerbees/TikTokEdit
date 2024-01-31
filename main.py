import rotate
import divideVideo
import addCap
top = "movie1.mp4"
bot = "Dokkan1.mp4"
length = 8

vids=divideVideo.divideVid(top,"TOP\\topVid",length)
divideVideo.divideVid(bot,"BOT\\botVid",length)
for i in range(vids+1):
    v1 = "TOP\\topVid"+str(i)+".mp4"
    v2 = "BOT\\botVid" + str(i) + ".mp4"
    ###############################
    v3 = "NO_SUB\\noSub"+str(i)
    rotate.start(v1,v2,v3)
    addCap.addCap(v3+".mp4","DONE\done"+str(i)+".mp4")
