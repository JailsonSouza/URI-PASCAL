program uri1011;
var 
raio, pir, volume: real;

begin
  ReadLn(raio);

  pir:= 3.14159;
  volume := (4.0/3) * pir * (raio * raio * raio);
  WriteLn('VOLUME = ', volume:0:3);
end.