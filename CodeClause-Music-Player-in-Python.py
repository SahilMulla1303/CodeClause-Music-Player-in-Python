from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('520x150'); window.title('CodeClause-Music-Player-in-Python'); window.resizable(False,False)
        Load = Button(window, text = 'Load',  width = 15, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 15,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 15, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 15, font = ('Times', 10), command = self.stop)
        Load.place(x=50,y=40);Play.place(x=200,y=40);Pause.place(x=350,y=40);Stop.place(x=200,y=100) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
        

root = Tk()
app= MusicPlayer(root)
root.mainloop()
