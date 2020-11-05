declare updating function local:delete-curso($anome){
  let $cs := collection('CursosUA')//curso
  for $a in $cs where $a/guid = $anome
    return delete node $a
};

local:delete-curso("$aguid")