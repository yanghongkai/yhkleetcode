
# 71 简化路径 https://leetcode-cn.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path):
        if path[-1] != "/":
            path += "/"
        stack = []
        atom = ""
        i = 0
        while i < len(path):
            s = path[i]
            # /h /. //
            # print("i:", i)
            # print("s:", s)
            if s == "/":
                if atom:
                    # print("atom:", atom)
                    if atom == "..":
                        if stack:
                            stack.pop()
                    elif atom != ".":
                        stack.append(atom)
                while i < len(path) and path[i] == "/":
                    i += 1
                atom = ""
            # /home
            elif s  not in [".", "/"]:
                while i < len(path) and path[i] not in [".", "/"]:
                    atom += path[i]
                    i += 1
            elif s == ".":
                # . 不用任何操作
                # ..
                # ... 多个点就用多个点表示
                # ..hidden
                while i < len(path) and path[i] == ".":
                    atom += path[i]
                    i += 1
        simple_path = "/"
        if len(stack) > 1:
            simple_path += "/".join(stack)
        else:
            simple_path += stack[0] if stack else ""
        return simple_path




path = "/home/"
path = "/home//foo/"
path = "/a/./b/../../c/"
# path = "/a/../../b/../c//.//"
path = "/a//b////c/d//././/.."
path = "/../"
# path = "/..."
# path = "/..hidden"
path = "/home/foo/.ssh/authorized_keys/"

s = Solution()
print(s.simplifyPath(path))





