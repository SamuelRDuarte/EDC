<root>{
  for $a in collection("CursosUA")//curso where $a//departamento = "Departamento de Biologia"
  return
  <elem>
    {$a/nome}
  </elem>
}
</root>