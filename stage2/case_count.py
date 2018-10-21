def read_md():
	lines = ''
	with open('tmp.md', 'r') as f:
		lines = f.readlines()
	return lines


def is_Chinese_word(chi):
	return chi >= u'\u4e00' and chi <= u'\u9fa5'


def is_title(line):
	if len(line) < 7:
		return False;
	return line[0] == '#' 


def count_case_words_num():
	lines = read_md()
	sum_count = 0
	tmp = i = 0
	single_count = [0 for i in range(0, 7)]
	for line in lines:
		if is_title(line):
			i = int(line[6])
			single_count[i - 1] = tmp
			tmp = 0
		else:
			for ch in line:
				if is_Chinese_word(ch):
					tmp += 1

	single_count[6] = tmp
	sum_count = sum(single_count)
	print('The sum of words in case doc is : ' + str(sum_count))
	for i in range(1, 7):
		print('The words of case %d is %d'%(i, single_count[i]))


count_case_words_num()