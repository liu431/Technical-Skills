class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # fucntion to build the final letters
        def new(s):
            news= []
            for i in s:
                if len(news) == 0:
                    if i != '#':
                        news.append(i)
                else:
                    if i == '#':
                        news.pop()
                    else:
                        news.append(i)
            return news
        return new(s), new(t)
