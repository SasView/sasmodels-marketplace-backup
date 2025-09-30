///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////

double Iq( double q, double I0,  double XI,  double Q0,  double M,  double P)
{
    return I0/pow(1.0+pow(fabs(q-Q0)*XI,M),P);
}
