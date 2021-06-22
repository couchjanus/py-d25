# search.in.file.py

def findPatterns(filename, patterns):
    res = []
    with open(filename, 'r') as file:
        text = ' '.join(file.read().split())
        for pattern in patterns:
            if pattern in text:
                res.append(pattern)
    return res

res = findPatterns('./some.txt', ['hip', 'for example', 'Hello'])

print(res)
