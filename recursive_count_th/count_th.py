'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    th_idx = -1
    # * Base Case is where there are no 'th' in word
    if 'th' not in word:
        return 0
    # * If word contains 'th', increment by one and slice word and pass it to count_word
    if 'th' in word:
        th_idx = word.index('th')
        th_idx_end = th_idx + 2
        return 1 + count_th(word[th_idx_end:])


# print(count_th('fourth'))
# print(count_th('fourthrouth'))
print(count_th('thoughth'))
