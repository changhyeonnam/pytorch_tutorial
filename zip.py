
# https://docs.python.org/3.3/library/functions.html
'''
zip(*iterables)
:   Make an iterator that aggregates(종합하다, 모두 합치다) elements from each other for iterables
    return an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
    The iterator stops when the shortest input iterable is exhausted.
    With a single iterable argument, it returns an iterator of 1-tuples.
    With no arguments, it returns an empty iterator. Equivalent to:

next(iterator[, default])
:   Retrieve the next item from the iterator by calling its __next__() method.
    If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

object()
:   Return a new featureless object. object is a base for all classes.
    It has the methods that are common to all instances of Python classes. This function does not accept any arguments.

iter(object[, sentinel])
:   Return an iterator object.
    The first argument is interpreted very differently depending on the presence of the second argument.
    Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method),
    or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0).
    If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given,
    then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method;
    if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.
'''
def zip(*iterables):
    # zip('ABCD','xy') -> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators: # stop iteration 하기전까지
        result = []
        for it in iterators:
            elem = next(it,sentinel) # sentinel은 iterator가 끝났을때.
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)





'''
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.
*iterable : iterable한 자료형 여러개를 입력할 수 있다는 의미
'''
l1 = list(zip([1, 2, 3], [4, 5, 6]))
print(l1)
l2 = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(l2)
l3 = list(zip("abc", "def"))
print(l3)


# 두개의 list를 하나의 연관된 리스트로 만든다.
Number = [1,2,3,4]
Name = ['hong','gil','dong','nim']
Number_Name = list(zip(Number,Name))
print(Number_Name)

# 하나의 연관된 List가 아닌 하나의 딕셔너리로 만든다고 하자.
Number = [1,2,3,4]
Name = ['hong','gil','dong','nim']
dic = {}

# for i in range(len(Number)):
#     dic[Number[i]] = Name[i]
# print(dic)

for number, name in zip(Number,Name):
    dic[number] = name
print(dic)
