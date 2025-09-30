static double
form_volume(double radius, double thickness)
{
    return M_4PI_3 * cube(radius + thickness);
}

static double Iq(double q, double NormalizationRadius, double sld_core, double sld_magcore, double sld_shell, double sld_magshell, double sld_solvent, double radius_core, 
double thickness_shell, int MVar, double Length, double ViewingAngle, double sigma, double Singlets, double Doubles, double Trimers, double Quadramers, double Pentamers)
{
    const double bes = sas_3j1x_x(q*radius_core);
    double volume_core = M_4PI_3 * cube(radius_core);
    double total_radius = radius_core + thickness_shell;
    double volume_total = M_4PI_3 * cube(total_radius);
    double volume_shell = volume_total - volume_core;
    
    double AmpR1 = sas_3j1x_x(q*radius_core)*(volume_core)/3.0;
    double AmpR2 = sas_3j1x_x(q*(total_radius))*(volume_shell)/3.0;
    double Amp = ((sld_core - sld_solvent)*AmpR1 + (sld_shell - sld_solvent)*(AmpR2-AmpR1));
    double MAmp = (sld_magcore)*AmpR1 + (sld_magshell)*(AmpR2-AmpR1);

    double VolumeFraction = 1.0;
    double SingletFraction = Singlets;
    double DimerFraction = Doubles;
    double TrimerFraction = Trimers;
    double QuadramerFraction = Quadramers;
    double PentamerFraction = Pentamers;

    double PiNum = 2.0*acos(0);
    double radius_total = radius_core + thickness_shell;
    double Vol = (4.0*PiNum/3.0)*pow(NormalizationRadius,3);
    if(Vol == 0){Vol = 1E-10;}

    double Norm = 0.0;
    double angle, variable1, variable2;
    for(int a=0; a<45; a++){
        for(int b=0; b<3; b++){
            angle = (a*2.0+1.0)*PiNum/180.0;
            variable1 = (a*2.0+1.0 - 0.0)/sigma;
            variable2 = sqrt(4.0*acos(0))*sigma;
            Norm = Norm + exp( -0.5*pow( variable1,2) ) / variable2;
        }
    }

    double SingletIntensity = 0;
    double MSingletIntensity = 0;
    double DimerIntensity = 0;
    double MDimerIntensity = 0;
    double TrimerIntensity = 0;
    double MTrimerIntensity = 0;
    double QuadramerIntensity = 0;
    double MQuadramerIntensity = 0;
    double PentamerIntensity = 0;
    double MPentamerIntensity = 0;
    double Q_X = q*cos(ViewingAngle*PiNum/180.0);
    double Q_Y = q*sin(ViewingAngle*PiNum/180.0);

    double anglewt;
    for(int a=0; a<45; a++){
        for(int b=0; b<3; b++){
            angle = (a*2.0+1.0)*PiNum/180.0;
            double phi = (b*45.0)*PiNum/180.0;
            variable1 = (a*2.0+1.0 - 0.0)/sigma;
            variable2 = sqrt(4.0*acos(0))*sigma;
            anglewt = (exp( -0.5*pow( variable1,2) ) / variable2)/Norm;

            double ChainProjX = cos(angle);
            double ChainProjY = sin(angle)*cos(phi);
            double ChainProjZ = sin(angle)*sin(phi);

            SingletIntensity  += anglewt*pow(Amp,2)/Vol;
            if(MVar <= 1){
                MSingletIntensity  += (2.0/3.0)*anglewt*pow(MAmp,2)/Vol;}
            if(MVar < 3 && MVar > 1){
                MSingletIntensity  +=  pow(sin(angle - ViewingAngle*PiNum/180.0),2)*anglewt*pow(MAmp,2)/Vol;}
            if(MVar >= 3){
                MSingletIntensity  +=  pow(sin(ViewingAngle*PiNum/180.0),2)*anglewt*pow(MAmp,2)/Vol;}

            double real_phase = 1.0;
            double img_phase = 0.0;
            double mreal_phase = 1.0;
            double mimg_phase = 0.0;

            if(MVar < 3 && MVar > 1){mreal_phase = sin(angle - ViewingAngle*PiNum/180.0);}
            if(MVar >= 3){mreal_phase = sin(ViewingAngle*PiNum/180.0);}

            for(int k=1; k<5; k++){
                real_phase += cos(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                img_phase += sin(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                if(MVar < 3 && MVar > 1){
                    mreal_phase += sin(angle - ViewingAngle*PiNum/180.0)*cos(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                    mimg_phase += sin(angle - ViewingAngle*PiNum/180.0)*sin(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                }
                if(MVar >= 3){
                    mreal_phase += sin(ViewingAngle*PiNum/180.0)*cos(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                    mimg_phase += sin(ViewingAngle*PiNum/180.0)*sin(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                }
            if(k==1){
            DimerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(2.0*Vol);
            MDimerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(2.0*Vol);
            }
            if(k==2){
            TrimerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(3.0*Vol);
            MTrimerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(3.0*Vol);
            }
            if(k==3){
            QuadramerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(4.0*Vol);
            MQuadramerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(4.0*Vol);
            }
            if(k==4){
            PentamerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(5.0*Vol);
            MPentamerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(5.0*Vol);
            }
            }//end k loop for dimers
       }
    }

    double FractionScale = SingletFraction + DimerFraction + TrimerFraction + QuadramerFraction + PentamerFraction;
    if(FractionScale == 0){FractionScale = 1.0;}

    double SIntensity = SingletFraction*SingletIntensity + DimerFraction*DimerIntensity + TrimerFraction*TrimerIntensity + QuadramerFraction*QuadramerIntensity + PentamerFraction*PentamerIntensity;
    double MIntensity = 0.0;
    if(MVar <= 1){
        MIntensity = MSingletIntensity*(SingletFraction + DimerFraction + TrimerFraction + QuadramerFraction + PentamerFraction);
    }
    else{
        MIntensity = SingletFraction*MSingletIntensity + DimerFraction*MDimerIntensity + TrimerFraction*MTrimerIntensity + QuadramerFraction*MQuadramerIntensity + PentamerFraction*MPentamerIntensity;
    }

    double Intensity = (SIntensity+MIntensity)*(1E4)/FractionScale;

    return Intensity;
}

static double Iqxy(double x, double y, double NormalizationRadius, double sld_core, double sld_magcore, double sld_shell, double sld_magshell, double sld_solvent, double radius_core, 
double thickness_shell, int MVar, double Length, double ViewingAngle, double sigma, double Singlets, double Doubles, double Trimers, double Quadramers, double Pentamers)
{

    double PiNum = 2.0*acos(0);
    double Q_X = x;
    double Q_Y = y;
    double q = sqrt(x*x + y*y);
    double ViewingAngle = atan(y/x)*180.0/PiNum;

    const double bes = sas_3j1x_x(q*radius_core);
    double volume_core = M_4PI_3 * cube(radius_core);
    double total_radius = radius_core + thickness_shell;
    double volume_total = M_4PI_3 * cube(total_radius);
    double volume_shell = volume_total - volume_core;
    
    double AmpR1 = sas_3j1x_x(q*radius_core)*(volume_core)/3.0;
    double AmpR2 = sas_3j1x_x(q*(total_radius))*(volume_shell)/3.0;
    double Amp = ((sld_core - sld_solvent)*AmpR1 + (sld_shell - sld_solvent)*(AmpR2-AmpR1));
    double MAmp = (sld_magcore)*AmpR1 + (sld_magshell)*(AmpR2-AmpR1);

    double VolumeFraction = 1.0;
    double SingletFraction = Singlets;
    double DimerFraction = Doubles;
    double TrimerFraction = Trimers;
    double QuadramerFraction = Quadramers;
    double PentamerFraction = Pentamers;

    double radius_total = radius_core + thickness_shell;
    double Vol = (4.0*PiNum/3.0)*pow(NormalizationRadius,3);
    if(Vol == 0){Vol = 1E-10;}

    double Norm = 0.0;
    double angle, variable1, variable2;
    for(int a=0; a<45; a++){
        for(int b=0; b<3; b++){
            angle = (a*2.0+1.0)*PiNum/180.0;
            variable1 = (a*2.0+1.0 - 0.0)/sigma;
            variable2 = sqrt(4.0*acos(0))*sigma;
            Norm = Norm + exp( -0.5*pow( variable1,2) ) / variable2;
        }
    }

    double SingletIntensity = 0;
    double MSingletIntensity = 0;
    double DimerIntensity = 0;
    double MDimerIntensity = 0;
    double TrimerIntensity = 0;
    double MTrimerIntensity = 0;
    double QuadramerIntensity = 0;
    double MQuadramerIntensity = 0;
    double PentamerIntensity = 0;
    double MPentamerIntensity = 0;

    double anglewt;
    for(int a=0; a<45; a++){
        for(int b=0; b<3; b++){
            angle = (a*2.0+1.0)*PiNum/180.0;
            double phi = (b*45.0)*PiNum/180.0;
            variable1 = (a*2.0+1.0 - 0.0)/sigma;
            variable2 = sqrt(4.0*acos(0))*sigma;
            anglewt = (exp( -0.5*pow( variable1,2) ) / variable2)/Norm;

            double ChainProjX = cos(angle);
            double ChainProjY = sin(angle)*cos(phi);
            double ChainProjZ = sin(angle)*sin(phi);

            SingletIntensity  += anglewt*pow(Amp,2)/Vol;
            if(MVar <= 1){
                MSingletIntensity  += (2.0/3.0)*anglewt*pow(MAmp,2)/Vol;}
            if(MVar < 3 && MVar > 1){
                MSingletIntensity  +=  pow(sin(angle - ViewingAngle*PiNum/180.0),2)*anglewt*pow(MAmp,2)/Vol;}
            if(MVar >= 3){
                MSingletIntensity  +=  pow(sin(ViewingAngle*PiNum/180.0),2)*anglewt*pow(MAmp,2)/Vol;}

            double real_phase = 1.0;
            double img_phase = 0.0;
            double mreal_phase = 1.0;
            double mimg_phase = 0.0;

            if(MVar < 3 && MVar > 1){mreal_phase = sin(angle - ViewingAngle*PiNum/180.0);}
            if(MVar >= 3){mreal_phase = sin(ViewingAngle*PiNum/180.0);}

            for(int k=1; k<5; k++){
                real_phase += cos(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                img_phase += sin(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                if(MVar < 3 && MVar > 1){
                    mreal_phase += sin(angle - ViewingAngle*PiNum/180.0)*cos(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                    mimg_phase += sin(angle - ViewingAngle*PiNum/180.0)*sin(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                }
                if(MVar >= 3){
                    mreal_phase += sin(ViewingAngle*PiNum/180.0)*cos(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                    mimg_phase += sin(ViewingAngle*PiNum/180.0)*sin(k*Length*(Q_X*ChainProjX + Q_Y*ChainProjY));
                }
            if(k==1){
            DimerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(2.0*Vol);
            MDimerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(2.0*Vol);
            }
            if(k==2){
            TrimerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(3.0*Vol);
            MTrimerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(3.0*Vol);
            }
            if(k==3){
            QuadramerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(4.0*Vol);
            MQuadramerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(4.0*Vol);
            }
            if(k==4){
            PentamerIntensity  += anglewt*(pow(Amp*real_phase,2) + pow(Amp*img_phase,2))/(5.0*Vol);
            MPentamerIntensity  += anglewt*(pow(MAmp*mreal_phase,2) + pow(MAmp*mimg_phase,2))/(5.0*Vol);
            }
            }//end k loop for dimers
       }
    }

    double FractionScale = SingletFraction + DimerFraction + TrimerFraction + QuadramerFraction + PentamerFraction;
    if(FractionScale == 0){FractionScale = 1.0;}

    double SIntensity = SingletFraction*SingletIntensity + DimerFraction*DimerIntensity + TrimerFraction*TrimerIntensity + QuadramerFraction*QuadramerIntensity + PentamerFraction*PentamerIntensity;
    double MIntensity = 0.0;
    if(MVar <= 1){
        MIntensity = MSingletIntensity*(SingletFraction + DimerFraction + TrimerFraction + QuadramerFraction + PentamerFraction);
    }
    else{
        MIntensity = SingletFraction*MSingletIntensity + DimerFraction*MDimerIntensity + TrimerFraction*MTrimerIntensity + QuadramerFraction*MQuadramerIntensity + PentamerFraction*MPentamerIntensity;
    }

    double Intensity = (SIntensity+MIntensity)*(1E4)/FractionScale;

    return Intensity;
}
