from picozero import Speaker, Switch

speaker = Speaker(5)
switch = Switch(18)

BEAT = 0.5 # 120 BPM

defying = [ ['a5', BEAT / 2], ['a5', BEAT], ['e6', BEAT], ['d6', BEAT * 1.5], ['f#5', BEAT], ['a5', BEAT * 1.5],  
              ['d5', BEAT], ['f#5', BEAT * 1.5], ['e5', BEAT / 2], ['e5', BEAT * 1.5]]

def play_song():
    probeer:
        speaker.play(defying)
           
    finally: # Turn speaker off if interrupted
        speaker.off()

switch.when_closed = play_song