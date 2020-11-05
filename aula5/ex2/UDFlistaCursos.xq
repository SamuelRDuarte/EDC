module namespace funcs = "com.funcs.my.index";

declare function funcs:lista-cursos(){
  for $a in collection("CursosUA")//curso
  return
  <elem>
    {$a/guid}
    {$a/nome}
  </elem>
};
