declare updating function local:replace-curso($anome, $anomereplace){
  let $cs := collection('CursosUA')//curso
  for $a in $cs/nome where $a = $anome
    return replace node $a/text()  with $anomereplace 
};

local:replace-curso("TESTE","TESTE2022")