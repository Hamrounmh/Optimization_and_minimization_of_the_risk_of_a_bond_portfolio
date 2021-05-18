/*********************************************
 * OPL 20.1.0.0 Model
 * Author: hamro
 * Creation Date: 20 déc. 2020 at 13:01:52
 *********************************************/


/* DATA VARIABLES ___________*/
int Actifs=...;
range numberActifs = 1..Actifs;
float R= ...;
float Rendements[numberActifs]=...;
float a = ...;
int s = ...;
range Simulations = 1..s;
float yProbabilites [Simulations][numberActifs]=...;
float bValues [numberActifs]=...;
/* DECISION VARIABLE ___________*/

dvar float+ x[1..Actifs];
dvar float k;
dvar float ZFunction[Simulations];
dexpr float Objective = k + (1/((1-a)*s)) * sum(s in Simulations) ZFunction[s];

/* OBJECTIF FUNCTION ___________*/
minimize  Objective;

/* CVAR MODEL CONSTRAINTES __________*/
subject to {
  forall(s in Simulations){
    ZFunction[s]>=(sum(i in numberActifs) x[i]*(bValues[i]-yProbabilites[s][i]))-k;
    ZFunction[s]>=0;
  }
  forall(i in numberActifs){
    x[i] >= 0;
	} 
  sum(i in numberActifs)x[i]==1;
  sum(i in numberActifs) (x[i]*Rendements[i]) >= R;
 
}
float TotalReturn = sum(i in numberActifs) Rendements[i]*x[i];
float Varx = k;
float Cvar = Objective;


execute DISPLAY {
  writeln("Total Expected Return: ", TotalReturn);
    writeln("VAR        : ", Varx);
    writeln("Cvar       : ", Cvar);
    writeln("x       : ", x);
     
  
}
