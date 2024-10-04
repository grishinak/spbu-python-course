from typing import Tuple, Iterator

def rgba_generator() -> Iterator[Tuple[int,int,int,int]]:
    for r in range(256):
        for g in range(256):
            for b in range(256):
                for a in range(0,100,2):
                    yield(r,g,b,a)


