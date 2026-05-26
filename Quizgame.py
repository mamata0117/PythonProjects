print('Welcome to the Quiz Game!')

questions = [
    {
        'question': 'How is comment done in python?',
        'options': ['//', '#', '/* */', '--'],
        'answer': '#'
    },

    {
        'question': 'Python was created by?',
        'options': ['Dennis Ritchie', 'Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
        'answer': 'Guido van Rossum'
    },
    {
        'question': 'Which of the following is not a valid variable name in Python?',
        'options': ['py_learn', '2nd_variable', '_variable', 'variable-name'],
        'answer': '2nd_variable'
    },
    {
        'question': 'How is square root calculated in python?',
        'options': ['sqrt()', '**0.5', 'math.sqrt()', 'All of the above'],
        'answer': 'All of the above'
        # eg: sqrt(8) or 8**0.5 or math.sqrt(8) will all give the same result.
    },
    {
        'question': 'What is the output of the following code: print(2 ** 3)?',
        'options': ['5', '6', '8', '9'],
        'answer': '8'
    },
    {
        'question': 'Which of the following is a mutable data type in Python?',
        'options': ['tuple', 'list', 'string', 'int'],
        'answer': 'list'
    },
    {
        'question': 'Which of the following is not a valid data type in Python?',
        'options': ['int', 'float', 'char', 'str'],
        'answer': 'char'
    },
    {'question':'Which is not a valid loop in python?',
     'options':['for loop','while loop','do-while loop','None of the above'],
     'answer':'do-while loop'       
    },
    {
        'question': 'How is integer division performed in Python?',
        'options': ['/', '//', '%', '**'],
        'answer': '//'
    },
    {
        'question': 'How is float division performed in Python?',
        'options': ['/', '//', '%', '**'],
        'answer': '/'
    },
    {
        'question': 'What is the output of the following code: print(5 % 2)?',
        'options': ['0', '1', '2', 'None of the above'],
        'answer': '1'
    },
    {
        'question': 'What is the output of the following code: print(10 // 3)?',
        'options': ['3', '3.33', '4', 'None of the above'],
        'answer': '3'
    },
    {
        'question': 'What is the use of enumerate() function in python?',
        'options': ['To get the index and value of a list', 'To get the length of a list', 'To sort a list', 'None of the above'],
        'answer': 'To get the index and value of a list'
    }
   ]
score = 0
for i in enumerate(questions):
    print(i[1]['question'])

    for number, option in enumerate(i[1]['options'], start=1):
        print(f"{number}. {option}")

    answer = int(input('Enter your answer: '))

    selected_option = i[1]['options'][answer - 1]

    if selected_option == i[1]['answer']:
        print('Correct!')
        score += 1
    else:
        print('Wrong! The correct answer is', i[1]['answer'])

print('Your final score is:', score)