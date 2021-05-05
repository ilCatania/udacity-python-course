import requests
import random

image_url = 'https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png'
r = requests.get(image_url, allow_redirects=True)
tmp = f'./tmp/{random.randint(0, 100000000)}.png'
open(tmp, 'wb').write(r.content)

print(tmp)

