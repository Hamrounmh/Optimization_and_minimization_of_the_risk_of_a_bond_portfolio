/*********************************************
 * OPL 20.1.0.0 Model
 * Author: hamro
 * Creation Date: 19 déc. 2020 at 22:16:29
 *********************************************/

/* DATA VARIABLES ___________*/
int Actifs=...;
range numberActifs = 1..Actifs;
float R= ...;
float Cov[numberActifs][numberActifs]=...;
float Rendements[numberActifs]=...;
int wealth = ...;


/* DECISION VARIABLE ___________*/
dvar float+ x[numberActifs];
dexpr float objective = 1 ; //sum(i ,j in  numberActifs)Cov[i][j]*x[i]*x[j];


/* OBJECTIF FUNCTION ___________*/
minimize objective;


/* Constraintes ________*/
subject to {
  sum(i in numberActifs)x[i]== wealth;
  
 sum(i in numberActifs) (x[i]*Rendements[i]) >= R ;
  
}

float TotalReturn = sum(i in numberActifs) Rendements[i]*x[i];
float TotalVariance = sum(i,j in numberActifs) Cov[i][j]*x[i]*x[j];

execute DISPLAY {
  writeln("Total Expected Return: ", TotalReturn);
  writeln("Total Variance       : ", TotalVariance);
}
