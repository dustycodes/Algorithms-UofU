#/usr/env python


class Node:
    def __init__(self, name):
        self.name = name
        self.toll = 1
        self.children = []
        self.cost_list = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def bfs(self, list_of_names):
        if len(self.cost_list) != 0:
            print(*self.cost_list)
        else:
            self.cost_list.append(self.name)
            visited = {}
            for name in list_of_names:
                visited[name] = False

            visited[self.name] = True

            for child in self.children:
                visited[child.name] = True
                self.cost_list.append(child.name)

            #sublist = []
            for child in self.children:
                for sub_child in child.children:
                    if visited[sub_child.name] is False:
                        visited[sub_child.name] = True
                        #sublist.append(sub_child.name)
                        self.cost_list.append(sub_child.name)

            #sublist.sort()
            #for name in sublist:
            #    self.cost_list.append(name)

            for name in list_of_names:
                if visited[name] is False:
                    self.cost_list.append(name)
            print(*self.cost_list)


def read_in():
    student_names = []
    students = {}
    number_of_students = int(input())
    n = 0
    while n < number_of_students:
        student_name = input()
        student_names.append(student_name)
        students[student_name] = Node(student_name)
        n += 1

    number_of_friendships = int(input())
    h = 0
    while h < number_of_friendships:
        line = input()
        s = line.split()
        friend_name1 = s[0]
        friend_name2 = s[1]
        students[friend_name1].add_child(students[friend_name2])
        students[friend_name2].add_child(students[friend_name1])
        h += 1

    for node in students.keys():
        students[node].children.sort(key=lambda x: x.name)
    student_names.sort()

    gossipers = []
    number_of_reports = int(input())
    t = 0
    while t < number_of_reports:
        gossiper = input()
        gossipers.append(students[gossiper])
        t += 1

    for gossiper in gossipers:
        gossiper.bfs(student_names)

if __name__ == "__main__":
    read_in()
