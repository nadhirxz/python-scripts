# resize all images in folder

#https://gist.github.com/ihercowitz/642650/f01986c0b1ebd04be588b196eb3ffefe9853e113

from PIL import Image
import os, sys

SIZE = 200

def resizeImage(infile, output_dir, size):
	outfile = os.path.splitext(infile)[0]
	extension = os.path.splitext(infile)[1]

	if infile != outfile:
		try:
			im = Image.open(infile)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(f"{output_dir}/{outfile}{extension}", "JPEG")
		except IOError:
			print(f"cannot reduce image for {infile}")


if __name__ == "__main__":
	output_dir = "resized"
	dir = os.getcwd()

	if not os.path.exists(os.path.join(dir, output_dir)):
		os.mkdir(output_dir)

	if sys.argv[1]: SIZE = int(sys.argv[1])

	for file in os.listdir(dir):
		resizeImage(file, output_dir, (SIZE, SIZE))
