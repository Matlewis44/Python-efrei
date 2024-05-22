def myPutStr(x):
  if isinstance(x, str):
    return x
  elif isinstance(x, int) or isinstance(x, float):
    return "Et pourquoi pas 42 ?"
  else:
    return "Type non pris en charge"

print(myPutStr(17))
