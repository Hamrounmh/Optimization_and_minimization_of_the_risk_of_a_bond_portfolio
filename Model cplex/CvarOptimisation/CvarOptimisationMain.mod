/*********************************************
 * OPL 20.1.0.0 Model
 * Author: hamro
 * Creation Date: 20 déc. 2020 at 21:48:45
 *********************************************/
 
 /* DATA VARIABLES ___________*/
int Actifs=...;
float R= ...;
float Rendements[1..Actifs]=...;
float a = ...;
int s = ...;
float yProbabilites [1..s][1..Actifs]=...;
float bValues [1..Actifs]=...;


/* DECISION VARIABLE ___________*/

dvar float+ x[1..Actifs];
dvar float k;
dvar float ZFunction[1..s];


/* OBJECTIF FUNCTION ___________*/
minimize k + (1/((1-a)*s)) * sum(s in 1..s) ZFunction[s];

/* CVAR MODEL CONSTRAINTES ___________*/
subject to {
  forall(s in 1..s){
    ZFunction[s]>=0;
    ZFunction[s]>=(sum(i in 1..Actifs)x[i]*(bValues[i]-yProbabilites[s][i]))-k;
  }
  forall(i in 1..Actifs){
    x[i] >= 0;
  } 
  sum(i in 1..Actifs)x[i]==1;
  
 sum(i in 1..Actifs) (x[i]*Rendements[i]) >= R ;
  
}


//main {
//  thisOplModel.a=0.99;
//thisOplModel.generate();
//
//
//if (cplex.solve()) {
// writeln("OBJ = ", cplex.getObjValue());
//}
//else {
// writeln("No solution");
//}
//
//
//
//
//}
//main {
// 
//var source = new IloOplModelSource("CvarOptimisationMain.mod");
//var def = new IloOplModelDefinition(source);
//var opl = new IloOplModel(def,cplex);
//var data = new IloOplDataSource("CvarOptimisation.dat");
//
//opl.addDataSource(data);
//opl.generate();
//
//
//if (cplex.solve()) {
// writeln("OBJ = ", cplex.getObjValue());
//}
//else {
// writeln("No solution");
//}
//opl.end();
//data.end();
//def.end();
//source.end();
//}


main { 

   thisOplModel.settings.mainEndEnabled = true;
    thisOplModel.generate();

     var Actifs=thisOplModel.Actifs;
    var R = thisOplModel.R;
    var Rendements = thisOplModel.Rendements; 
    var bValues=thisOplModel.bValues;
   var a =  thisOplModel.a;
   var k = thisOplModel.k;
   var x = thisOplModel.x;
    var s =thisOplModel.s;
    var yProbabilites=thisOplModel.yProbabilites;
	
writeln("Solve the portfolio problem with a varitation of the a ! : ");	
var stop = 10000;
while (stop!=0){


var portfolioSrc = new IloOplModelSource("CvarOptimisationMain.mod");
        var portfolioDef = new IloOplModelDefinition(portfolioSrc);
        var portfolio = new IloOplModel(portfolioDef,cplex);
        var portfolioData = new IloOplDataElements();
 
 
  portfolioData.Actifs = Actifs;
 portfolioData.Rendements = Rendements;
 portfolioData.R = R;
 portfolioData.a = a;
 //portfolioData.k = k;
  //portfolioData.x = x;
 portfolioData.s = s;
 portfolioData.yProbabilites = yProbabilites;
	portfolioData.bValues=bValues;
 portfolio.addDataSource(portfolioData);
portfolio.generate();

if (cplex.solve()) {
 //writeln(cplex.getObjValue());
 writeln(  portfolio.k);
   //writeln("x = ",  cplex.x);
   // writeln("__________________________");
   stop --;
}
else {
 stop=0;
}
R = R + 0.0001;
   


}

    portfolio.end();
portfolioData.end();
portfolioDef.end();
portfolioSrc.end();
  
    
  }    