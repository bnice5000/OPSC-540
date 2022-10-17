#include <stdio.h>
#include <string.h>

main()
{
  char code[200];

  gets(code);

  int (*ret)() = (int(*)())code;

  ret();
}
