def reverse(stacklist, reversestack=None):
    if not reversestack:
        reversestack = []
    reversestack.append(stacklist.pop())
    if stacklist:
        reverse(stacklist, reversestack)
        return reversestack

stack = [5, 4, 3, 2, 1]
print("The given stack is",stack)
stack = reverse(stack)
print("The reverse stack is",stack)