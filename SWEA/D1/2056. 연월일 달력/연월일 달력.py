T = int(input())
date_range = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    date = input()
    format_data = date[:4]+'/' + date[4:6]+'/' + date[6:8]
    if 0 < int(date[4:6]) < 13 and 0 < int(date[6:8]) <= date_range[int(date[4:6])-1]:
        print("#"+str(tc), format_data)
    else:
        print("#"+str(tc), -1 )