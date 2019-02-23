from moviepy.editor import *

class NeckBeard():
    def __init__(self):
        self.trump_vid = '/home/ghost/Downloads/trumps-most-awkward-moments-of-2018.mp4'

    def generate_meme(self, pic_path):
        with open(pic_path) as in_file:
            pass

    # Generate a gif
    # parameters:
    #   start_time/end_time format = 4,11.4
    #   text_postion = tuple ex) ('center', 'bottom')
    def generate_gif(self, start_time, end_time, text=None, text_position=None):
        clip = (VideoFileClip(self.trump_vid).subclip((start_time), (4,11.4)).resize(0.45))

        text = (TextClip('I\'m just going to leave this here', fontsize=45.0, font='Impact', color='white')
            .set_position(('center', 'bottom'))
            .set_duration(clip.duration))

        composition = CompositeVideoClip([clip, text])
        composition.write_gif('leave_this_here.gif')

    def generate_baby_gif(self):
        vid = '/home/ghost/Downloads/reddit-cringe-compilation-most-awkward-moments-2019.mp4'

        clip = (VideoFileClip(vid).subclip((4,10.6), (4,13.4)).resize(0.3))

        text = (TextClip('The Priest really takes his job seriously'.upper(), fontsize=18.0, font='Impact', color='white')
            .set_position(('center', 'top'))
            .set_duration(clip.duration))

        composition = CompositeVideoClip([clip, text])
        composition.write_gif('priest_small.gif')


if __name__ == '__main__':
    gif_maker = NeckBeard()

    gif_maker.generate_baby_gif()
 
