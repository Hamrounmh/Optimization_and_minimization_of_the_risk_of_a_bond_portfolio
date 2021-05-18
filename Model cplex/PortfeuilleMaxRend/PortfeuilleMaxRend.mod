/*********************************************
 * OPL 20.1.0.0 Model
 * Author: hamro
 * Creation Date: 16 janv. 2021 at 03:19:52
 *********************************************/
/*********************************************
 * OPL 20.1.0.0 Model
 * Author: hamro
 * Creation Date: 19 déc. 2020 at 22:16:29
 *********************************************/

/* DATA VARIABLES ___________*/
int Actifs=...;
range numberActifs = 1..Actifs;
float R= ...;
float Rendements[numberActifs]=...;
int alphaNumber = ...;
float cVarSeuil [1..alphaNumber]=...;
float alphaValues [1..alphaNumber] = ...;
int s = ...;
range Simulations = 1..s;
float yProbabilites [Simulations][numberActifs]=...;
float bValues [numberActifs]=...;

/* DECISION VARIABLE ___________*/

dvar float+ x[1..Actifs];
dvar float k;
dvar float ZFunction[Simulations];
dexpr float objective = sum(i  in  numberActifs)Rendements[i]*x[i];


/* OBJECTIF FUNCTION ___________*/
maximize objective;


/* Constraintes ________*/
subject to {
  forall(j in 1..alphaNumber){
     k + (1/((1-alphaValues[j])*s)) * sum(s in Simulations) ZFunction[s] <= cVarSeuil[j];
    
  }

    forall(s in Simulations){ 
    ZFunction[s]>=(sum(i in numberActifs) x[i]*(bValues[i]-yProbabilites[s][i]))-k;
    ZFunction[s]>=0;
  }
       sum(i in numberActifs)x[i]== 1;
}

float TotalReturn = sum(i in numberActifs) Rendements[i]*x[i];

execute DISPLAY {
  writeln("Total Expected Return: ", TotalReturn);
  writeln("VAR: ", k);
  writeln("x: ", x);
}
 