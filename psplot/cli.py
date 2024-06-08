import fire

from . import live
from . import plot
from . import capture


def main():
    fire.Fire(dict(live=live.main, plot=plot.main, capture=capture.main))

if __name__ == "__main__":
    main()

