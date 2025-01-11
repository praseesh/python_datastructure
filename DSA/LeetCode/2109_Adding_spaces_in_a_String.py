import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="new_log.log",
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s ",
                    )
def add_spaces(s, spaces):
    ans = []
    space = set(spaces)
    for i, c in enumerate(s):
        logging.info(f"i: {i}, c: {c}" )
        if i in space:
            ans.append(" ")
        ans.append(c)
        
    return "".join(ans)
        
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

print(add_spaces(s,spaces))