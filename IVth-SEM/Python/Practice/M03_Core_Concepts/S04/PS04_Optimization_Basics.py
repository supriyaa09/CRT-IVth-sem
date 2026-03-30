'''check for duplicates in a list

input: [1,2,3,4,5,1]
output: True

input: [1,2,3,4,5]
output: False
'''

def check_duplicates(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i]==li[j]:
                return True
    return False

li=[1,2,3,4,5,1]
print(check_duplicates(li)) #-> time complexity: O(n^2)

#make it from O(n^2) to O(n)
def check_duplicates(li):
    d=set()
    for i in li:
        if i in d:
            return True
        d.add(i)
    return False
li=[1,2,3,4,5,1]
print(check_duplicates(li)) #-> time complexity: O(n)