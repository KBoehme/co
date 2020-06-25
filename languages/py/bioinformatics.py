# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = fast_q_from_dict(json.loads(json_string))
#     result = bam_from_dict(json.loads(json_string))
#     result = vcf_from_dict(json.loads(json_string))
#     result = bed_from_dict(json.loads(json_string))
#     result = variant_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class FastQ:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'FastQ':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return FastQ(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class BAM:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'BAM':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return BAM(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class Vcf:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Vcf':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Vcf(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class Bed:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Bed':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Bed(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


class Variant:
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Variant':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Variant(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


def fast_q_from_dict(s: Any) -> FastQ:
    return FastQ.from_dict(s)


def fast_q_to_dict(x: FastQ) -> Any:
    return to_class(FastQ, x)


def bam_from_dict(s: Any) -> BAM:
    return BAM.from_dict(s)


def bam_to_dict(x: BAM) -> Any:
    return to_class(BAM, x)


def vcf_from_dict(s: Any) -> Vcf:
    return Vcf.from_dict(s)


def vcf_to_dict(x: Vcf) -> Any:
    return to_class(Vcf, x)


def bed_from_dict(s: Any) -> Bed:
    return Bed.from_dict(s)


def bed_to_dict(x: Bed) -> Any:
    return to_class(Bed, x)


def variant_from_dict(s: Any) -> Variant:
    return Variant.from_dict(s)


def variant_to_dict(x: Variant) -> Any:
    return to_class(Variant, x)
