from django.template.defaultfilters import length

grades = [
    ("Аня", 5, 4, 5, 3),
    ("Боря", 3, 3, 4, 2),
    ("Ваня", 5, 5, 5, 4),
    ("Галя", 4, 4, 4, 4),
    ("Андрей", 2, 3, 2, 3),
]

filtered = filter(
    lambda row: sum(row[1:]) / len(row[1:]) >= 4,
    grades
)

result = map(
    lambda row: {
        "name": row[0],
        "avg": round(sum(row[1:]) / len(row[1:]), 2),
        "status": "Отлично" if sum(row[1:]) / len(row[1:]) >= 4.5 else "Хорошо"
    },
    filtered
)
print(list(result))

n = [1,2,3,2,1]
pal =lambda x: x == x[::-1]
#print(pal(n))#так чисто на тру чекнул

p = lambda x,y: (x+y)**2
print(p(4,5))
#tuple

w = lambda x:', '.join(x)
print(w(['виноград','сливы','яблоко одно']))
#list
dict = {'name': 'ахаха',
        'age' : 20}
introduce = lambda x : f'меня зовут {x['name']} и мне {x['age']}'
print(introduce(dict))
#на словарик

'----------------------------------------------------------------'

nums = [1,2,3,4]
sq = list(map(lambda x:x**2,nums))
print(sq)#база

words = ['чиназс','игрушка','аахаха']
length = list(map(lambda x: len(x),words))
print(length)#посчитал лен стр

pairs =[(1,2),(3,4)]
sums = list(map(lambda x : x[0]+x[1],pairs))
print(sums)#список кортежей


users = [
    {"name": "Аня", "city": "Москва"},
    {"name": "Боря", "city": "Питер"},
    {"name": "Ваня", "city": "Казань"}
    ]
info = list(map(lambda x : f'{x['name']} из {x['city']}',users))
print(info)
#словарик в стр
pairs = [(5, 3), (2, 8), (10, 1), (4, 4)]
n = list(filter(lambda x:x[0]>x[1] ,pairs))
print(n)#tuple

users = [
    {"name": "Аня", "age": 20},
    {"name": "Боря", "age": 16},
    {"name": "Ваня", "age": 18},
    {"name": "Галя", "age": 14},]

n  = list(filter(lambda x : x['age']>=18,users))
print(n)#dict
'===================================================================='
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value ={}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in value:
                return [value[complement],i]
            value[num] = i
        return []

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s = str(x)
        return s == s[::-1]


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
            if not prefix:
                return ''
        return prefix


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(d) for d in digits))
        num += 1
        return [int(c) for c in str(num)]

class Solution:
    def mySqrt(self, x: int) -> int:
        a =int(x**0.5)
        return a

class Solution:
    def climbStairs(self, n: int) -> int:
        return n


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

'===================================='
'''update'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            #обратный порядок индексов
            if digits[i] < 9:
                digits[i] +=1
                return digits
            digits[i]=0

        return [1] + digits


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)  # right = len не len-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                # target точно правее mid двигаем left
                left = mid + 1
            else:
                # nums[mid] >= target,target может быть здесь или левее
                # сужаем right,но mid остаётся в зоне поиска
                right = mid

        return left  # left == right


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # фиктивный узел-заглушка
        current = dummy  # указатель, куда будем вешать новые узлы
        carry = 0  # перенос из предыдущего разряда

        while l1 or l2 or carry:
            # Берём значения, если список закончился — берём 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Суммируем
            total = val1 + val2 + carry

            # Новая цифра — остаток от деления на 10
            carry = total // 10
            digit = total % 10

            # Создаём новый узел и двигаем current
            current.next = ListNode(digit)
            current = current.next

            # Двигаем указатели по спискам, если они ещё есть
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
'===================================================================='
      l1 = self.reverse(l1)
      l2 = self.reverse(l2)

      pass
  def reverse(self,head):
      prev = None
      curr = head

      while curr:
          next_temp = curr.next
          curr.next = prev
          prev = curr
          curr = next_temp
      return prev



class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def find_min(head):
    if not head:
        raise ValueError('список пустой')

    min_node = head
    curr =  head.next

    while curr:
        if curr.value < min_node.value:
            min_node =curr
        curr = curr.next
    return min_node.value


def find_max(head):
    if not head:
        raise ValueError('список пустой')

    max_node = head
    curr = head.next

    while curr:
        if curr.value > max_node.value:
            max_node = curr
        curr = curr.next

    return max_node.value

# --- Создание списка: 7 -> 1 -> 3 -> 4 -> 6 -> 3 ---
head = Node(7)
head.next = Node(1)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(3)

# --- Проверка ---
print(find_min(head))   # 1
print(find_max(head))   # 7




def move(zeros):
    left = 0
    for right in range(len(zeros)):
        if zeros[right] != 0:
            zeros[left],zeros[right] = zeros[right],zeros[left]
            left +=1

zeros = [0,0,1,2,4,5]
move(zeros)
print(zeros)


def moving(zero):
    count = zero.count(0)
    res = [x for x in zero if x!=0]#убираем нули
    res +=[0]*count#добавляем в конец
    zero[:] = res
zero =[2,0,0,0,2,3,4,5,5]
moving(zero)
print(zero)

list1 = [1,2,3,4,5,6]
def reverse(list1):
    prev = None
    curr = list1
    while curr:
        next_node = curr.next #след узел
        curr.next = prev#меняем сслку на пред
        prev = curr#prev вперед сдвиг
        curr = next_node# curr вперед
    return  prev#новый ведущий списка






