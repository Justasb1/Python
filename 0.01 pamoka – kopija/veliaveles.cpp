#include <iostream>
#include <fstream>

using namespace  std;

void skaityti(int &R,  int &G, int &Z)

int main(){
    int R=0,G=0,Z=0;
    skaityti(R,G,Z);
    cout<<G;
    return 0;
}

void skaityti(int &R,  int &G, int &Z){

int n,kiekis;
string spalva;
ifstream fin("U1.txt");

fin>>n;
for(int i=0;i<n;i++){
    fin>>spalva>>kiekis;
    if(spalva=="G")G+=kiekis;
    else if (spalva=="R")R+=kiekis;
    else Z+=kiekis;
}
fin.close();
}


