#include"TApplication.h"
#include<string>
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<TROOT.h>
#include<TStyle.h>
#include<TGraph.h>
#include<TCanvas.h>
#include<TAxis.h>
#include<TMath.h>
#include<TH1.h>
#include<TF1.h>
#include<TGaxis.h>

int main(int argc, char **argv){

  TApplication theApp("App",&argc,argv);
  char filename[100];
  int j,N=500;
  Double_t a,b,x[N],px[N];

  std::ifstream data_file;
  sprintf(filename,"gamma-energy-spectrum.dat");
  data_file.open(filename);
  if(!data_file) {
    printf("file open error \n");
  }
  else{
    for(j=0;j<N;j++){
      data_file >> a;
      data_file >> b;
      x[j]=TMath::Log10(a);
      px[j]=TMath::Log10(b);
    }
  }
  data_file.close();
  TCanvas c1;

  //c1.SetLogy();
  //c1.SetLogx();
  TGraph *ehist=new TGraph(N,x,px);
  TF1 *espec=new TF1("es0","[0]*x**2.0+[1]*x+[2]",1,1000);
  ehist->Fit("es0");
  ehist->SetFillColor(kBlue);
  ehist->Draw("AB");
  theApp.Run();
  return 0;
}
