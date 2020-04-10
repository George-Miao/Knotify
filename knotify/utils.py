from typing import List


def build_uri(scheme: str, loc: str, paths: List[str] = [], **kwargs) -> str:
    """
    Used to build URIs
    :param scheme: scheme e.g. http in http://google.com/
    :param loc: netloc e.g. google.com in http://google.com/
    :param paths: a list of paths e.g. ["example", "path"] in http://google.com/example/path
    :param kwargs: parameters e.g. {NETLOC}?k1=v&k2=v
    :return:
    """
    path = "/" + "/".join(paths) if paths else ""
    params = "?" + "&".join([f"{k}={kwargs[k]}" for k in kwargs.keys()]) if kwargs else ""
    return "{}://{}{}{}".format(scheme, loc, path, params)
