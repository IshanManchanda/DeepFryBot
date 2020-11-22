from os import environ, remove
from io import BytesIO
from os import environ, remove
from os.path import abspath, isfile, join as path_join, split as path_split
from random import shuffle
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from PIL import Image, ImageEnhance, ImageOps
from discord import File
from numpy import arcsin, arctan, array, copy, pi, sin, sqrt, square, sum
from numpy.random import normal, random
from pyimgur import Imgur

bin_path = path_split(abspath(__file__))[0]


# @run_async
# def fry_image(update, url, number_of_cycles, args):
async def fry_image(message, attachment):
	# log_info('Starting Image Fry')
	# number_of_emojis = (
	# 	3 if args['high-fat']
	# 	else 1 if args['low-fat']
	# 	else 0 if args['no-fat']
	# 	else 2
	# )
	# bulge_probability = (
	# 	0.75 if args['heavy']
	# 	else 0 if args['light']
	# 	else 0.45
	# )
	# magnitude = 4 if args['deep'] else 1 if args['shallow'] else 2

	name = message.author.name
	filename = '%s_%s_%s.png' % (
		message.guild.id if message.guild else '<NONE>',
		name,
		message.id
	)
	filepath = path_join(bin_path, 'temp', filename)
	print(attachment.filename)

	data = await attachment.read()
	# print('Read img')
	img = Image.open(BytesIO(data))
	if img.mode != 'RGB':
		img = img.convert('RGB')
	img.save(filepath)
	print('Saved image!')

	# caption = __get_caption(name, number_of_cycles, args)
	caption = f'Requested by {name}.'

	# success, img = __get_image(url)
	# if not success:
		# log_error('Image download failed')
		# return
	# log_info('Image successfully downloaded')

	# img = __fry(
	# 	img, 1, 2,
	# 	0.4, False, False
	# )

	# log_info('Frying effects starting')
	fs = [__posterize, __sharpen, __increase_contrast, __colorize]
	# for _ in range(number_of_cycles):
	shuffle(fs)
	for f in fs:
		img = f(img, 2)
	# log_info('Frying effects applied')

	bio = BytesIO()
	bio.name = filename
	img.save(bio, 'PNG')
	bio.seek(0)
	await message.channel.send(caption, file=File(bio, filename))

	# log_info('Image saved and replied')
	img.save(filepath, 'PNG')
	# __upload_to_imgur(filepath, caption)


# log_info('Image frying process completed')


def __get_image(url):
	for _ in range(5):
		try:
			return 1, Image.open(BytesIO(urlopen(url).read()))
		except (HTTPError, URLError):
			sleep(1)
		except (OSError, UnboundLocalError):
			# log_error('OSError while retrieving image')
			return 0, None
	# log_warn('Quitting loop while retrieving image')
	return 0, None


# @jit(fastmath=True)
def __fry(
		img, number_of_cycles, number_of_emojis,
		bulge_probability, laser, vitamin_b
):
	# log_info('__fry starting')
	# if laser:
	# log_info('Finding eye coordinates')
	# eye_coords = __find_eyes(img)
	# log_info('Eye coordinates found')
	# img = __add_lasers(img, eye_coords)
	# log_info('Laser eyes added')

	# if vitamin_b:
	# log_info('Finding char coordinates')
	# coords = __find_chars(img)
	# log_info('Char coordinates found')
	# img = __add_b(img, coords, number_of_emojis / 20)
	# log_info('"B"s added')

	# log_info('Starting emoji adding')
	img = __add_emojis(img, number_of_cycles * number_of_emojis)
	# log_info('emojis added')

	# log_info('Starting bulge adding')
	w, h = img.width - 1, img.height - 1
	for _ in range(number_of_cycles):
		if random(1)[0] > bulge_probability:
			continue

		# __add_bulge(img, coords, radius, flatness, h, ior)
		img = __add_bulge(
			img,
			array([
				int(w * random(1)),
				int(h * random(1))
			]),
			int(((img.width + img.height) / 10) * (random(1)[0] + 1)),
			1 + random(3)[0],
			6 + random(2)[0],
			1.2 + random(2)[0]
		)
	# log_info('Bulges added, __fry completed')
	return img


