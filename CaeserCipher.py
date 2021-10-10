alph = 'abcdefghijklmnopqrstuvwxyz'
def undo_code(message, offset):
	in_words = message.split(' ')
	lst = []
	new = ''
	for bit in in_words:
		for char in bit:
			if char in alph and (alph.find(char) + offset) <= len(alph) - 1:
				new = new + alph[alph.find(char)+offset]
			elif char in alph and (alph.find(char) + offset) > len(alph) - 1:
				new = new + alph[((alph.find(char)+offset) - len(alph)) + 0]
			else:
				new = new + char
		lst.append(new)
		new = ''
	return ' '.join(lst)
def create_code(message, offset):
	words = message.split(' ')
	lst = []
	new = ''
	for bit in words:
		for char in bit:
			if char in alph:
				new = new + alph[alph.find(char) - offset]
			else:
				new = new + char
		lst.append(new)
		new = ''
	return ' '.join(lst)
def find_offset(message):
	in_words = message.split(' ')
	lst = []
	lst2 = []
	new = ''
	offset = 0
	for i in range(0, 25):
		offset += 1
		for bit in in_words:
			for char in bit:
				if char in alph and (alph.find(char) + offset) <= len(alph) - 1:
					new = new + alph[alph.find(char)+offset]
				elif char in alph and (alph.find(char) + offset) > len(alph) - 1:
					new = new + alph[((alph.find(char)+offset) - len(alph)) + 0]
				else:
					new = new + char
			lst.append(new + ' ' + str(offset))
			new = ''
	lst2.append(' '.join(lst))

	
	return lst2

def undo_code_with_keyword(message, keyword):
	key_list = []
	char_index = []
	words_indexs = []
	char2_index = []
	shifted_index = []
	solved_index = []
	solved_list = []
	final_list = []
	r = 0
	for el in keyword:
		key_list.append(alph.find(el))
	for word in message.split(' '):
		for el in word:
			if el in alph:
				char_index.append(alph.find(el))
			else:
				char_index.append(el)
		words_indexs.append(char_index)
		char_index = []
	key_list = 200*key_list
	for i in words_indexs:
		for el in i:
			if isinstance(el, int):
				char2_index.append(el - key_list[r])
				r+=1
			else:
				char2_index.append(el)
				
		shifted_index.append(char2_index)
		char2_index = []
	for lst in shifted_index:
		for i in lst:
			if isinstance(i, int):
				solved_index.append(alph[i])
			elif i == 0:
				solved_index.append(alph[i])
			else:
				solved_index.append(i)
		solved_list.append(solved_index)
		solved_index = []
	for i in solved_list:
		final_list.append(''.join(i))
	return ' '.join(final_list)

print(undo_code_with_keyword("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", 'friends'))

def create_code_with_keyword(message, keyword):
	key_list = []
	char_index = []
	words_indexs = []
	char2_index = []
	shifted_index = []
	solved_index = []
	solved_list = []
	final_list = []
	r = 0
	for el in keyword:
		key_list.append(alph.find(el))
	for word in message.split(' '):
		for el in word:
			if el in alph:
				char_index.append(alph.find(el))
			else:
				char_index.append(el)
		words_indexs.append(char_index)
		char_index = []
	key_list = 200*key_list
	for i in words_indexs:
		for el in i:
			if isinstance(el, int) and el + key_list[r] <= len(alph) - 1:
				char2_index.append(el + key_list[r])
				r+=1
			elif isinstance(el, int) and el + key_list[r] > len(alph) - 1:
				char2_index.append(((el + key_list[r]) - (len(alph))) + 0)
				r+=1
			else:
				char2_index.append(el)
				
		shifted_index.append(char2_index)
		char2_index = []
	for lst in shifted_index:
		for i in lst:
			if isinstance(i, int):
				solved_index.append(alph[i])
			elif i == 0:
				solved_index.append(alph[i])
			else:
				solved_index.append(i)
		solved_list.append(solved_index)
		solved_index = []
	for i in solved_list:
		final_list.append(''.join(i))
	return ' '.join(final_list)
