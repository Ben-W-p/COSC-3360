def add_elem(s):
    try:
        val = int(input("Value to add: "))
        s.add(val)
    except ValueError:
        print("Please enter an integer.")

def remove_elem(s):
    try:
        val = int(input("Value to remove: "))
        if val in s:
            s.remove(val)
        else:
            print("Not present.")
    except ValueError:
        print("Please enter an integer.")

def choose_set(A, B):
    which = input("Which set? (A/B): ").strip().upper()
    return A if which == 'A' else B

def operation(A,B,op):
    print('-----------------------------------')
    match op:
        case 'add':
            set = choose_set(A,B)
            add_elem(set)
        case 'remove':
            target = choose_set(A,B)
            remove_elem(target)
        case 'perform union':
            print('union of A and B is', A.union(B))
        case 'intersection':
            print('intersection', A.intersection(B))
        case 'difference':
            print('A - B', A.difference(B))
            print('B - A', B.difference(A))
        case 'symmetric difference':
            print('Symmetric difference of A and B:', A.symmetric_difference(B))
        case 'disjoint':
            print('A and B are disjoint:', A.isdisjoint(B))
        case 'q':
            return False
        case _:
            print('Please type a valid operation')
    return True

        

nums = list(range(10, 21))
A = set(nums)
B = {n for n in nums if n % 2 == 1}
print('A:', A)
print('B:', B)
keep_going = True
while (keep_going):
    print('Pick one of the the following operations the for the two sets')
    op = input('add, remove, perform union, intersection, difference, symmetric difference, or disjoint: ')
    keep_going = operation(A,B, op)
    print('----------After Operation----------')
    print('A:', A)
    print('B:', B)
    print('-----------------------------------')
    
    
