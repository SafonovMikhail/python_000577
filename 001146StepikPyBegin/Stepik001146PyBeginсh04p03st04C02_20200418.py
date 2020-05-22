a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a != b and b == c:
    print("Равнобедренный")
elif b != c and c == a:
    print("Равнобедренный")
elif c != a and b == a:
    print("Равнобедренный")
else:
    print("Разносторонний")