class ComputerAssembly:
    
    # Статический атрибут - список комплектующих ПК
    computer_parts = ['процессор', 'материнская плата', 'видеокарта', 'оперативная память', 'накопитель', 'блок питания', 'корпус']
    
    def __init__(self):
        # Динамический атрибут - текущий набор комплектующих ПК
        self.current_parts = []
    
    # Статический метод - вывод списка комплектующих ПК
    @staticmethod
    def show_parts():
        print("Комплектующие ПК: ", ', '.join(ComputerAssembly.computer_parts))
    
    # Динамический метод - добавление комплектующей в текущий набор
    def add_part(self, part):
        if part not in self.current_parts:
            self.current_parts.append(part)
            print(f"Комплектующая '{part}' успешно добавлена")
        else:
            print(f"Комплектующая '{part}' уже есть в наборе")
    
    # Динамический метод - удаление комплектующей из текущего набора
    def remove_part(self, part):
        if part in self.current_parts:
            self.current_parts.remove(part)
            print(f"Комплектующая '{part}' успешно удалена")
        else:
            print(f"Комплектующей '{part}' нет в наборе")
    
    # Динамический метод - вывод текущего набора комплектующих ПК
    def show_current_parts(self):
        if self.current_parts:
            print("Текущий набор комплектующих ПК: ", ', '.join(self.current_parts))
        else:
            print("Текущий набор комплектующих ПК пуст")

# Создаем объект класса
my_pc = ComputerAssembly()

# Выводим список всех комплектующих ПК
ComputerAssembly.show_parts()

# Добавляем комплектующие в набор
my_pc.add_part('процессор')
my_pc.add_part('материнская плата')
my_pc.add_part('видеокарта')
my_pc.add_part('накопитель')

# Выводим текущий набор комплектующих ПК
my_pc.show_current_parts()

# Пытаемся добавить уже существующую в наборе комплектующую
my_pc.add_part('процессор')

# Удаляем комплектующие из набора
my_pc.remove_part('материнская плата')
my_pc.remove_part('SSD')

# Выводим обновленный текущий набор комплектующих ПК
my_pc.show_current_parts()