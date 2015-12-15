patterns = ['cs21.txt', 'arrowtoleft.txt']
for pattern in patterns:
    with open(pattern, 'r') as fIn:
        print 'void ' + pattern[:-4] + '(int fd)'
        print '{'
        print '\t// fd = frame duration (1 frame = fd milliseconds)'
        print ''
        row = 0
        while True:
            line = fIn.readline().strip()
            if not line:
                break

            s = ''
            if line == '-':
                print '\tlight_board(fd);'
                print ''
                row = 0
            else:
                line = line.split()
                line = [int(x) for x in line]
                for i, val in enumerate(line):
                    if i:
                        s += ' '
                    s += 'board[' + str(row) + '][' + str(i) + '] = ' + str(val) + ';'
                print '\t' + s
                row += 1
        print '\tlight_board(fd);'
        print '}'