from __future__ import annotations

from typing import Optional, Literal, overload
from typing_extensions import reveal_type


class Cat:
    def __init__(self, x: int) -> None:
        self.x = x

    # inplace False
    @overload
    def increase_x(
            self,
            increase: int,
            say_goodbye: bool = ...,
            say_hello: bool = ...,
            inplace: Literal[False] = ...,
    ) -> Cat:
        ...

    # inplace True, all kwargs present
    @overload
    def increase_x(
            self,
            increase: int,
            say_goodbye: bool,
            say_hello: bool,
            inplace: Literal[True]
    ) -> None:
        ...

    # inplace True, say_hello present
    @overload
    def increase_x(
            self,
            increase: int,
            *,
            say_hello: bool,
            inplace: Literal[True]
    ) -> None:
        ...

    # inplace True, say_goodbye present
    @overload
    def increase_x(
            self,
            increase: int,
            say_goodbye: bool,
            *,
            inplace: Literal[True]
    ) -> None:
        ...

    # inplace True, no other kwargs
    @overload
    def increase_x(
            self,
            increase: int,
            *,
            inplace: Literal[True]
    ) -> None:
        ...

        # inplace bool

    @overload
    def increase_x(
            self,
            increase: int,
            say_goodbye: bool = ...,
            say_hello: bool = ...,
            inplace: bool = ...,
    ) -> Optional[Cat]:
        ...

    def increase_x(
            self,
            increase: int,
            say_goodbye: bool = False,
            say_hello: bool = False,
            inplace: bool = False,
    ):
        if say_hello:
            print('hello')
        if say_goodbye:
            print('goodbye')
        if inplace:
            self.x += 1
            return None
        else:
            cat = Cat(self.x + 1)
            return cat


cat = Cat(0)

inplace: bool = True

reveal_type(cat.increase_x(1, inplace=True))
reveal_type(cat.increase_x(1, inplace=False))
reveal_type(cat.increase_x(1))
reveal_type(cat.increase_x(1, inplace=inplace))
reveal_type(cat.increase_x(1, say_hello=True, inplace=True))
reveal_type(cat.increase_x(1, say_hello=True, inplace=False))
reveal_type(cat.increase_x(1, say_hello=True))
reveal_type(cat.increase_x(1, say_hello=True, inplace=inplace))
reveal_type(cat.increase_x(1, say_goodbye=True, inplace=True))
reveal_type(cat.increase_x(1, say_goodbye=True, inplace=False))
reveal_type(cat.increase_x(1, say_goodbye=True))
reveal_type(cat.increase_x(1, say_goodbye=True, inplace=inplace))
reveal_type(cat.increase_x(1, say_hello=True, say_goodbye=True, inplace=True))
reveal_type(cat.increase_x(1, say_hello=True, say_goodbye=True, inplace=False))
reveal_type(cat.increase_x(1, say_hello=True, say_goodbye=True))
reveal_type(cat.increase_x(1, say_hello=True, say_goodbye=True, inplace=inplace))
