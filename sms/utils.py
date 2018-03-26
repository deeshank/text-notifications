import re

def parse_message(message):
    if message:
        req_time = _parse_time(message)
        req_date = _parse_date(message)
    return req_time,req_date

def _parse_time(message):
    req_time = ''
    resp = re.match(r'.*\s+([0-9]+):*([0-9]*)\s*(AM|PM)*\s+.*', message)
    if resp:
        req_time += resp.group(1) if resp.group(1) else ''
        req_time += ':'+resp.group(2) if resp.group(2) else ''
        req_time += ' '+resp.group(3) if resp.group(3) else ''
    return req_time



def _parse_date(message):
    req_day = ''
    resp = re.match(r'.*([0-9]+)/([0-9]+).*', message)
    if resp:
        req_day += resp.group(1) if resp.group(1) else ''
        req_day += '/'+resp.group(2) if resp.group(2) else ''
    return req_day
