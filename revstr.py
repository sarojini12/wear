def reverse(veni):
 
    i = len(veni)
    rev = ""
    while i != 0:
        rev = rev + veni[i-1]
        i = i - 1
    return rev
 
 
print(reverse("veni"))
