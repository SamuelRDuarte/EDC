<root>{
  for $a in collection("CursosUA")//curso
  return
  <elem>
    {$a/guid}
    {$a/nome}
  </elem>
}
</root>
