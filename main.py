import fluidsynth
from sympy.mpmath import mp
import time
#contains the midinumbers fom all notes from C4 to E5 (C Major) and their number eqivalent in pi 
num_to_midinum = {'0' : 60, '1' : '62','2' : 64, '3' : 65, '4' : 67, '5' : 69, '6' : 71, '7':72, '8' : 74, '9' : 76, '.' : 77}
mp.dps = 1000 #precision for pi

#converts the next digit of pi to a midi number
def play_pi():
	#setup fluidsynth
	fs = fluidsynth.Synth()
	fs.start(driver='alsa')
	sfid = fs.sfload('/usr/share/sounds/sf2/FluidR3_GM.sf2') #load sound font
	fs.program_select(0,sfid,0,0)

	pi = str(mp.pi)
	print 'playing'
	for i in range(mp.dps):
		midinum = num_to_midinum[pi[i]]
		fs.noteon(0,midinum,100) #play the note
		time.sleep(0.5)
	fs.delete()

if __name__ == "__main__":
	play_pi()		
