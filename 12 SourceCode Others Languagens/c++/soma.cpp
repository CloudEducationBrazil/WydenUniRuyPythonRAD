#include <iostream>
#include <locale.h>

using namespace std;

int main(void){
  setlocale(LC_ALL, "Portuguese");
  double n1, n2, avarage;

  cout<< "Digite n�mero 1: "; cin>> n1;
  cout<< "Digite n�mero 2: "; cin>> n2;

  avarage = ( n1 + n2 ) / 2.0;
  cout<< "\nResultado = " << avarage << endl;
}
