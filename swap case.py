def swap_case(s):
    answer=[]
    for each in s:
        if each.isupper():
            answer.append(each.lower())
        else:
            answer.append(each.upper())

    return"".join(answer)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
