'''
	Tinkoff five_letters_game
'''
import re



#	Varaible
list_word = [] # Массив всей базы слов
period_result = [] # Переодический результат, для работы функций
result = {} # Результат для пользователя
array_procent = [] # Отвечает за процент совпадения



# 	Connect DateBase
file = open('words.txt', 'r')
for word in file:
	list_word.append(word.replace('\n', ''))



#	Function

def processing(use_letters):
	'''
		Обрабатывает результат
		Убирает слова не подходящие под use_letters
	'''
	global period_result
	global array_procent

	for item in period_result:
		procent = 0
		
		for letter_word in item:
			for use in use_letters:
				if letter_word == use:
					procent += 20

		array_procent.append(procent)

def research_words(famous_letters):
	'''
		Ищет подходящие слова в ДБ
	'''
	global list_word
	global period_result

	regex = '^' + famous_letters.replace('-', '.') + '$'
	for word in list_word:
		if re.match(regex, word):
			period_result.append(word)



#	Main Loop
while True:
	print("Введите известные,установленные буквы с их позициями.")
	print('Например, "э-ита" ')
	famous_letters = input("Известные позиции: ")

	print("\nТеперь укажите вообще какие буквы могут быть в слове.")
	print('Например, "эита" ')
	use_letters = input("Какие буквы используем: ")

	print("\nСекунду...")

	research_words(famous_letters)
	processing(use_letters)

	print("\nВозможно это:")

	for i in range(len(period_result)):
		if array_procent[i] > 50:
			result[period_result[i]] = array_procent[i]

	result_sorted = {k: result[k] for k in sorted(result,reverse=True, key=result.get)}

	lot = 0
	for item in result_sorted.items():
		if lot != 10:
			print(item[0])
			lot += 1

	print("---------------------------------------")

	period_result = []
	result_sorted = []


