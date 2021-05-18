from pathlib import Path
from typing import Tuple

from moviepy.editor import *

__version__ = "0.1.2"
package_name = "neckbeard"
python_major = "3"
python_minor = "7"

try:
    assert sys.version_info >= (int(python_major), int(python_minor))
except AssertionError:
    raise RuntimeError(
        f"{package_name!r} requires Python {python_major}.{python_minor}+ (You have Python {sys.version})")


class Neckbeard:
    _out = Path('./NEW_MEME.gif')
    _start_time = None
    _end_time = None
    _clip = None
    _top_caption = None
    _bottom_caption = None

    def __init__(self,
                 path,
                 start_time: Tuple[int, float] = _start_time,
                 end_time: Tuple[int, float] = _end_time,
                 out: Path = _out):
        self.vid_path = path
        self.out = out
        self.start_time = start_time
        self.end_time = end_time
        self.top_caption = self._top_caption
        self.bottom_caption = self._bottom_caption
        self.clip = self._set_time(path, start_time, end_time)

    @staticmethod
    def _set_time(path, start, end):
        if start is not None and \
                end is not None:
            return VideoFileClip(path).subclip(start, end).resize(1.0)
        else:
            return VideoFileClip(path).resize(1.0)

    def top(self, msg, text_size=45.0, text_font='Impact', text_color='white'):
        self.top_caption = (TextClip(msg, fontsize=text_size, font=text_font, color=text_color)
                            .set_position(('center', 'top'))
                            .set_duration(self.clip.duration))

    def bottom(self, msg, text_size=45.0, text_font='Impact', text_color='white'):
        self.bottom_caption = (TextClip(msg, fontsize=text_size, font=text_font, color=text_color)
                               .set_position(('center', 'bottom'))
                               .set_duration(self.clip.duration))

    # Generate a gif meme with text
    # parameters:
    #   start_time/end_time format = (4,11.4)
    #   text_postion = tuple ex) ('center', 'bottom')
    def tip_fedora(self):
        try:
            comp_parm = []
            if self.clip is not None:
                comp_parm.append(self.clip)

            if self.top_caption is not None:
                comp_parm.append(self.top_caption)

            if self.bottom_caption is not None:
                comp_parm.append(self.bottom_caption)

            composition = CompositeVideoClip(comp_parm)
            composition.write_gif(self.out)

            print(f"*tips fedora* M'lady, your meme is ready! ({self.path})")

        except Exception as ex:
            raise ex


if __name__ == '__main__':
    gif = Neckbeard(path='F:\\wACDCVwsgGSS.mp4', start_time=(8, 52.0), end_time=(9, 15.0))
    gif.top('WOAH, JOE...')
    gif.bottom('YOU WANNA CALM DOWN A LITTLE')
    gif.tip_fedora()
