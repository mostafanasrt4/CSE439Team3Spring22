import re


def get_tokens_list(input_code):
    # y = re.search('^(IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
    #               '( ELSE IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)*'
    #               '( ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', input_code)
    NUM = "([0-9]+)"
    ID = "([_a-zA-Z]\w*)"
    STMT = f"({ID}\s*:=\s*({NUM}|{ID})\s*;\s*)"
    IFBODY = f"(IF\s+{NUM}\s+THEN\s+({STMT})+\s*)"
    REGEX = f"(\s*{IFBODY}((ELSE\s+{IFBODY})+)?(ELSE\s+({STMT})+)?END\s*)"
    ################

    tokens_list = []
    tokens = re.findall(r"IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;", input_code)
    for token in tokens:
        if token == "IF":
            tokens_list.append({"token": token, "type": "IF"})
        elif token == "THEN":
            tokens_list.append({"token": token, "type": "THEN"})
        elif token == "ELSE":
            tokens_list.append({"token": token, "type": "ELSE"})
        elif token == "END":
            tokens_list.append({"token": token, "type": "END"})
        elif token == ":=":
            tokens_list.append({"token": token, "type": ":="})
        elif token == ";":
            tokens_list.append({"token": token, "type": ";"})
        elif re.fullmatch("[0-9]+", token) is not None:
            tokens_list.append({"token": token, "type": "NUM"})
        elif re.fullmatch("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
            tokens_list.append({"token": token, "type": "ID"})
        else:
            raise Exception("Invalid token returned from tokenization")

    return tokens_list




# import re
#
#
# def get_tokens_list(input_code):
#     # y = re.search('^(IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+'
#     #               '( ELSE IF [0-9]+ THEN ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)*'
#     #               '( ELSE ([_a-zA-Z][_a-zA-Z0-9]* := ([_a-zA-Z]+[_a-zA-Z0-9]*|[0-9]+);)+)? END)+$', input_code)
#     NUM = "([0-9]+)"
#     ID = "([_a-zA-Z]\w*)"
#     STMT = f"({ID}\s*:=\s*({NUM}|{ID})\s*;\s*)"
#     IFBODY = f"(IF\s+{NUM}\s+THEN\s+({STMT})+\s*)"
#     REGEX = f"(\s*{IFBODY}((ELSE\s+{IFBODY})+)?(ELSE\s+({STMT})+)?END\s*)"
#     ################
#     y = re.fullmatch(REGEX, input_code)
#
#     if y is None:
#         print("Invalid IF statement")
#         return None
#     else:
#         tokens_list = []
#         tokens = re.findall('IF|[0-9]+|THEN|ELSE|END|[_a-zA-Z][_a-zA-Z0-9]*|:=|;', y.string)
#         for token in tokens:
#             if token == "IF":
#                 tokens_list.append({"token": token, "type": "IF"})
#             elif token == "THEN":
#                 tokens_list.append({"token": token, "type": "THEN"})
#             elif token == "ELSE":
#                 tokens_list.append({"token": token, "type": "ELSE"})
#             elif token == "END":
#                 tokens_list.append({"token": token, "type": "END"})
#             elif token == ":=":
#                 tokens_list.append({"token": token, "type": ":="})
#             elif token == ";":
#                 tokens_list.append({"token": token, "type": ";"})
#             elif re.search("[0-9]+", token) is not None:
#                 tokens_list.append({"token": token, "type": "NUM"})
#             elif re.search("[_a-zA-Z][_a-zA-Z0-9]*", token) is not None:
#                 tokens_list.append({"token": token, "type": "ID"})
#             else:
#                 raise Exception("Invalid token returned from tokenization")
#
#         return tokens_list
