from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect

def compare(str1, str2):
    rows = len(str1) + 1
    cols = len(str2) + 1
    matrix = [['0' for x in range(cols)] for y in range(rows)]

    # Assign strings to array
    i = 1
    while(i != rows):
        matrix[i][0] = str1[i - 1]
        i = i + 1
    
    i = 1
    while(i != cols):
        matrix[0][i] = str2[i - 1]
        i = i + 1

    # Processing
    i = 2
    while(i != cols):
        matrix[1][i] = str(int(matrix[1][i - 1]) + -2)
        i = i + 1

    i = 2
    while( i != rows):
        matrix[i][1] = str(int(matrix[i - 1][1]) + -2)
        i = i + 1

    # Alignment
    i = 2
    while(i != rows):
        j = 2
        while(j != cols):
            d = 1
            if matrix[i][0] != matrix[0][j]:
                d = -1
            matrix[i][j] = str(max(int(matrix[i - 1][j - 1]) + d, int(matrix[i - 1][j]) - 2, int(matrix[i][j - 1]) - 2))
            j = j + 1
        i = i + 1

    # Trace-back
    arr_tb = []
    def traceback(matrix, r, c, str_tb = str(rows - 1) + str(cols - 1) + '.'):
        if r == 1 and c == 1:
            arr_tb.append(str_tb)
            return

        d = -1
        if matrix[r][0] != matrix[0][c]:
            d = 1

        temp = int(matrix[r][c]) + 2
        temp_dia = int(matrix[r][c]) + d

        if matrix[r - 1][c - 1] == str(temp_dia):
            traceback(matrix, r - 1, c - 1, str_tb = str_tb + str(r - 1) + str(c - 1) + '.')

        if matrix[r - 1][c] == str(temp):
            traceback(matrix, r - 1, c, str_tb = str_tb + str(r - 1) + str(c) + '.')

        if matrix[r][c - 1] == str(temp):
            traceback(matrix, r, c - 1, str_tb = str_tb + str(r) + str(c - 1) + '.')

    traceback(matrix, rows - 1, cols - 1)

    arr_tb = [s.split('.') for s in arr_tb]

    arr_tb = [[s for s in l if len(s) != 0]
          for l in arr_tb]

    str_des = []
    for index in  range(len(arr_tb)):
        str_temp = ''
        for iter in range(len(arr_tb[index]) - 1):
            x1 = int(arr_tb[index][iter][0])
            y1 = int(arr_tb[index][iter][1])

            x2 = int(arr_tb[index][iter + 1][0])
            y2 = int(arr_tb[index][iter + 1][1])

            if x1 - 1 == x2 and y1 - 1 == y2:
                str_temp = str_temp + matrix[0][y1]
            else:
                str_temp = str_temp + '--'
        str_des.append(str_temp)

    str_des = [s[::-1] for s in str_des]
    #del str1[0]

    return str_des

def home(request):
    if request.method == "POST":
        test_1 = request.POST['test_1']
        test_2 = request.POST['test_2']

        rs = compare('-' + test_1, '-' + test_2)

        html_rs = test_1 + '<br />'

        for i in rs:
            html_rs += i + '<br />'


        return HttpResponse('result: <br />' + html_rs )
    return render(request, 'biocom/SenAli.html')