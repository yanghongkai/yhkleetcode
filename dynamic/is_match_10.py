
# 10. 正则表达式匹配  https://leetcode-cn.com/problems/regular-expression-matching/


# 字符串匹配 递归

def is_match(s, p):
    # base 两者都为空时，返回True
    if not p:
        return not s
    return s[0] == p[0] and is_match(s[1:], p[1:])


# 正则 . * 递归
def is_match_1(text, pattern):
    if not pattern:
        return not text
    first_match = text[0] and pattern[0] in {text[0], "."}
    # 处理 *
    if len(pattern) >= 2 and pattern[1] == "*":
        return is_match_1(text, pattern[2:]) or first_match and is_match_1(text[1:], pattern)
    else:
        return first_match and is_match_1(text[1:], pattern[1:])


# 普通字符串匹配，非递归

def is_match_normal(s, p):
    if len(s) != len(p):
        return False
    while i < len(s):
        if i > len(p):
            return False
        if s[i] != p[i]:
            return False
    return True


# 双指针实现字符串匹配
def is_match_pointer(s, p):
    i = 0
    j = 0
    while i < len(s):
        if i >= len(p):
            return False
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            return False
    if i == len(j):
        return True













