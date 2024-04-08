def gerarGDF(table, filename, direction): # undirected = 0
    n = table['n']
    edge = []
    #para gerar o file so com as edge coloridas
    for i in range(len(table['Edges'])):
       if table['Edges'][i][2] == '0,0,255':     # blue - parent
          edge.append(table['Edges'][i])
       if table['Edges'][i][2] == '255,255,0': # yellow - cousin
         edge.append(table['Edges'][i])
       if table['Edges'][i][2] == '0,255,0':   # green - uncle
          edge.append(table['Edges'][i])
       if table['Edges'][i][2] == '255,0,0':   # red - sibling
          edge.append(table['Edges'][i])

    #sample
    edgeSort = sorted(edge, key=lambda x: x[0])

    if direction == 0:
      dir = 'false'

    with open(filename, 'w') as file:
        file.write('nodedef>name VARCHAR, label VARCHAR\n')  
        for v in range(n):
            file.write(f'{v+1},{v+1}\n')  # my vertix

        file.write('edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n')  
        for p, v, c in edgeSort:
            file.write(f'{p},{v},{dir},\'{c}\'\n')