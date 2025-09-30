//Updated: October 3, 2020 - Cleaning comments
//Updated: December 7, 2020 - Cleaning comments
//Updated: December 8, 2020 - Cleaning comments

double form_volume(double radius, double thick_rim, double thick_face, double length1, double length2);
double Iq(double q,
		  double radius,
		  double thick_rim,
		  double thick_face,
		  double methylene_length,
		  double methyl_length,
		  double methylene_sld,
		  double methyl_sld,
		  double face_sld,
		  double rim_sld,
		  double solvent_sld);


double Iqxy(double qx, double qy,
		    double radius,
		    double thick_rim,
		    double thick_face,
		    double methylene_length,
		    double methyl_length,
			double methylene_sld,
			double methyl_sld,
			double face_sld,
			double rim_sld,
			double solvent_sld,
			double theta,
			double phi);

double add(double a, double b)
{
	double sum;
	sum = 2.0*a + b;
	return sum;
}

double form_volume(double radius, double thick_rim, double thick_face, double length1, double length2)
{
	return M_PI*(radius+thick_rim)*(radius+thick_rim)*(2.0*length1+length2+2.0*thick_face);
}

static double
bicellemod_kernel(double qq,
              double rad,
              double radthick,
              double facthick,
			  double length1,
			  double halflength2,
              double rhol1,
			  double rhol2,
              double rhoh,
              double rhor,
              double rhosolv,
              double sin_alpha,
              double cos_alpha)

{
    double si1,si2,si3,be1,be2;
	const double dr1 = rhol1 - rhoh;
	const double dr2 = rhor - rhosolv;
	const double dr3 = rhoh - rhor;
	const double dr4 = rhol2 - rhol1;
// Core length is a generic variable for halfway from center to face, not the length of the core.
// Core radius does not include phospholipid heads.
	const double vol1 = M_PI*rad*rad*2.0*(length1+halflength2);
    const double vol2 = M_PI*(rad+radthick)*(rad+radthick)*2.0*(length1+halflength2+facthick);
    const double vol3 = M_PI*rad*rad*2.0*(length1+halflength2+facthick);
	const double vol4 = M_PI*rad*rad*(2.0*halflength2);
    double besarg1 = qq*rad*sin_alpha;
    double besarg2 = qq*(rad+radthick)*sin_alpha;
// Should take the difference between each core section and rim.
    double sinarg1 = qq*(length1+halflength2)*cos_alpha;
    double sinarg2 = qq*(length1+halflength2+facthick)*cos_alpha;
	double sinarg3 = qq*(halflength2)*cos_alpha;
    be1 = sas_2J1x_x(besarg1);
    be2 = sas_2J1x_x(besarg2);
    si1 = sas_sinx_x(sinarg1);
    si2 = sas_sinx_x(sinarg2);
	si3 = sas_sinx_x(sinarg3);

    const double t = vol1*dr1*si1*be1 +
                     vol2*dr2*si2*be2 +
                     vol3*dr3*si2*be1 +
					 vol4*dr4*si3*be1;

    const double retval = t*t*sin_alpha;

    return retval;

}

static double
bicelle_integration(double qq,
		double rad,
		double radthick,
		double facthick,
	    double length1,
		double length2,
		double rhol1,
	    double rhol2,
		double rhoh,
		double rhor,
		double rhosolv)
{
    // set up the integration end points
    const double uplim = M_PI_4;
	const double halflength2 = 0.5*length2;
    double summ = 0.0;
    for(int i=0;i<GAUSS_N;i++) {
        double alpha = (GAUSS_Z[i] + 1.0)*uplim;
        double sin_alpha, cos_alpha; // slots to hold sincos function output
        SINCOS(alpha, sin_alpha, cos_alpha);
        double yyy = GAUSS_W[i] * bicellemod_kernel(qq, rad, radthick, facthick,
												length1, halflength2, rhol1, rhol2,
												rhoh, rhor, rhosolv,
												sin_alpha, cos_alpha);
        summ += yyy;
    }

    // calculate value of integral to return
    double answer = uplim*summ;
    return answer;
}

static double
bicellemod_kernel_2d(double qx, double qy,
          double radius,
          double thick_rim,
          double thick_face,
          double methylene_length,
		  double methyl_length,
		  double methylene_sld,
		  double methyl_sld,
          double face_sld,
          double rim_sld,
          double solvent_sld,
          double theta,
          double phi)
{
    double q, sin_alpha, cos_alpha;
    ORIENT_SYMMETRIC(qx, qy, theta, phi, q, sin_alpha, cos_alpha);
	double answer = bicellemod_kernel(q, radius, thick_rim, thick_face,
		methylene_length, 0.5*methyl_length, methylene_sld, methyl_sld,
		face_sld, rim_sld, solvent_sld,
		sin_alpha, cos_alpha) / fabs(sin_alpha);

    answer *= 1.0e-4;

    return answer;
}

double Iq(double q,
		double radius,
		double thick_rim,
		double thick_face,
		double methylene_length,
	    double methyl_length,
		double methylene_sld,
		double methyl_sld,
		double face_sld,
		double rim_sld,
		double solvent_sld)
{
    double intensity = bicelle_integration(q, radius, thick_rim, thick_face,
                       methylene_length, methyl_length, methylene_sld, methyl_sld, face_sld, rim_sld, solvent_sld);
    return intensity*1.0e-4;
}


double Iqxy(double qx, double qy,
          double radius,
          double thick_rim,
          double thick_face,
          double methylene_length,
		  double methyl_length,
		  double methylene_sld,
		  double methyl_sld,
          double face_sld,
          double rim_sld,
          double solvent_sld,
          double theta,
          double phi)
{
    double intensity = bicellemod_kernel_2d(qx, qy,
                      radius,
                      thick_rim,
                      thick_face,
                      methylene_length,
					  methyl_length,
                      methylene_sld,
					  methyl_sld,
                      face_sld,
                      rim_sld,
                      solvent_sld,
                      theta,
                      phi);

    return intensity;
}