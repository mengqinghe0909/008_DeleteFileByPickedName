import os


def main():
	delete_files = []
	file_names = os.listdir()
	for file_name in file_names:
		if file_name.find('restart_flow') != -1:
			if file_name.find('99.csv') != -1:
				pass
			elif file_name.find('00.csv') != -1:
				pass
			elif file_name.find('01.csv') != -1:
				pass
			elif file_name.find('02.csv') != -1:
				pass
			else:
				delete_files.append(file_name)
	for file in delete_files:
		os.remove(file)


if __name__ == '__main__':
    main()