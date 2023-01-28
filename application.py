from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "hello world !!"

@application.route('/nqueens/<n>')
def n_queens(n):
    head = '<h1>Solving ' + str(n) + ' Queens Problem</h1>\n\n';
    head += 'The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. There are 92 solutions. The problem was first posed in the mid-19th century. In the modern era, it is often used as an example problem for various computer programming techniques'
    body = solve((int)(n));

    return head + body;

def solve(n):
    arr = [['.'] * n for i in range(n)]

    ans = []
    dfs(0, n, 0, arr, set(), set(), set(), set(), ans)

    s = '<pre>'
    for result in ans:
        s += result
    return s;

def render(arr:list):
    str = ''
    for row in arr:
        for ele in row:
            str += ele
            str += ' '
        str += '<br>'
    str += '<br>'
    return str;    

def dfs(index:int, n:int, numQueens:int, arr:list, visitRows:set, visitCols:set, visitDiag:set, visitAnti:set, ans:list):
    if (n == numQueens):
        ans.append(render(arr))
        return;
    
    x = (int)(index / n);
    y = (int)(index % n);

    if x >= n or y >= n:
        return;

    if (x in visitRows or y in visitCols or x + y in visitDiag or x - y in visitAnti):
        dfs(index + 1, n, numQueens, arr, visitRows, visitCols, visitDiag, visitAnti, ans)
        return
    dfs(index + 1, n, numQueens, arr, visitRows, visitCols, visitDiag, visitAnti, ans)

    arr[x][y] = 'Q'
    visitRows.add(x);
    visitCols.add(y);
    visitDiag.add(x + y);
    visitAnti.add(x - y);
    dfs(index + 1, n, numQueens + 1, arr, visitRows, visitCols, visitDiag, visitAnti, ans)
    visitRows.remove(x);
    visitCols.remove(y);
    visitDiag.remove(x + y);
    visitAnti.remove(x - y);
    arr[x][y] = '.'
    

if __name__ == "__main__":
    application.run()