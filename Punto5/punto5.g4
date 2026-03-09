grammar punto5;

stat: 'FIBO' '(' INT ')' ;

INT: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ; // Ignorar espacios en blanco