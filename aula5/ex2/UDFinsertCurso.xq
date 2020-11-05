declare updating function local:insert-curso($anome, $aguid){
  let $cs := collection('CursosUA')/cursos
  return insert node <curso><guid>{$aguid}</guid><nome>{$anome}</nome></curso> as first into $cs
};

local:insert-curso("TESTE","1000")