# @jit(fastmath=True)
def __posterize(img, p):
	return ImageOps.posterize(
		img,
		4 if p == 4 else 6 if p == 1 else 5
	)


# @jit(fastmath=True)
def __sharpen(img, p):
	return ImageEnhance.Sharpness(img).enhance(
		(img.width * img.height * p / 3200) ** 0.4
	)


# @jit(fastmath=True)
def __increase_contrast(img, p):
	return ImageEnhance.Contrast(img).enhance(normal(1.8, 0.8) * p / 2)


# @jit(fastmath=True)
def __colorize(img, p):
	return ImageEnhance.Color(img).enhance(normal(2.5, 1) * p / 2)


# @jit(fastmath=True)
def __add_lasers(img, coords):
	# log_info('__add_lasers started')
	if not coords:
		return img
	tmp = img.copy()

	laser = Image.open(f'{bin_path}/Resources/Frying/laser1.png')
	for coord in coords:
		tmp.paste(
			laser, (
				int(coord[0] - laser.size[0] / 2),
				int(coord[1] - laser.size[1] / 2)
			), laser
		)

	# log_info('__add_lasers completed')
	return tmp


# @jit(fastmath=True)
def __add_b(img, coords, c):
	# log_info('__add_b started')
	tmp = img.copy()

	b = Image.open(f'{bin_path}/Resources/Frying/B.png')
	for coord in coords:
		if random(1)[0] < c:
			resized = b.copy()
			resized.thumbnail((coord[2], coord[3]), Image.ANTIALIAS)
			tmp.paste(resized, (int(coord[0]), int(coord[1])), resized)

	# log_info('__add_b completed')
	return tmp


# @jit(fastmath=True)
def __add_emojis(img, m):
	# log_info('__add_emojis started')
	emojis = ['100', 'OK', 'laugh', 'fire', 'think']
	tmp = img.copy()

	for i in emojis:
		emoji = Image.open(f'{bin_path}/Resources/Frying/%s.png' % i)
		for _ in range(int(random(1)[0] * m)):
			coord = random(2) * array([img.width, img.height])
			size = int((img.width / 10) * (random(1)[0] + 1)) + 1
			theta = random(1)[0] * 360

			resized = emoji.copy()
			resized = resized.rotate(theta)
			resized.thumbnail((size, size), Image.ANTIALIAS)
			tmp.paste(resized, (int(coord[0]), int(coord[1])), resized)

	# log_info('__add_emojis completed')
	return tmp


