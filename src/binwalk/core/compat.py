
def str2bytes(string):
    if isinstance(string, str):
        return bytes(string, 'latin1')
    return string


def bytes2str(bs):
    if isinstance(bs, bytes):
        return bs.decode('latin1')
    return bs
