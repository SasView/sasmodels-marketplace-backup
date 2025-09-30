// tied core/shell ellipsoid, from core_shell_ellipsoid in 4.2.2, RKH 17/07/2019
// this needs a rewrite for v5 to give Fq and effective radius etc.
//
// Converted from Igor function gfn4, using the same pattern as ellipsoid
// for evaluating the parts of the integral.
//     FUNCTION gfn4:    CONTAINS F(Q,A,B,MU)**2  AS GIVEN
//                       BY (53) & (58-59) IN CHEN AND
//                       KOTLARCHYK REFERENCE
//
//       <OBLATE ELLIPSOID>
static double
_cs_ellipsoid_kernel(double qab, double qc,
    double equat_core, double polar_core,
    double equat_shell, double polar_shell,
    double sld_core_shell, double sld_shell_solvent)
{
    const double qr_core = sqrt(square(equat_core*qab) + square(polar_core*qc));
    const double si_core = sas_3j1x_x(qr_core);
    const double volume_core = M_4PI_3*equat_core*equat_core*polar_core;
    const double fq_core = si_core*volume_core*sld_core_shell;

    const double qr_shell = sqrt(square(equat_shell*qab) + square(polar_shell*qc));
    const double si_shell = sas_3j1x_x(qr_shell);
    const double volume_shell = M_4PI_3*equat_shell*equat_shell*polar_shell;
    const double fq_shell = si_shell*volume_shell*sld_shell_solvent;

    return fq_core + fq_shell;
}


static double
// compiler needs ALL params here to by of type "volume" in the .py definition, even though we may not really want to be 
// able to makle them all polydisperse.
form_volume(double radius_equat_core,
    double x_core,
    double vol_dry_shell_over_core,
    double x_polar_shell,
    double f_solvent_in_shell)
{
    // Now we have to set up and solve the one real root of a cubic equation for thick_shell
    const double thick_shell = solve_shell_v3(radius_equat_core, x_core, vol_dry_shell_over_core,
    x_polar_shell, f_solvent_in_shell);
    const double equat_shell = radius_equat_core + thick_shell;
    const double polar_shell = radius_equat_core*x_core + thick_shell*x_polar_shell;
    double vol = M_4PI_3*equat_shell*equat_shell*polar_shell;
    return vol;
}


static double
Iq(double q,
    double radius_equat_core,
    double x_core,
    double vol_dry_shell_over_core,
    double x_polar_shell,
    double core_sld,
    double dry_shell_sld,
    double solvent_sld,
    double f_solvent_in_shell)
{
    // sort out the parameterized sld
    const double shell_sld = f_solvent_in_shell*solvent_sld + (1-f_solvent_in_shell)*dry_shell_sld;
    const double sld_core_shell = core_sld - shell_sld;
    const double sld_shell_solvent = shell_sld - solvent_sld;
    // Now we have to set up and solve the one real root of a cubic equation for thick_shell
    const double thick_shell = solve_shell_v3(radius_equat_core, x_core, vol_dry_shell_over_core,
    x_polar_shell, f_solvent_in_shell);
    //printf(" thick_shell = %g
",thick_shell);
    // from here on is the same as the original core_shell_ellipsoid
    const double polar_core = radius_equat_core*x_core;
    const double equat_shell = radius_equat_core + thick_shell;
    const double polar_shell = radius_equat_core*x_core + thick_shell*x_polar_shell;

    // translate from [-1, 1] => [0, 1]
    const double m = 0.5;
    const double b = 0.5;
    double total = 0.0;     //initialize intergral
    for(int i=0;i<GAUSS_N;i++) {
        const double cos_theta = GAUSS_Z[i]*m + b;
        const double sin_theta = sqrt(1.0 - cos_theta*cos_theta);
        double fq = _cs_ellipsoid_kernel(q*sin_theta, q*cos_theta,
            radius_equat_core, polar_core,
            equat_shell, polar_shell,
            sld_core_shell, sld_shell_solvent);
        total += GAUSS_W[i] * fq * fq;
    }
    total *= m;

    // convert to [cm-1]
    return 1.0e-4 * total;
}

static double
Iqac(double qab, double qc,
    double radius_equat_core,
    double x_core,
    double vol_dry_shell_over_core,
    double x_polar_shell,
    double core_sld,
    double dry_shell_sld,
    double solvent_sld,
    double f_solvent_in_shell)
{
    // sort out the parameterized sld
    const double shell_sld = f_solvent_in_shell*solvent_sld + (1-f_solvent_in_shell)*dry_shell_sld;
    const double sld_core_shell = core_sld - shell_sld;
    const double sld_shell_solvent = shell_sld - solvent_sld;
    // Now we have to set up and solve the one real root of a cubic equation for thick_shell
    const double thick_shell = solve_shell_v3(radius_equat_core, x_core, vol_dry_shell_over_core,
    x_polar_shell, f_solvent_in_shell);
    // from here on is the same as the original core_shell_ellipsoid
    const double polar_core = radius_equat_core*x_core;
    const double equat_shell = radius_equat_core + thick_shell;
    const double polar_shell = radius_equat_core*x_core + thick_shell*x_polar_shell;

    double fq = _cs_ellipsoid_kernel(qab, qc,
                  radius_equat_core, polar_core,
                  equat_shell, polar_shell,
                  sld_core_shell, sld_shell_solvent);

    //convert to [cm-1]
    return 1.0e-4 * fq * fq;
}
