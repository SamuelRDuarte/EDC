<root>{
  for $a in distinct-values(collection("CursosUA")//departamento)
  return
  <elem>
    <departamento>{$a}</departamento>{
    for $b in collection("CursosUA")//curso where $b//departamento = $a
    return
      <curso>{$b/nome/text()}</curso>
  }</elem>
}
</root>