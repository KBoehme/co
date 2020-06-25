# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = pantry_from_dict(json.loads(json_string))
#     result = fridge_from_dict(json.loads(json_string))
#     result = bread_slice_from_dict(json.loads(json_string))
#     result = jelly_from_dict(json.loads(json_string))
#     result = pb_from_dict(json.loads(json_string))
#     result = jelly_slice_from_dict(json.loads(json_string))
#     result = pb_slice_from_dict(json.loads(json_string))
#     result = pbj_sandwhich_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Pantry:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Pantry':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Pantry(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class Fridge:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Fridge':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Fridge(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class BreadSlice:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'BreadSlice':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return BreadSlice(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class Jelly:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Jelly':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Jelly(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class Pb:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Pb':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Pb(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class JellySlice:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'JellySlice':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return JellySlice(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class PBSlice:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'PBSlice':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return PBSlice(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class PBJSandwhich:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'PBJSandwhich':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return PBJSandwhich(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


def pantry_from_dict(s: Any) -> Pantry:
    return Pantry.from_dict(s)


def pantry_to_dict(x: Pantry) -> Any:
    return to_class(Pantry, x)


def fridge_from_dict(s: Any) -> Fridge:
    return Fridge.from_dict(s)


def fridge_to_dict(x: Fridge) -> Any:
    return to_class(Fridge, x)


def bread_slice_from_dict(s: Any) -> BreadSlice:
    return BreadSlice.from_dict(s)


def bread_slice_to_dict(x: BreadSlice) -> Any:
    return to_class(BreadSlice, x)


def jelly_from_dict(s: Any) -> Jelly:
    return Jelly.from_dict(s)


def jelly_to_dict(x: Jelly) -> Any:
    return to_class(Jelly, x)


def pb_from_dict(s: Any) -> Pb:
    return Pb.from_dict(s)


def pb_to_dict(x: Pb) -> Any:
    return to_class(Pb, x)


def jelly_slice_from_dict(s: Any) -> JellySlice:
    return JellySlice.from_dict(s)


def jelly_slice_to_dict(x: JellySlice) -> Any:
    return to_class(JellySlice, x)


def pb_slice_from_dict(s: Any) -> PBSlice:
    return PBSlice.from_dict(s)


def pb_slice_to_dict(x: PBSlice) -> Any:
    return to_class(PBSlice, x)


def pbj_sandwhich_from_dict(s: Any) -> PBJSandwhich:
    return PBJSandwhich.from_dict(s)


def pbj_sandwhich_to_dict(x: PBJSandwhich) -> Any:
    return to_class(PBJSandwhich, x)
