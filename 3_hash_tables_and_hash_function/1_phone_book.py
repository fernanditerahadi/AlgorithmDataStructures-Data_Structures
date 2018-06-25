#Uses Python3
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

    def __str__(self):
        try:
            return "%s %s %s" % (self.type, self.number, self.name)
        except:
            return "%s %s" % (self.type, self.number)

class PhoneBook:
    def read_queries(self):
        n = int(input())
        return [Query(input().split()) for i in range(n)]

    def process_queries(self, queries):
        result = []
        # Keep list of all existing (i.e. not deleted yet) contacts.
        contacts = {}
        for cur_query in queries:
            if cur_query.type == 'add':
                contacts[cur_query.number] = cur_query.name
            elif cur_query.type == 'del':
                contacts.pop(cur_query.number, None)
            elif cur_query.type == 'find':
                result.append(contacts.get(cur_query.number, 'not found'))
        return result

    def write_responses(self, result):
        print('\n'.join(result))

if __name__ == '__main__':
    phone_book = PhoneBook()
    phone_book.write_responses(phone_book.process_queries(phone_book.read_queries()))