# @jit(fastmath=True)
def __add_bulge(img: Image.Image, coords, radius, flatness, h, ior):
	"""
	Creates a bulge like distortion to the image

	:param img: The Image
	:type img: PIL.Image
	:param coords: Numpy Array with Coordinates of Centre of Bulge
	:type coords: numpy.array
	:param radius: Radius of Bulge
	:type radius: int
	:param flatness: Flatness: 1 for Spherical, > 1 for Flat.
	:type flatness: int
	:param h: Height of Bulge
	:type h: int
	:param ior: Index of Refraction of Bulge Material
	:type ior: float
	:return: The Bulged Image
	:rtype: PIL.Image
	"""
	# log_info('__add_bulge started')

	width = img.width
	height = img.height
	# noinspection PyTypeChecker
	img_data = array(img)

	if width * height > 9000000:
		return img

	# Determine range of pixels to be checked (square enclosing bulge)
	x_min = int(coords[0] - radius)
	if x_min < 0:
		x_min = 0
	x_max = int(coords[0] + radius)
	if x_max > width:
		x_max = width
	y_min = int(coords[1] - radius)
	if y_min < 0:
		y_min = 0
	y_max = int(coords[1] + radius)
	if y_max > height:
		y_max = height

	# Make sure that bounds are int and not np array
	if isinstance(x_min, type(array([]))):
		x_min = x_min[0]
	if isinstance(x_max, type(array([]))):
		x_max = x_max[0]
	if isinstance(y_min, type(array([]))):
		y_min = y_min[0]
	if isinstance(y_max, type(array([]))):
		y_max = y_max[0]

	# Array for holding bulged image
	bulged = copy(img_data)
	for y in range(y_min, y_max):
		for x in range(x_min, x_max):
			ray = array([x, y])

			# Find the magnitude of displacement
			# in the xy plane between the ray and focus
			s = sqrt(sum(square(ray - coords)))

			# If the ray is in the centre of the bulge or beyond the radius,
			# it doesn't need to be modified
			if not 0 < s < radius:
				bulged[y][x] = img_data[y][x]
				continue

			# Slope of the bulge relative to xy plane at (x, y) of the ray
			m = -s / (flatness * sqrt(radius ** 2 - s ** 2))

			# Find the angle between the ray and the normal of the bulge
			theta = pi / 2 + arctan(1 / m)

			# Find the magnitude of the angle between
			# the XY plane and refracted ray using Snell's Law

			# s >= 0 -> m <= 0 -> arctan(-1/m) > 0,
			# but ray is below xy plane so we want a negative angle
			# arctan(-1/m) is therefore negated
			phi = abs(arctan(1 / m) - arcsin(sin(theta) / ior))

			# Find length the ray travels in xy plane before hitting z=0
			k = (h + (sqrt(radius ** 2 - s ** 2) / flatness)) / sin(phi)

			# Find intersection point
			normalized = (coords - ray) / sqrt(sum(square(coords - ray)))
			intersect = ray + normalized * k

			# Assign pixel the colour of pixel at intersection
			if 0 < intersect[0] < width - 1 and 0 < intersect[1] < height - 1:
				bulged[y][x] = img_data[int(intersect[1])][int(intersect[0])]
			else:
				# No light reaching the pixel
				bulged[y][x] = [0, 0, 0]
	img = Image.fromarray(bulged)

	# log_info('__add_bulge completed')
	return img


# @run_async
def __upload_to_imgur(path, caption):
	# log_info('__upload started')
	if not isfile(path):
		# log_warn('File to be uploaded not found')
		return

	# TODO: Convert to GIF and upload.
	if path[-3:] == 'mp4':
		remove(path)
		# log_warn('Skipping mp4 upload')
		return

	# log_info('Authorizing imgur client')
	im = Imgur(
		environ.get('IMGUR_CLIENT_ID'),
		environ.get('IMGUR_CLIENT_KEY'),
		environ.get('IMGUR_ACCESS_TOKEN'),
		environ.get('IMGUR_REFRESH_TOKEN')
	)
	for _ in range(5):
		# noinspection PyBroadException
		try:
			im.upload_image(
				path=abspath(path),
				title=caption,
				album=environ.get('IMGUR_ALBUM')
			)
		except Exception:
			# log_warn('Upload failed, refreshing token')
			im.refresh_access_token()
			sleep(10)
			continue
	# log_info('Deleting file')
	remove(path)
	return


def __get_caption(name, number_of_cycles, args):
	caption = 'Requested by %s, %d Cycle(s) of%sfrying. %s, %s' % (
		name,
		number_of_cycles,
		' Deep ' if args['deep'] else ' Shallow ' if args['shallow'] else ' ',
		(
			'High-fat' if args['high-fat']
			else 'Low-fat' if args['low-fat']
			else 'No-fat' if args['no-fat']
			else 'Normal-fat'
		),
		(
			'Heavy' if args['heavy']
			else 'Light' if args['light']
			else 'Classic'
		)
	)
	if args['chilli']:
		if args['vitamin-b']:
			return f'{caption}, with extra Chilli and added Vitamin-B.'

		return f'{caption}, with extra Chilli.'

	if args['vitamin-b']:
		return f'{caption}, with added Vitamin-B.'
	return f'{caption}.'
