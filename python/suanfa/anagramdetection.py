class AnagramDetection:
    def anagramSolution1(self,s1,s2):
        # 对字符串 列表化
        alist1=list(s1)
        alist2=list(s2)
        return alist1

s1 = 'abcde'
s2 = 'acbde'
test = AnagramDetection()
print(test.anagramSolution1(s1, s2))
