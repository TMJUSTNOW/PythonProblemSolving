def PrintMatrixSpiral(matrix):
  '''
    given a matrix, print out in a spiral form   
    Args: matrix: two dimensional array
  '''
  rowNum = len(matrix) - 1
  columnNum = len(matrix[0]) - 1 
  startRow = 0
  startColumn = 0

  while startRow < rowNum and startColumn < columnNum:
  # print the first row for the remaining column
    if startColumn < columnNum:
      for col in range(startColumn, columnNum + 1):
        print matrix[startRow][col]
      startRow += 1
  # print the last column for the remaining rows
    if startRow < rowNum:
      for row in range(startRow, rowNum + 1):
        print matrix[row][columnNum]
      columnNum -= 1
  # print the last row in reverse order
    if startColumn < columnNum:
      for col in range(columnNum, startColumn - 1, -1):
        print matrix[rowNum][col]
      rowNum -= 1
  # print the first column in reverse order
    if startRow < rowNum:
      for row in range(rowNum, startRow - 1, -1):
        print matrix[row][startColumn]
    startColumn += 1


matrix = [
          [1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]
          ]
PrintMatrixSpiral(matrix)