<root>{
  for $a in collection("CursosUA")//curso where $a//areacientifica = "Informática"
  return
  <elem>
    {$a/nome}
  </elem>
}
</root>