
# 383. 赎金信

# 给你两个字符串：ransomNote 和 magazine ，
# 判断 ransomNote 能不能由 magazine 里面的字符构成。
#
# 如果可以，返回 true ；否则返回 false 。
#
# magazine 中的每个字符只能在 ransomNote 中使用一次。
#
#  
#
# 示例 1：
#
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 示例 2：
#
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazine = list(magazine)
    for i in ransomNote:
        if i in magazine:
            magazine.remove(i)
        else:
            return False
    return True