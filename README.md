# Automação E2DOC

Automação que desenvolvi para a empresa em que trabalho. Essa automação conta com uma interface para interação do usuário, 
e faz conexão com uma plataforma de gestão de documentos voltada para o setor jurídico chamada E2DOC.

O objetivo dessa automação é alimentar a plataforma E2DOC com os comprovantes de pagamento feitos isoladamente no portal de um banco determinado. 
Em detalhes, o que ocorre é que a maioria dos pagamentos feitos pelo setor financeiro são realizados de forma automática pelo sistema ERP da empresa, 
mas, existem os casos onde, devido uma falha no processo, o título de pagamento não pode ser efetivado pelas vias comuns, implicando que seu pagamento seja feito de forma manual, direto no portal do banco.
Esses comprovantes "manuais" precisam estar disponíveis para consulta do setor jurídico na plataforma E2DOC. Ao contrario dos comprovantes pagos pelo sistema ERP, - que alimentam a plataforma automaticamente devido uma integração que há entre o ERP e o E2DOC - os comprovantes manuais não são integrados automaticamente à plataforma, fazendo com que seja necessário a ação de um operador para separar esse documento do arquivo lote de comprovantes extraídos da plataforma do banco, e, fazer a sua integração manual, alimentando uma pasta processual compartilhada na nuvem com aquele documento e preenchendo um formulário com os seus dados no E2DOC, fazendo assim sua indexação.

Na interface de interação, o usuario irá clicar em um botão que o permitirá selecionar o, ou, os arquivos lote desejados. 
O caminho desses arquivos lote é armazenado em uma lista, que será percorrida pela automação. Antigamente, o usuário separava comprovante por comprovante pela sua natureza, pelo seu tipo de pagamento, por exemplo: pagamento de VA, VT, salário, férias, e etc...
Existe uma lista de processos que podem ocorrer pagamento manual, todos mapeados nessa automação, e, cada tipo de natureza de pagamento tem uma pasta final correspondente na nuvem, onde o comprovante deve ser salvo isolado dos demais comprovantes, tendo como título do arquivo apenas o nome completo do colaborador para o qual se destinou aquele pagamento.
Através de uma informação complementar distinta inserida no comprovante "manual" - convencionada em reuniões de levantamento de requisitos onde determinou-se a criação de uma chave de identificação - faz-se então a distinção dos comprovantes. Essa chave obedece a seguinte estrutura: CHAVECPFCÓDDENATUREZA; CHAVE00000000000FER.

A automação irá ler cada comprovante do arquivo lote, separar aquele pago manualmente, coletar o CPF do colaborador, destiná-lo a sua pasta processual final, e, através do CPF, buscar os dados pertinentes ao preenchimento do formulário do E2DOC direto no banco de dados da empresa, depois integrar os tais comprovantes à plataforma através da API que eles disponibilizam para os seus clientes.
Essa é a versão Beta que já está em produção. Durante um período determinado a automação estará funcionando nessa versão, e caso alguma excepcionalidade aconteça, será tratada.
