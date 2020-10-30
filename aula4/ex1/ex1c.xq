<root>{
  for $a in distinct-values(collection("CursosUA")//departamento)
  return
  <elem>
    {$a}
  </elem>
}
</root>