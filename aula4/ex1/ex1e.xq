<root>{
  for $a in collection("CursosUA")//curso where $a/guid = 17
  return
  <elem>
    {$a/nome}
    {$a/codigo}
    {$a/grau}
    {$a/local}
    
  </elem>
}
</root>