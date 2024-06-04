
import datetime
import math

def define_dot_first(x:int, y:int) -> str: ## Task 1
    x_line:int = 4
    if x > x_line:
        return 'II'
    else:
        return 'I'
        
def define_dot_second(x: int, y: int) -> str: ## Task 2
    y_line:int = 4
    if y > y_line:
        return 'I'
    else:
        return 'II'
    
def define_y_at_func(func: str, x: float) -> float: ## Task 3
    y: float = 0
    #???????????? Принимаем функцию и по функции получаем значение y при значении x ? 
    return y 

def define_bigger_and_smaller(first: float, second: float) -> str: ## Task 4, 5
    if first != second:
        if first > second:
            return f'{first} максимальное, {second} минимальное'
        else:
            return f'{second} максимальное, а {first} минимальное'
    else:
        return 'Числа равны'

def define_human_age(year_born: int, month_born: int) -> int: ## Task 6
    date = datetime.datetime.now()
    now_year = date.year
    now_month = date.month
    if year_born < now_year and month_born < 12:
        years = now_year - year_born - 1
        if now_month > month_born:
            years += 1  
    else:
        return 0
    
    return years

def output_task_seven(x: float) -> float: ## Task 7
    if x > 0:
        return math.sin(x**2) ** 2
    else:
        return 1+2*(math.sin(x)**2)
    

