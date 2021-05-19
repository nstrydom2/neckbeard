# neckbeard Python library
Neckbeard is a lightweight and easy to use GIF meme generator library built for Python3 application implementation.

## Getting Started

These instructions will get you a copy of the project up and running on your local
machine for development and testing purposes. See deployment for notes on how to
deploy the project on a live system.

### Prerequisites

Python 3.7+ is required to run this application, other than that there are no
prerequisites for the project, as the dependencies are included in the repository.

### Installing

To install the library is as simple as cloning the repository and running

```bash
pip install -e .
```

It is recommended to create an virtual environment prior to installing this library.
Alternatively, you can also install this library via Pip:

```bash
pip install anonfile
```

### Dev Notes

Run unit tests locally:

```bash
pytest --verbosity=2 -s [--token "REDACTED"]
```

Add the `-k test_*` option if you want to test only a single function.

## Usage

Import the module and instantiate the `Neckbeard()` constructor with the image path as
a parameter. Set your meme text, positioning, and color. Then call the process method
to generate your new meme!

```python
from neckbeard import Neckbeard

# create meme from existing GIF
nb = Neckbeard('/home/ghost/Pictures/olaf.gif')
nb.top('tfw you have something important to do')
nb.bottom('but you don't care')

# process the new meme
nb.tip_fedora()

# create GIF meme from mp4
nb = Neckbeard(path='/home/ghost/Videos/wACDCVwsgGSS.mp4', start_time=(8, 52.0), end_time=(9, 15.0))
nb.top('tfw you have something important to do')
nb.bottom('but you don't care')

# process the new meme
nb.tip_fedora()
```

## Command Line Interface

```bash
# get help
anonfile --help

# simple generate a meme
anonfile --top "tfw you have something important to do" --bottom "but you just dgaf" --file /home/ghost/olaf_playing_nose.gif
```

## Built With

* [moviepy](https://zulko.github.io/moviepy/) - Python module for video editing


## Versioning

Navigate to [tags on this repository](https://github.com/nstrydom2/neckbeard/tags)
to see all available versions.

## Authors

| Name             | Mail Address                | GitHub Profile                                |
|------------------|-----------------------------|-----------------------------------------------|
| Nicholas Strydom | nstrydom@gmail.com          | [nstrydom2](https://github.com/nstrydom2)     |

See also the list of [contributors](https://github.com/nstrydom2/neckbeard/contributors)
who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

## Acknowledgments

* Joseph Marie Jacquard
* Charles Babbage
* Ada Lovelace
* My Dad
* Hat tip to anyone whose code was used
* Inspiration
* etc

