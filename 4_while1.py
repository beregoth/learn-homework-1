"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    def hello_user():
      while True:
          user_say = input('Как дела?    ')
          if user_say == 'Хорошо':
              print('И у меня хорошо!')
              break
    hello_user()

    
if __name__ == "__main__":
    hello_user()
