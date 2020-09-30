#!/user/bin/env python
haha = open("teehee.cpp", "w")
init = """#include <fstream>
int main() {
    const std::string alpha = \"0123456789qwertyuiopasdfghjklzxcvbnm\";
    std::ofstream file;
    const std::string ext = \".txt\";
    const std::string hehe = \"teehee\";\n"""
brackets = 0
haha.write(init)
alpha = "abcdefghijklmnopqrstuvwxyz"
combos = list()
"""
The following would have made a much bigger teehee.cpp
but sadly, you can only have 256 nested for loops in C++
"""
# for i in alpha:
#     combos.append(i)

# for i in alpha:
#     for b in alpha:
#         combos.append(i + b)

# for i in alpha:
#     for b in alpha:
#         for c in alpha:
#             combos.append(i + b + c)

# for i in ["do", "if", "int", "for", "or", "and", "asm", "new", "xor", "not", "try"]:
#     combos.remove(i)

for i in range(256):
    combos.append("a" + str(i))

for z in combos:
    haha.write("\tfor (char {0}: alpha) {1}\n".format(z, "{"))
    brackets += 1

tot = "\t\tfile = std::ofstream(hehe"
for z in combos:
    tot += f" + {z}"
tot += " + ext);\n\t\tfile << \"teehee billions of files\";"
haha.write(tot)

haha.write(brackets * "\t}\n")
haha.write("}")
haha.close()
