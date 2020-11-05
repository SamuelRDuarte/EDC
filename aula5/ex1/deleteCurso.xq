let $cs := collection('CursosUA')//curso
for $a in $cs where $a/nome = "TESTE2020"
return delete node $a