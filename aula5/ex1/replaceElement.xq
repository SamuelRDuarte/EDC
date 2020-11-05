let $cs := collection('CursosUA')//curso
for $a in $cs/nome where $a = "TESTE"
return replace node $a/text()  with "TESTE2020" 