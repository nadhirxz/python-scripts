import requests, os, sys
from tqdm import tqdm
from urllib.request import urlopen


def download(url, dst):
	"""
    @param: url to download file
    @param: dst place to put the file
    """
	file_size = int(urlopen(url).info().get('Content-Length', -1))
	if os.path.exists(dst):
		first_byte = os.path.getsize(dst)
	else:
		first_byte = 0
	if first_byte >= file_size:
		return file_size
	header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
	pbar = tqdm(total=file_size, initial=first_byte, unit='B', unit_scale=True, desc=url.split('/')[-1])
	req = requests.get(url, headers=header, stream=True)
	with (open(dst, 'ab')) as f:
		for chunk in req.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
				pbar.update(1024)
	pbar.close()
	return file_size


url = sys.argv[1]
try:
	path = sys.argv[1]
except:
	path = "C:\\Users\\Nadhir\\Desktop\\"
name = url.split("/")
name = name[len(name) - 1]
download(url, path)