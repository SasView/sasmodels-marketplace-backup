double form_volume(void);

double Iq(double q, double radius, double arms);

static double star_polymer_v2_kernel(double q, double radius, double arms)
{
// now using Rg not Rg^2, simplified to avoid two calcs of the exponential
    double u_2 = square(radius * q);
    double v = u_2 * arms / (3.0 * arms - 2.0);

    double term1 = expm1(-v);
    double term2 = ((arms - 1.0)/2.0) * square(term1);

    return (2.0 * (v + term1 + term2)) / (arms * v * v);

}

double form_volume(void)
{
    return 1.0;
}

double Iq(double q, double radius, double arms)
{
    return star_polymer_v2_kernel(q, radius, arms);
}
