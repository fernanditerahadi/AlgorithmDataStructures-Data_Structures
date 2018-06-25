# python3
import random
class RabinKarp:
    def __init__(self):
        self.prime = 1000000007
        self.random_x = random.randint(1, self.prime)

    def poly_hash(self, strings, prime, random_x):
        hash = 0
        length = len(strings)
        for s in reversed(strings):
            hash = ((hash * random_x + ord(s)) % prime)
        return hash

    def precompute_hash(self, text, pattern_length, prime, x):
        text_length = len(text)
        hash = [0] * (text_length - pattern_length + 1)
        strings = text[-pattern_length:]
        hash[(text_length - pattern_length)] = self.poly_hash(strings, prime, x)
        y = 1
        for i in range(1, pattern_length+1):
            y = (y * x) % prime
        for i in reversed(range(text_length-pattern_length)):
            hash[i] = (x * hash[i+1] + ord(text[i]) - y * ord(text[i+pattern_length])) % prime
        return hash

    def are_equal(self, text, pattern):
        if len(text) != len(pattern):
            return False
        for i in range(0, len(text)):
            if text[i] != pattern[i]:
                return False
        return True

    def rabin_karp(self, text, pattern):
        result = []
        text_length = len(text)
        pattern_length = len(pattern)
        pattern_hash = self.poly_hash(pattern, self.prime, self.random_x)
        precomputed_hash = self.precompute_hash(text, pattern_length, self.prime, self.random_x)
        for i in range(0, text_length-pattern_length+1):
            if pattern_hash != precomputed_hash[i]:
                continue
            if self.are_equal(text[i : i+pattern_length], pattern):
                result.append(i)
        return result

    def print_output(self, result):
        print(' '.join(map(str, result)))

    def read_input(self):
        pattern = input().rstrip()
        text = input().rstrip()
        return text, pattern

if __name__ == '__main__':
    find_pattern = RabinKarp()
    text, pattern = find_pattern.read_input()
    result = find_pattern.rabin_karp(text, pattern)
    find_pattern.print_output(result)
