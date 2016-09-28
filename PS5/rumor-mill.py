#/usr/env python
import copy

cost_list = {}

def bfs(students, rumor_starter, sorted_names):
    global cost_list
    if len(cost_list[rumor_starter]) < 1:
        names_copy = copy.deepcopy(sorted_names)
        answer = {}
        level = 0
        queue = [[rumor_starter, level]]
        visited = set()
        while len(queue) > 0:
            n = queue.pop(0)
            v = n[0]
            current_level = n[1]
            level = current_level

            if v not in visited:

                if current_level not in answer:
                    answer[current_level] = [v]
                else:
                    answer[current_level].append(v)

                visited.add(v)
                names_copy.remove(v)
                for u in students[v]:
                    if u not in visited:
                        queue.append([u, current_level+1])

        # for name in names_copy:
        #     answer.append(name)
        level += 1
        answer[level] = names_copy
        cost_list[rumor_starter] = []

        for l in answer.keys():
            answer[l].sort()
            cost_list[rumor_starter].extend(answer[l])
        #cost_list[rumor_starter] = answer

    print(*cost_list[rumor_starter])


def read_in():
    student_names = []
    students = {}
    number_of_students = int(input())
    n = 0
    while n < number_of_students:
        student_name = input()
        student_names.append(student_name)
        students[student_name] = []
        cost_list[student_name] = []
        n += 1

    number_of_friendships = int(input())
    h = 0
    while h < number_of_friendships:
        line = input()
        s = line.split()
        friend_name1 = s[0]
        friend_name2 = s[1]
        students[friend_name1].append(friend_name2)
        students[friend_name2].append(friend_name1)
        h += 1

    student_names.sort()
    for s in students.keys():
        students[s].sort()

    gossipers = []
    number_of_reports = int(input())
    t = 0
    while t < number_of_reports:
        gossiper = input()
        gossipers.append(gossiper)
        t += 1

    for gossiper in gossipers:
        bfs(students, gossiper, student_names)


if __name__ == "__main__":
    read_in()
