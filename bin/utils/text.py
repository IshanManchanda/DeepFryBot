# Help Responses
commands = '''
*Basic Commands*
1. Hmmm
2. Boom son
3. Just do it
4. E
5. Hello there
6. I don't think so
7. Wut / Wat / Dude what / What even / What the
8. Ironic
9. F / RIP
10. ???

*Advanced Commands*

1. ABC, not XYZ
	Generates a meme using either the Robbie Rotten, Babushka, or Drake
	template in which ABC is chosen over XYZ.

2. Alt:
	Converts text that follows the colon to aLt CaSe.
	Deletes the trigger message if given admin rights.

3. Vapourize:
	Converts text that follows the colon to Vapourwave text.
	Deletes the trigger message if given admin rights.

4. 🅱️
	Replaces the first consonant group of each word with 🅱️.
	Doesn't replace those consonants which can (mostly) be pronounced after a B.

5. Alexa / Dankbot play Despacito [x]
	Sends a GIF of the Despacito music video
	along with an audio file of Despacito.
	If a number x is given, certain effects are applied to the audio.
	If not, the audio file has a 10% chance of being extremely bass boosted.

6. T: ABC B: XYZ
	Reply to an image to create a meme.
	ABC is the top-text and XYZ is the bottom-text.
	By default, the captions are converted to upper case.
	Replace T with Ts and B with Bs to keep case as it is.


Please note, DankBot needs permission to access messages to work properly.
For additional functionality, such as removing certain trigger messages
after responding, the Bot needs to be an admin on the group.
Admin rights are optional and may be toggled at your discretion.

Use */help* to print commands and */cookbook* for frying help.
'''
cookbook = '''
*Deep Fryer*
Fries images, GIFs, or videos (Experimental).
This includes increasing saturation & contrast,
and adding noise, emojis, laser eyes, and bulges.

To invoke, reply to a message containing an image, GIF, or video
using one of the following commands:

	a) Fry: 1 cycle of frying.
	b) Nuke: 3 cycles of frying.
	d) Tsar Bomba: 5 cycles of frying.

	Additional parameters (Include in the same message):

	a) Deep: High contrast and saturation increase.
	b) Shallow: Low contrast and saturation increase.

	c) High-fat: Emojis are increased.
	d) Low-fat: Emojis are reduced.
	e) No-fat: Emojis aren't added.

	f) Heavy: Extra bulges are added.
	g) Light: No bulges are added.

	h) Vitamin-B: (Experimental) Adds the B emoji on text in the image.
	i) Chilli: (Experimental) Adds laser eyes.

Also note that emojis and bulges are disabled by default for GIFs and Videos.
Use High-fat and Heavy to enable them as needed.


Use */help* to print commands and */cookbook* for frying help.
'''
changes = '''
16 Nov 2020

- Some housekeeping, general maintenance
'''

# Vaporwave Text
normal = \
	'''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890''' + \
	'''`-=~!@#$%^&*()_+[];',./{}:"|<>?'''
vapor = \
	'''ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ''' + \
	'''ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０''' + \
	'''`－＝~！＠＃＄％^＆＊（）_＋[]；＇，．／{}："|<>？'''
vaportext = {normal[x]: vapor[x] for x in range(len(normal))}
vaportext[' '] = '   '

# B-ify
bs = '🅱️bcdfgjkmnpqtvwx'
excluded = ['a', 'an', 'and', 'are', 'if', 'the']

# Misc.
chars = 'abcdefghijklmnopqrstuvwxyz'
keys = [
	'shallow', 'deep',
	'no-fat', 'low-fat', 'high-fat',
	'light', 'heavy',
	'chilli',
	'vitamin-b'
]

ironic = '''
Did you ever hear the tragedy of Darth Plagueis The Wise?
I thought not. It's not a story the Jedi would tell you.

It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith,
so powerful and so wise he could use the Force
to influence the midichlorians to create life…

He had such a knowledge of the dark side that
he could even keep the ones he cared about from dying.

The dark side of the Force is a pathway to many abilities
some consider to be unnatural. He became so powerful…

The only thing he was afraid of was losing his power,
which eventually, of course, he did.

Unfortunately, he taught his apprentice everything he knew,
then his apprentice killed him in his sleep.

Ironic. He could save others from death, but not himself.
'''.replace('\n', ' ')
