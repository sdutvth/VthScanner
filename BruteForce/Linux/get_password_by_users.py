import re
import crypt
def get_users(file_ptr): # 拿到所有的用户名、盐值、加密后的值等数据
	data_lines = file_ptr.readlines()
	user_salts_results = []
	for data_line in data_lines:
		if data_line.find('$') > 2:
			user = data_line.split(':')[0]
			salt = re.findall('[$].+[$]',data_line)[0]
			res = data_line.split(':')[1]
			user_salts_results.append((user,salt,res))
	return user_salts_results

def UI(user_salts_results): # UI交互
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
	targets_user,target_salt,target_encode = UI(user_salts_results)
	fp_passwd = open('password.txt','r')
	passwords = fp_passwd.readlines()
	fp_passwd.close()
	for i in passwords:
		encoded = crypt.crypt(i[:-1],target_salt) # 注意字符串末尾是\n,要过滤掉
		if encoded == target_encode:
			print('user %s\'s password is %s' %(targets_user,i))
			break
	else:
		print('sorry,not found!')
main()
