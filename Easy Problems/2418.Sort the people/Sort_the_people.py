class Solution(object):
    def sortPeople(self, names, heights):
        people = list(zip(names, heights))
        people.sort(key=lambda x: x[1], reverse=True)
        sorted_names = [person[0] for person in people]
        
        return sorted_names