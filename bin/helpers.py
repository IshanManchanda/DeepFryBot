from bin.fryer import fry_image
from bin.utils.text import keys


async def fry_helper(message):
	print(f'Found {len(message.attachments)} attachments')

	for attachment in message.attachments:
		print('Attachment found:', attachment.url)
		text = message.content.lower()
		n = (
			5 if 'tsar bomba' in text else
			3 if 'nuke' in text or 'nuking' in text else
			# REVIEW: Change to 0 when reply feature done
			1 if 'fry' in text else 1
		)
		args = {key: 1 if key in text else 0 for key in keys}
		await fry_image(message, attachment, n, args)
