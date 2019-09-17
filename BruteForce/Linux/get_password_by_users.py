import re
import crypt
def get_users(file_ptr):
	data_lines = file_ptr.readlines()
	user_salts_results = []
	for data_line in data_lines:
		if data_line.find('$') > 2:
			user = data_line.split(':')[0]
			salt = re.findall('[$].+[$]',data_line)[0]
			res = data_line.split(':')[1]
			user_salts_results.append((user,salt,res))
	return user_salts_results

def UI(user_salts_results):
	users = []
	for data in user_salts_results:
		users.append(data[0])
	print('This file find those users.please choose one to crack:')
	for i in range(len(users)):
		print('%d:%s' %(i,users[i]))
	target = int(input('please input target number before user_name:'))
	print('you choose user:%s' %(users[target]))
	return user_salts_results[target]

def main():
	file_ptr = open('./HackedFiles/shadow','r')
	user_salts_results = get_users(file_ptr)
	targets_user = UI(user_salts_results)
main()
