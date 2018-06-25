# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.bucket = int(query[1])
        else:
            self.strings = query[1]

    def __str__(self):
        try:
            return "%s %s %s" % (self.type, self.bucket)
        except:
            return "%s %s" % (self.type, self.strings)

class QueryProcessor:
    x = 263
    p = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = [[] for i in range(bucket_count)]

    def hash_function(self, strings):
        answer = 0
        for element in reversed(strings):
            answer = (answer * self.x + ord(element)) % self.p
        return answer % self.bucket_count

    def add(self, strings):
        hash = self.hash_function(strings)
        if strings not in self.hash_table[hash]:
            self.hash_table[hash] += [strings]

    def check(self, bucket):
        return print(" ".join(reversed(self.hash_table[bucket])))

    def find(self, strings):
        hash = self.hash_function(strings)
        if strings in self.hash_table[hash]:
            print('yes')
        else:
            print('no')

    def delete(self,strings):
        hash = self.hash_function(strings)
        try:
            self.hash_table[hash].remove(strings)
        except:
            print(' ')

    def process_queries(self):
        n = int(input())
        for i in range(n):
            query = Query(input().split())
            if query.type == 'add':
                self.add(query.strings)
            elif query.type == 'check':
                self.check(query.bucket)
            elif query.type == 'find':
                self.find(query.strings)
            elif query.type == 'del':
                self.delete(query.strings)


if __name__ == '__main__':
    bucket_count = int(input())
    query_processor = QueryProcessor(bucket_count)
    query_processor.process_queries()
