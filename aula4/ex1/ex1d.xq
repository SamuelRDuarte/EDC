<root>{
  for $a in distinct-values(collection("CursosUA")//areacientifica)
  return
  <elem>
    {$a}
  </elem>
}
</root>