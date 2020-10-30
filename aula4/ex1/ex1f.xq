<root>{
  for $a in collection("CursosUA")//curso where $a/guid = 17
  return
  <elem>
    {$a//departamento}
  </elem>
}
</root>