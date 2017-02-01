import os 
os.chdir('/home/anderson/Documentos/Projetos/Redes Mutualisticas e Coevolucao') #MTA ATENCAO AQUI: diretorio de trabalho!
import time

start_time = time.time()
mensagem = '||| Runing Nuismer Model |||'
print mensagem.center(100)
###########
###########

alpha = [0.01,0.5,0.9]
gamma = [0.01,0.5,0.9]

for i in alpha:
    for j in gamma:
        mymodel = nuismerModel(50,10,10,3,200,0.9,0.07,2,50) #paratriza o modelo
        mymodel.run() #roda
        #salvando arquivos
        pd.DataFrame(mymodel.outputInteractionMatrix).to_csv('intMat'+str(i)+str(j)+'.csv') #salva matriz de interacao como arquivo .csv
        pd.DataFrame(mymodel.outputPlantsPop).to_csv('plaPop'+str(i)+str(j)+'.csv') #salva abundancia de plantas como arquivo .csv
        pd.DataFrame(mymodel.outputAnimalPop).to_csv('aniPop'+str(i)+str(j)+'.csv') #salva abundancia de animais como arquivo .csv
        pd.DataFrame(mymodel.outputAnimalFenMean).to_csv('aniFenMean'+str(i)+str(j)+'.csv') #salva fenotipo medio das sps animais como .csv
        pd.DataFrame(mymodel.outputAnimalFenSD).to_csv('aniFenSD'+str(i)+str(j)+'.csv') #salva SD do fenotipo de animais como arquivo .csv
        pd.DataFrame(mymodel.outputPlantsFenMean).to_csv('plaFenMean'+str(i)+str(j)+'.csv') #salva fenotipo medio das sps plantas como .csv
        pd.DataFrame(mymodel.outputPlantsFenMean).to_csv('plaFenSD'+str(i)+str(j)+'.csv') #salva SD do fenotipo de plantas como arquivo .csv


#pl.plot(mymodel.outputAnimalPop)
#pl.plot(mymodel.outputPlantsPop)
#pl.plot(mymodel.outputAnimalFenMean)
#pl.show()

###########
###########
print '\nTime: %s minutes\n'  % ((time.time()-start_time)/60)

# import sys
# bar_length=50
# end_val = 500
# for i in xrange(0, end_val):
#         time.sleep(0.01)
#         percent = float(i) / end_val
#         hashes = '#' * int(round(percent * bar_length))
#         spaces = ' ' * (bar_length - len(hashes))
#         sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
#         sys.stdout.flush()

# print "\nFim!!\n"
