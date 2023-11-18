from server.models import FlagStatus, SubmitResult, Flag
from pwnlib.tubes.remote import *

RESPONSES = {
    FlagStatus.QUEUED: ['OFFLINE'],
    FlagStatus.ACCEPTED: ['OK'],
    FlagStatus.REJECTED: ['ERR'],
}

READ_TIMEOUT = 10

def submit_flags(flags:list[Flag], config):
    p = remote(config['SYSTEM_HOST'], int(config['SYSTEM_PORT']))
    p.recvuntil(b'\n\n', timeout=READ_TIMEOUT)
    try:
        for item in flags:
            p.sendline(item.flag.encode())
            while True:
                elements = p.recvuntil(b'\n', timeout=READ_TIMEOUT).decode().split()
                if len(elements) < 1:
                    continue
                else:
                    break
            status, message = elements[0][1:][:-1], ' '.join(elements[1:])
            response_status = FlagStatus.QUEUED
            if status in RESPONSES[FlagStatus.ACCEPTED]:
                response_status = FlagStatus.ACCEPTED
            elif status in RESPONSES[FlagStatus.REJECTED]:
                response_status = FlagStatus.REJECTED

            yield SubmitResult(item.flag, response_status, message)
        p.close()
    except EOFError:
        print("Sumbitter connection closed!")
        pass
