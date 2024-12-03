class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.next = None  # Указатель на следующий узел


class List:
    def __init__(self):
        self.head = None  # Первый элемент списка
        self.size = 0  # Количество элементов в списке

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Находим последний узел
                current = current.next
            current.next = new_node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            print("Ошибка: индекс выходит за границы списка.")
            return

        new_node = Node(value)
        if index == 0:  # Вставка в начало
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):  # Доходим до нужного индекса
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def remove(self, value):
        current = self.head
        prev = None

        while current:
            if current.value == value:
                if prev is None:  # Удаляем первый элемент
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        print("ошибка!: элемент не найден.")

    def pop(self, index=None):
        if self.size == 0:
            print("ошибка!: список пуст.")
            return None

        if index is None:
            index = self.size - 1 

        if index < 0 or index >= self.size:
            print("ошибка!: индекс выходит за границы списка.")
            return None

        current = self.head
        prev = None

        for _ in range(index):
            prev = current
            current = current.next

        if prev is None: 
            self.head = current.next
        else:
            prev.next = current.next

        self.size -= 1
        return current.value

    def get(self, index):
        if index < 0 or index >= self.size:
            print("ошибка!: индекс выходит за границы списка.")
            return None

        current = self.head
        for _ in range(index):
            current = current.next

        return current.value

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)

    def show_size(self):
        return self.size


# Пример использования
if __name__ == "__main__":
    list = List()
    list.add(10)
    list.add(20)
    list.add(30)
    list.display()  

    list.insert(1, 15)
    list.display()  

    list.remove(20)
    list.display()  
    print(list.pop())  
    list.display()

    print(list.get(1))  
    print("размер списка:", list.show_size())