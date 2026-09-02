class TrieNode:
    __slots__ = ("ch", "pass_cnt", "word_cnt")

    def __init__(self):
        self.ch = {}
        self.pass_cnt = 0
        self.word_cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, c=1):
        node = self.root
        node.pass_cnt += c
        for x in s:
            if x not in node.ch:
                node.ch[x] = TrieNode()
            node = node.ch[x]
            node.pass_cnt += c
        node.word_cnt += c

    def count(self, s):
        """s の完全一致個数"""
        node = self.root
        for x in s:
            if x not in node.ch:
                return 0
            node = node.ch[x]
        return node.word_cnt

    def count_prefix(self, s):
        """s で始まる単語数"""
        node = self.root
        for x in s:
            if x not in node.ch:
                return 0
            node = node.ch[x]
        return node.pass_cnt

    def contains(self, s):
        return self.count(s) > 0

    def has_prefix_of(self, s):
        """登録語のどれかが s の接頭辞か"""
        node = self.root
        if node.word_cnt:
            return True

        for x in s:
            if x not in node.ch:
                return False
            node = node.ch[x]
            if node.word_cnt:
                return True

        return False

    def delete(self, s, c=1):
        """s を c 個削除。足りなければ False"""
        node = self.root
        path = []

        for x in s:
            if x not in node.ch:
                return False
            path.append((node, x))
            node = node.ch[x]

        if node.word_cnt < c:
            return False

        node.word_cnt -= c
        self.root.pass_cnt -= c

        node = self.root
        for x in s:
            node = node.ch[x]
            node.pass_cnt -= c

        for par, x in reversed(path):
            if par.ch[x].pass_cnt == 0:
                del par.ch[x]
            else:
                break

        return True

    def delete_prefix(self, s):
        """s で始まる単語を全部削除し、削除数を返す"""
        if s == "":
            res = self.root.pass_cnt
            self.root = TrieNode()
            return res

        node = self.root
        path = []

        for x in s:
            if x not in node.ch:
                return 0
            path.append((node, x))
            node = node.ch[x]

        res = node.pass_cnt
        if res == 0:
            return 0

        self.root.pass_cnt -= res

        node = self.root
        for x in s[:-1]:
            node = node.ch[x]
            node.pass_cnt -= res

        par, x = path[-1]
        del par.ch[x]

        for par, x in reversed(path[:-1]):
            if par.ch[x].pass_cnt == 0:
                del par.ch[x]
            else:
                break

        return res
