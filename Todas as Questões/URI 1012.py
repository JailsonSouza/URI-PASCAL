program uri1012;
var
A, B, C, pir: real;
areatri, areacir, areatra, areaqua, arearet : real;

begin
  readln(A, B, C);
  pir := 3.14159;
  areatri := (A * C)/2;
  areacir := (pir * (C * C));
  areatra := ((A + B)/2)* C;
  areaqua := (B * B);
  arearet := (A * B);
  writeln('TRIANGULO: ',areatri:2:3);
  writeln('CIRCULO: ',areacir:2:3);
  writeln('TRAPEZIO: ',areatra:2:3);
  writeln('QUADRADO: ', areaqua:2:3);
  writeln('RETANGULO: ',arearet:2:3);
end.