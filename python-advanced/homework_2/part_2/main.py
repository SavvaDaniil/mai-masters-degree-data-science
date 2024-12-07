from typing import List, Any

class NoDataBufferMemoryException(Exception):
    def __init__(self):
        super().__init__("Буфер памяти чист")

class OutOfMemoryBufferMemoryException(Exception):
    def __init__(self):
        super().__init__("Буфер памяти переполнен, очистка буфера")

class BufferMemory:
    """Класс, представляющий собою буфер данных"""

    def __init__(self):
        self.memory_list: List[Any] = []

    def add_data(self, data: Any) -> None:
        """Добавление данных в буфер"""
        if len(self.memory_list) >= 5:
            self.memory_list.clear()
            raise OutOfMemoryBufferMemoryException()
        self.memory_list.append(data)

    def get_data(self) -> List[Any]:
        """Получение последних данных из буфера"""
        if len(self.memory_list) == 0:
            raise NoDataBufferMemoryException()
        answer_list: List[Any] = self.memory_list.copy()
        self.memory_list.clear()
        return answer_list

if __name__ == '__main__':
    bufferMemory: BufferMemory = BufferMemory()
    try:
        bufferMemory.get_data()
    except NoDataBufferMemoryException as e:
        print(e)

    bufferMemory.add_data(data=123)
    bufferMemory.add_data(data="Строка")
    print(''.join(str(bufferMemory.get_data())))

    try:
        bufferMemory.get_data()
    except NoDataBufferMemoryException as e:
        print(e)
    
    try:
        for i in range(6):
            bufferMemory.add_data(data=123)
    except OutOfMemoryBufferMemoryException as e:
        print(e)
    
    try:
        bufferMemory.get_data()
    except NoDataBufferMemoryException as e:
        print(e)



    

