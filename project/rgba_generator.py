from typing import Tuple, Iterator

def rgba_generator() -> Iterator[Tuple[int,int,int,int]]:
    for r in range(256):
        for g in range(256):
            for b in range(256):
                for a in range(0,100,2):
                    yield(r,g,b,a)

def get_rgba_element(i: int) -> Tuple[int,int,int,int]:
    gen=rgba_generator()
    for _ in range(i):
        next(gen)
    return(next(gen))

