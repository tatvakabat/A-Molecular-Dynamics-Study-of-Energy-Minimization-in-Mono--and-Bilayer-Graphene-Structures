class Classroom:
    def __init__(self, priorList=None):
        if priorList is None:
            self.currentList = []
        else:
            self.currentList = priorList

    @property
    def returnList(self):
        return self.currentList
    
    def addStudent(self, new_tuple): # Each student should be added in format (name, score) as a tuple
        if isinstance(new_tuple, tuple) and len(new_tuple) == 2:
            self.currentList.append(new_tuple)
        else:
            raise ValueError("The student parameter must be a tuple")
        
    def sortByScoreUp(self):
        return sorted(self.currentList, key=lambda student: student[1])
    
    def sortByScoreDown(self):
        return sorted(self.currentList, key=lambda student: student[1], reverse=True)
    
    def sortByName(self):
        return sorted(self.currentList, key=lambda student: student[0])
        
# Example usage:
classroom = Classroom([("Alice", 88), ("Bob", 95)])
classroom.addStudent(("Charlie", 78))
print("Original List:", classroom.returnList)
print("Sorted by Score Up:", classroom.sortByScoreUp())
print("Sorted by Score Down:", classroom.sortByScoreDown())
print("Sorted by Name:", classroom.sortByName())
