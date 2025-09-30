static double
form_volume(double radius, double thick_rim, double thick_face, double length)
{
    return M_PI*square(radius+thick_rim)*(length+2.0*thick_face);
}

static double
bicelle_kernel(double qab,
    double qc,
    double lipid_radius,
    double tails_thick,
    double belt_thick,
    double heads_thick, 
    double tails_sld,
    double belt_sld, 
    double belt_solv,
    double heads_sld, 
    double heads_solv,
    double solvent_sld,
    double halflength
    )
{
    const double heads_sld_hy = heads_solv * solvent_sld + (1 - heads_solv) * heads_sld;
    const double belt_sld_hy = belt_solv * solvent_sld + (1 - belt_solv) * belt_sld;
    const double dr1 = tails_sld-heads_sld_hy;
    const double dr2 = belt_sld_hy-solvent_sld;
    const double dr3 = heads_sld_hy-belt_sld_hy;
    const double vol1 = M_PI*square(lipid_radius)*2.0*(halflength);
    const double vol2 = M_PI*square(lipid_radius+belt_thick)*2.0*(halflength+heads_thick);
    const double vol3 = M_PI*square(lipid_radius)*2.0*(halflength+heads_thick);

    const double be1 = sas_2J1x_x((lipid_radius)*qab);
    const double be2 = sas_2J1x_x((lipid_radius+belt_thick)*qab);
    const double si1 = sas_sinx_x((halflength)*qc);
    const double si2 = sas_sinx_x((halflength+heads_thick)*qc);

    const double t = vol1*dr1*si1*be1 +
                     vol2*dr2*si2*be2 +
                     vol3*dr3*si2*be1;

    return t;
}

static double
Iq(double q,
    double lipid_radius,
    double tails_thick,
    double belt_thick,
    double heads_thick, 
    double tails_sld,
    double belt_sld, 
    double belt_solv,
    double heads_sld, 
    double heads_solv,
    double solvent_sld)
{
    // set up the integration end points
    const double uplim = M_PI_4;
    const double halflength = 0.5*tails_thick;

    double total = 0.0;
    for(int i=0;i<GAUSS_N;i++) {
        double theta = (GAUSS_Z[i] + 1.0)*uplim;
        double sin_theta, cos_theta; // slots to hold sincos function output
        SINCOS(theta, sin_theta, cos_theta);
        double fq = bicelle_kernel(q*sin_theta, q*cos_theta, lipid_radius, tails_thick, 
            belt_thick, heads_thick, tails_sld, belt_sld, belt_solv, heads_sld, 
            heads_solv, solvent_sld, halflength);
        total += GAUSS_W[i]*fq*fq*sin_theta;
    }

    // calculate value of integral to return
    double answer = total*uplim;
    return 1.0e-4*answer;
}

static double
Iqac(double qab, double qc,
    double lipid_radius,
    double tails_thick,
    double belt_thick,
    double heads_thick, 
    double tails_sld,
    double belt_sld, 
    double belt_solv,
    double heads_sld, 
    double heads_solv,
    double solvent_sld)
{
    double fq = bicelle_kernel(qab, qc, lipid_radius, tails_thick, 
        belt_thick, heads_thick, tails_sld, belt_sld, belt_solv, heads_sld, 
        heads_solv, solvent_sld, 0.5*tails_thick);
    return 1.0e-4*fq*fq;
}