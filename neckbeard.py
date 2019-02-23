from moviepy.editor import *

class NeckBeard():
    def __init__(self):
        pass

    # Generate a gif meme with text
    # parameters:
    #   start_time/end_time format = (4,11.4)
    #   text_postion = tuple ex) ('center', 'bottom')
    def generate_gif(self, vid_path, start_time=None, end_time=None, out='./NEW_MEME.gif', resize=1.0,
                     text=None, text_position=None, text_size=45.0, text_font='Impact', text_color='white'):
        clip = None
        composition = None

        if start_time is not None and \
            end_time is not None:
            clip = (VideoFileClip(vid_path).subclip(start_time, end_time).resize(resize))
        else:
            clip = (VideoFileClip(vid_path).resize(resize))

        if text is not None:
            caption = (TextClip(text, fontsize=text_size, font=text_font, color=text_color)
                .set_position(text_position)
                .set_duration(clip.duration))
            composition = CompositeVideoClip([clip, caption])
        else:
            composition = CompositeVideoClip([clip])

        composition.write_gif(out)

if __name__ == '__main__':
    gif_maker = NeckBeard()

    gif_maker.generate_gif('/home/ghost/Downloads/luke.gif',
                           out='./funny-meme.gif',
                           resize=0.6,
                           text='NOOOOOOO',
                           text_position=('center', 'bottom'))
 
