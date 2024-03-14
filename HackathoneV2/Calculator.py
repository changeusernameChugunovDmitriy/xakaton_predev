import re

class Caalculator():
    def __init__(self) -> None:
        
        pass

    def add(self, x1, x2) -> float:
        """
        Функционал сложения полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        result = str((x1+x2))
        if '.' in result:
            result = result.split('.')
            res = list(result[1]) 
            i = 0
            while i < len(res)-2:
                if res[i] == '0' and res[i+1] == '0' and res[i+2] == '0':                   
                    res2 = ''.join(res[:i])
                    result = result[0]+'.'+res2
                    return float(result)
                else:
                    i+=1
        result = (x1+x2)
        return result
    
    def subtract(self, x1, x2) -> float:
        """
        Функционал вычитания полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        result = str((x1-x2))
        if '.' in result:
            result = result.split('.')
            res = list(result[1]) 
            i = 0
            while i < len(res)-2:
                if res[i] == '0' and res[i+1] == '0' and res[i+2] == '0':                   
                    res2 = ''.join(res[:i])
                    result = result[0]+'.'+res2
                    return float(result)
                else:
                    i+=1
        result = (x1-x2)
        return result
    
    def multiply(self, x1, x2) -> float:
        """
        Функционал умножения полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        result = str((x1*x2))
        if '.' in result:
            result = result.split('.')
            res = list(result[1]) 
            i = 0
            while i < len(res)-2:
                if res[i] == '0' and res[i+1] == '0' and res[i+2] == '0':                   
                    res2 = ''.join(res[:i])
                    result = result[0]+'.'+res2
                    return float(result)
                else:
                    i+=1
        result = (x1*x2)
        return result

    def divide(self, x1, x2) -> float:
        """
        Функционал деления полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        if x2 == 0:
            return "Делить на ноль нельзя!"
        result = str((x1/x2))
        if '.' in result:
            result = result.split('.')
            res = list(result[1]) 
            i = 0
            while i < len(res)-2:
                if res[i] == '0' and res[i+1] == '0' and res[i+2] == '0':                   
                    res2 = ''.join(res[:i])
                    result = result[0]+'.'+res2
                    return float(result)
                else:
                    i+=1
        result = (x1/x2)
        return result
    

    def readline(self, line) -> list:
        print("===Reading line started...===")
        splited_line = {"a": "???", "b": "???", "f": "???", "r": "???"}
        # Удаляем лишние пробелы чтобы код работал
        line = line.replace(' ','')
        # pattern для разделения целый чисел и чисел с плавающей точкой
        # у нас ^ для начала а $ для конца чтобы лишнего не добавлялось
        pattern = r"^(\d+(\.\d+)?)([\+\-\*/])(\d+(\.\d+)?)$"
        # Ищем совпадения с pattern
        match = re.search(pattern, str(line))
        # try и except для отлавливания ошибок
        if match:
            try:
                # Извлекаем числа и знак операции
                a = float(match.group(1))
                f = match.group(3)
                b = float(match.group(4))
                
                # Обновляем значения в словаре
                splited_line["a"] = a
                splited_line["b"] = b
                splited_line["f"] = f
            except:
                print("Введите корректные числа!")
        else:
            print("Неверный формат строки!")
            
        print("===Reading line finished...===")
        print(splited_line["a"], " ", splited_line["f"], " ", splited_line["b"], " = ", splited_line["r"])
        return splited_line

    
