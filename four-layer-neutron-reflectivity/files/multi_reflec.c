//
//  multi_reflec.c
//  NREFLEC
//
//  Created by Simon Martin on 16/10/2017.
//


//2 component vector to hold the real and imaginary parts of a complex number:
typedef double complex cfloat;

//#define I ((cfloat)(0.0, 1.0))
#define SLABS 4

#include <complex.h>

//double Iq(double q,double sld_cap,double t1,double sld1,double r1,double sld_s,double r_s);
double Iq(double q,
          double sld_cap,
          double sld1,double t1,double r1,
          double sld2,double t2,double r2,
          double sld3,double t3,double r3,
          double sld4,double t4,double r4,
          double sld_s,double r_s);

double complex fresnel(cfloat k1, cfloat k2, double rough);

double complex k_medium(cfloat qi,double sld_medium);




double Iq(double q,
          double sld_cap,
          double sld1,double t1,double r1,
          double sld2,double t2,double r2,
          double sld3,double t3,double r3,
          double sld4,double t4,double r4,
          double sld_s,double r_s)
{
    // arrays: space for each slab plus cap and substrate
    double sld_array[SLABS+2]   = {0.};    /* array of sld */
    double thick_array[SLABS+2] = {0.};  /* array of thickness */
    double rough_array[SLABS+2] = {0.};  /* array of roughness */
    double complex r_array[SLABS+2]     = {(double complex)(0.,0.)};      /* array of reflectivity terms*/
    double complex rn = (double complex)(0.,0.);  // fresnel term for nth layer
    double complex numer=(double complex)(0.,0.); // calculation numerator
    double complex denom=(double complex)(0.,0.); // calculation denominator
    int nlayers=SLABS; /*total layers in system */
    // set up arrays of sld etc
    // will need to update this code if/when other layers are added
    // parameters are not passed as block/list, so have to set up arrays row by ro
    sld_array[0]=sld_cap*1.e-6;
    sld_array[1]=sld1*1.e-6;
    sld_array[2]=sld2*1.e-6;
    sld_array[3]=sld3*1.e-6;
    sld_array[4]=sld4*1.e-6;
    sld_array[5]=sld_s*1.e-6;
    // set up array of thicknesses
    thick_array[0]=0.;
    thick_array[1]=t1;
    thick_array[2]=t2;
    thick_array[3]=t3;
    thick_array[4]=t4;
    thick_array[5]=0.;
    // array of roughness
    rough_array[0]=0.;
    rough_array[1]=r1;
    rough_array[2]=r2;
    rough_array[3]=r3;
    rough_array[4]=r4;
    rough_array[5]=r_s;
    double ko=q/2.; // external wavevector
    // calculate wavevector in capping medium
    double complex kcap=cabs(csqrt(ko*ko+4.*M_PI*sld_cap+4.*M_PI*I*0.));// add complex sld later
    
    r_array[nlayers+1]=(double complex)(0.,0.); // reflection term, builds up iteratively
    // no reflection from bulk of substrate
    double complex kzn=k_medium(kcap,sld_array[nlayers]);
    double complex kznp1=k_medium(kcap,sld_array[nlayers+1]);
    r_array[nlayers]=fresnel(kzn,kznp1,rough_array[nlayers+1]);
    for (int i=nlayers-1;i>=0;i--)
    {
        kzn   = k_medium(kcap,sld_array[i]);
        kznp1 = k_medium(kcap,sld_array[i+1]);
        rn    = fresnel(kzn,kznp1,rough_array[i+1]); // nth layer fresnel term
        //double complex delta=cmult_imag(kznp1,2.*thick_array[i+1]);
        double complex delta=kznp1*2.*I*thick_array[i+1];
        double complex expon=cexp(delta); //               exp(I*q*t)
        double complex rnexp=r_array[i+1]*expon;
        numer=rn+rnexp;
        denom=1.+rn*rnexp;
        
        r_array[i]=numer/denom;
        
        //numer=kznp1;
    }
    
    return (r_array[0]*conj(r_array[0]));
    //return c_abs2(numer);
}

double complex fresnel(double complex k1,double complex k2,double rough)
{
    //return c_exp(-0.5*q1*q2*rough*rough)*(q1-q2)/(q1+q2);
    double complex fres = (k1-k2)/(k1+k2);
    // now calculate effect of interface roughness (Nevot and Croce method)
    double complex kprod=k1*k2;
    double complex expon=kprod*(-2.)*rough*rough;
    return (fres*cexp(expon));
    
}

double complex k_medium(double complex k,double sld_medium)
{
    double complex term;
    double delta;
    delta= 4.*M_PI*sld_medium;
    double complex k2=(k*k);
    //cfloat term=cfloat(16.*M_PI*sld_medium,0.);
    term=(k2-delta);
    return csqrt(term);
}

