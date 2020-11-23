from datetime import datetime
from inspect import currentframe, getframeinfo
from sys import stdout

from pytz import timezone


def log_debug(message):
	cf = currentframe()
	file = getframeinfo(cf).filename
	line = cf.f_back.f_lineno
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))

	stdout.write(f'DEBUG {timestamp} <line {line}, {file}>: {message}\n')


def log_info(message):
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))
	stdout.write(f'INFO {timestamp}: {message}\n')


def log_warn(message):
	cf = currentframe()
	file = getframeinfo(cf).filename
	line = cf.f_back.f_lineno
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))

	stdout.write(f'WARN {timestamp} <line {line}, {file}>: {message}\n')


def log_error(message):
	cf = currentframe()
	file = getframeinfo(cf).filename
	line = cf.f_back.f_lineno
	timestamp = datetime.now(tz=timezone('Asia/Kolkata'))

	stdout.write(f'WARN {timestamp} <line {line}, {file}>: {message}\n')


def log_command(update, command):
	log_info(f'{{{command}}} {{{generate_log_message(update)}}}')


def log_message(update):
	log_info(generate_log_message(update))


def generate_log_message(update):
	return (
		'(%s[%s]) %s[%s]: %s' % (
			update.message.chat.title,
			update.message.chat.id,
			update.message.from_user.first_name,
			update.message.from_user.id,
			update.message.text if update.message.text else '<media file>'
		)
		if update.message.chat.type != 'private' else
		'%s[%s]: %s' % (
			update.message.from_user.first_name,
			update.message.from_user.id,
			update.message.text
		)
	)
