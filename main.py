import requests
import misc
import python_client_single as loc

token = misc.token
#https://api.telegram.org/bot741100901:AAGr4tmNwLK3ruNeqqaalVT6P5cjk9MGKFY/sendMessage?chat_id=62571377&text=hi

URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def  get_message():
	data = get_updates()

	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
	message = {'chat_id': chat_id,
				'text': message_text}
	return message


def send_message(chat_id, text='wait'):
	url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)


def main():
	#d = get_updates()
	
		answer = get_message()
		chat_id = answer['chat_id']
		text = answer['text']
		#print(text)
		send_message(chat_id, loc.get_loc(text))

		#if 'da' in text:
		#	send_message(chat_id, loc.get_loc(text))







if __name__ == '__main__':
	main()