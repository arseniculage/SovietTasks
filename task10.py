import random

list_=[['Коллеги,','В то же время,','Однако,','Тем не менее,','Следовательно,','Соответственно,','Вместе с тем,','С другой стороны,'],
      ['парадигма цифровой экономики','контекст цифровой трансформации','дижитализация бизнес-процессов','паргматичный подход к цифровым платформам','совокупность сквозных технологий','программа прорывных исследований','ускорение блокчейн-транзакций','экспоненциальный рост Big Data'],
      ['открывает новые возможнсти','выдвигает новые требования','несет в себе риски','расширяет горизонты','заставляет искать варианты','не оставляет шанса для','повышает вероятность','обостряет проблему'],
      ['дальнейшего углубления','бюджетного финансирования','синергического эффекта','компрометации конфеденциальных','универсальной коммодитизации','несанкционированной кастомизации','нормативного регулирвания','практического применения'],
      ['знаний и компетенций.','непроверенных гипотез.','волатильных активов.','опасных экспериментов.','государственно-частных партенрств.','цифровых следов граждан.','нежелательных последствий.','внезапных открытий.']]

prob=[ [560,0,0,0,0,0,0,0],
        [70,70,70,70,70,70,70,70],
        [70,70,70,70,70,70,70,70],
        [70,70,70,70,70,70,70,70],
        [70,70,70,70,70,70,70,70] ]


pgphs = input()
for sooqa in range(int(pgphs)):
    #generate paragraph
    random.seed(version=2)
    par_prob = [random.randrange(0,560) for i in range(5)]


    #picking parts
    paragraph = ''
    for i in range(5) :
        for elem_prob in range(len(prob[i])):
            if par_prob[i] - prob[i][elem_prob] < 0 :
                paragraph+=list_[i][elem_prob]+' '
                for it in range(8):
                    if it != elem_prob :
                        prob[i][it]+=(prob[i][elem_prob]//7)
                temp = prob[i][elem_prob]%7
                prob[i][elem_prob] = 0
                prob[i][random.randrange(0,7)]+=temp
                break
            else: 
                par_prob[i]-=prob[i][elem_prob]
    print(paragraph)
            
            





