<root>{
  for $a in distinct-values(collection("CursosUA")//areacientifica)
  return
  <elem>
    <areacientifica>{$a}</areacientifica>{
    for $b in collection("CursosUA")//curso where $b//areacientifica = $a
    return
      <curso>{$b/nome/text()}</curso>
  }</elem>
}
</root>