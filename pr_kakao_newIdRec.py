import re
def solution(new_id):
    new_id = new_id.lower()
    
    r = re.compile('[0-9a-z_.\-]+')
    new_id = r.findall(new_id)
    new_id = ''.join(new_id)
    # print(new_id)
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    new_id = new_id.lstrip('.')
    new_id = new_id.rstrip('.')
    
    if len(new_id) == 0:
        new_id = new_id.replace('','a')
    
    new_id = new_id[:15]
    
    new_id = new_id.rstrip('.')
    
    while len(new_id) <= 2:
        new_id = new_id + new_id[len(new_id) - 1]
    
    return new_id

print(solution("=.="))