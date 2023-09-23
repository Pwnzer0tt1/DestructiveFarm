from server.models import FlagStatus, SubmitResult, Flag
from pwnlib.tubes.remote import *

RESPONSES = {
    FlagStatus.QUEUED: ['ERR'],
    FlagStatus.ACCEPTED: ['OK'],
    FlagStatus.REJECTED: ['DUP', 'OWN', 'OLD', 'INV'],
}

READ_TIMEOUT = 5

def submit_flags(flags:list[Flag], config):
    p = remote(config['SYSTEM_HOST'], int(config['SYSTEM_PORT']))
    p.recvuntil(b'\n\n', timeout=READ_TIMEOUT)
    
    for item in flags:
        p.sendline(item.flag.encode())
        while True:
            elements = p.recvuntil(b'\n', timeout=READ_TIMEOUT).decode().split()
            if len(elements) < 2:
                continue
            else:
                break
        flag, status, message = elements[0], elements[1].upper(), ' '.join(elements[2:])
        response_status = FlagStatus.QUEUED
        if status in RESPONSES[FlagStatus.ACCEPTED]:
            response_status = FlagStatus.ACCEPTED
        elif status in RESPONSES[FlagStatus.REJECTED]:
            response_status = FlagStatus.REJECTED
            
        yield SubmitResult(flag, response_status, message)
    p.close()
    
