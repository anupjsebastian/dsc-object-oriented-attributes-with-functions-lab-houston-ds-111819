class School:
    def __init__(self, name, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, name, grade_level):
        # if self.roster[grade_level].append(name) if self.roster.get(grade_level) != None else (self.roster[grade_level] = [name])
        if grade_level in list(self.roster.keys()):
            self.roster[grade_level].append(name)
        else:
            self.roster[grade_level] = [name]
            
    def grade(self,grade):
            return self.roster[grade]
    
    def sort_roster(self):
        sorted_dict = self.roster
        for key in sorted_dict:
            sorted_dict[key].sort()
        return sorted_dict