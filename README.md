# python_test
cinq python test

#inicio 9:50
#fim 12:30
#total 2:40

Comentarios:
    -processo faz transicao do processing para collecting, porém não existe esa transição na tabela. 
    Se permitir o processo executar essa ação, o usuário também poderá, a menos que crie uma variável
    de controle de chamada, verificando se foi o processo ou o usuário que chamou o método.
    -a transição automática do processing para collecting e vice versa gera loop sem fim, por isso 
    espera confirmação do usuário para continuar as transições.
    -para terminar o processo insira estado 'fim'
    -para verificação de entrada foi usado if's aninhados, não sendo necessariamente a melhor opção.
    -nome de estado e input para mudar os estados é diferente, fiz um método para igualar.
    -info mostra as informaçõs do objeto