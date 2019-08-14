import requests

token='ccdcff3ef1c44eb0029e1bef96d33da6ebc3f951824137e9a5222dab6e08ecfce97da0ff76fd539460ec6'

print('Make by Lonely Dark')
print('1. Delete friends if human deactivated')
print('2. Delete from conversation, if human deactivated')
choose=input('Your choose: ')

if choose=='1':
	people_all=requests.get('https://api.vk.com/method/friends.get',params={'access_token': token, 'fields': 'deactivated', 'v': '5.101'}).json()
	for i in people_all['response']['items']:
		if 'deactivated' in i:
			print('Found. Human name is: ' + str(i['first_name']) + ' ' + str(i['last_name']))
			print('1. Delete human')
			print('2. Not delete human')
			delete=input('Delete this human?: ')
			if delete=='1':
				requests.get('https://api.vk.com/method/friends.delete',params={'access_token': token, 'v': '5.101'}).json()
				print('Process done.')
			if delete=='2':
				print('Pass this human')


if choose=='2':
	conversation_id=int(input('Please type conversation_id here: '))
	get_conversation_peoples=requests.get('https://api.vk.com/method/messages.getConversationMembers',params={'access_token': token, 'peer_id': 2000000000+conversation_id, 'fields': 'deactivated', 'v': '5.101'}).json()
	for i in get_conversation_peoples['response']['profiles']:
		if 'deactivated' in i:
			print('Found. Human name is: ' + str(i['first_name'] + ' ' + str(i['last_name'])))
			print('1. Delete human')
			print('2. Not delete human')
			delete=input()
			if delete=='1':
				requests.get('https://api.vk.com/method/messages.removeChatUser',params={'access_token': token, 'chat_id': conversation_id, 'user_id': i['id'], 'v': '5.101'}).json()
				print('Process done.')
			if delete=='2':
				print('Pass this human')