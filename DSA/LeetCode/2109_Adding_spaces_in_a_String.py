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
        # print(f"i: {i}, c: {c}")
        logging.info(f"i: {i}, c: {c}" )
        
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

add_spaces(s,spaces)