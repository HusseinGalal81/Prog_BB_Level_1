

def countSessions():
    Sessions_Attended = {'sessions':'1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
    for v in Sessions_Attended.values(): sessionList = v.split(',')
    sessionsNumber = len(sessionList)
    print(f'I have attended {sessionsNumber} sessions!!')


def main():
    countSessions()


if __name__ == '__main__': main()

