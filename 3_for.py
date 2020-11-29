"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [
    {'school_class': '6A', 'scores': [3,4,4,5,2]},
    {'school_class': '7A', 'scores': [3,5,4,3,2]},
    {'school_class': '8A', 'scores': [5,4,4,5,3]},
    {'school_class': '9A', 'scores': [4,5,5,5,3]}
    ]
    school_avg = 0
    for score in school_scores:
        scores_sum = sum(score['scores'])
        score_avg = scores_sum/len(score['scores'])
        school_avg += score_avg/len(school_scores)
        class_name = score['school_class']
        print(f'Средняя оценка учеников класса {class_name} : {score_avg} балла')
    print(f'Средняя оценка учеников всей школы : {school_avg} балла')
    
if __name__ == "__main__":
    main()
