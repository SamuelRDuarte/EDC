<root>{
  for $a in collection("CursosUA")//curso where $a/local = "Campus Universitário de Santiago, Aveiro"
  return
  <elem>
    {$a/nome}
  </elem>
}
</root>