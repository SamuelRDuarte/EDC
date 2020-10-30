<root>{
  for $a in distinct-values(collection("CursosUA")//local)
  return
  <elem>
    {$a}
  </elem>
}
</root>