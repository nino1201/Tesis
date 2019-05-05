
{
 gROOT->Reset();
 gROOT->SetStyle();
 gStyle->SetOptStat(00);
 ofstream outmatrix; ///creates output file

 outmatrix.open("CdTeEscalera2_20keV56.txt"); ///gives output file a name and opens it
 TString hname_raw1="RTPSPDoseHistos: Dose XY_merged"; ///looks for histogram name in .root fil

 TFile *f1=new TFile("CdTeEscalera2_20keV56.root"); ///selects .root file
 TH2D *h1= (TH2D *)f1->Get(hname_raw1); ///gets histogram

  for(i = 0; i < 256; i++){
    for(j = 0; j < 256; j++){
      double im1=h1->GetBinContent(i,j); ///gets the data in each matrix entri
      outmatrix<<" "<<im1; ///writes data in output file
    }
    outmatrix<<endl; ///when row ends, end line in .txt
  }


}
