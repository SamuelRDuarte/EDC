<root>{
  for $a in distinct-values(collection("CursosUA")//local)
  return
  <elem>
    <local>{$a}</local>{
    for $b in collection("CursosUA")//curso where $b/local = $a
    return
      <curso>{$b/nome/text()}</curso>
  }</elem>
}
</root>

(:resolução do stor:)
(:<root>{
  for $a in distinct-values(collection("CursosUA")//local)
  return
  <elem>
    <local>{$a}</local>
    {
      for $b in collection("CursosUA")//curso[local =$a]
        return
          <curso>{$b/nome/text()}</curso>
  }</elem>
}
</root>:)