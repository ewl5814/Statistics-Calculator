import sys
import math

from fontTools.misc.py23 import xrange


def load_numbers(filename):
    numbers = list()
    probs = list()
    count = 0
    with open(filename, encoding='UTF 8') as f:
        for line in f:
            pieces = line.split()
            for j in pieces:
                if count < 1:
                    numbers.append(float(j))
                else:
                    probs.append(j)
            count += 1
    return numbers,probs


def main() -> None:
    fn = sys.argv[1]
    print(fn)
    decision = input("Binomial Prob: (P)    Stats: (S)")
    if decision == 'S':
        nums, probs = load_numbers(fn)
        numbers = quick_sort(nums)
        e = 0
        for k in range(len(probs)):
            e += float(numbers[k])*float(probs[k])

        for i in numbers:
            print(i)
        print("\n# of Elements: " + str(len(numbers)))
        sum = 0
        psum = 0
        for i in numbers:
            sum += float(i)
            psum += math.pow(float(i), 2)

        print("Sigma: " + str(sum) + " Sigma^2: " + str(psum))
        print("E(x): " + str(e))
        print("Median: " + str(median(numbers, len(numbers))))
        print("Mean: " + str(mean(numbers, len(numbers))))
        sv = standard_variance(numbers, len(numbers), mean(numbers, len(numbers)))
        if len(probs) > 0:
            esv = e_standard_variance(nums, len(numbers), e, probs)
        else:
            esv = 0
        print("Sample Variance: " + str(sv) + " E(x) SV: " + str(esv))
        print("Sample Standard Deviation: " + str(math.sqrt(sv)) + " E(x) STD: " + str(math.sqrt(esv)))
    else:
        n = input("input n:")
        p = input("input probability:")
        binomial_prob(int(n), float(p))



def binomial_prob(n, p):
    bis = list()
    i = 0
    for i in range(n):
        b = ((factorial(n)/(factorial(n-i)*factorial(i))) * math.pow(p, i) * math.pow(1-p, n - i))
        bis.append(b)
    for i in bis:
        print(str(i) + " ")
    x = 0
    j = 10
    for j in range(n):
        x += bis[j]
    print(str(x))
def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num > 1:
        return num*factorial(num - 1)

def _partition(data, pivot):
    less, equal, greater = [], [], []
    for element in data:
        if float(element) < float(pivot):
            less.append(element)
        elif float(element) > float(pivot):
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater

def quick_sort(data):
    if len(data) == 0:
        return []
    else:
        pivot = data[0]
        less, equal, greater = _partition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)


def median(list, n):
    if n % 2 == 1:
        med = list[(n + 1) // 2 - 1]
    elif n % 2 == 0:
        med = (float(list[int(n / 2) - 1]) + float(list[int(n / 2 + 1) - 1])) / 2
    return med


def mean(list, n):
    add = 0
    for i in list:
        add += float(i)
    mean = add / n
    return mean


def standard_variance(list, n, mea):
    sum = 0.0
    for i in list:
        sum += math.pow(float(i) - mea, 2)
    var = sum / (n-1)
    return var

def e_standard_variance(list, n, e, probs):
    sum = 0.0
    for i in range(len(list)):
        sum += math.pow(float(list[i]) - e, 2)*float(probs[i])
    return sum

if __name__ == '__main__':
    main()
