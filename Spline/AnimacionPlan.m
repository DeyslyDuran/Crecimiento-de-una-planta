function retval = AnimacionPlan()
n=3;
for i = 1:n
  Planta();
  pause(.2);
  plan2();
  pause(.2);
  plan3();
  pause(.2);

end
