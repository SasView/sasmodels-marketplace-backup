//  Author: 
//    Martin Schmiele
//    Niels-Bohr-Institutet
//    Koebenhavns Universitet
//    martin.schmiele@nbi.ku.dk
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//
//
//
// (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((((((+++++++++++++(((((((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%++(((((((((((((((((((((((((((((
// ((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%%%%%%%%%%%++((((((((((((((((((((((((
// ((((((((((((((((((((++%%%%%%%%%%...............%%%%%%%%%%++((((((((((((((((((((
// (((((((((((((((((++%%%%%%%%...........%%%...........%%%%%%%%++(((((((((((((((((
// (((((((((((((((++%%%%%%..............%%%%%..............%%%%%%++(((((((((((((((
// (((((((((((((++%%%%%%...............%%%%%.................%%%%%%++(((((((((((((
// ((((((((((((++%%%%%.%%%%%.........%%%%%%....................%%%%%++((((((((((((
// ((((((((((++%%%%%...%%%%%%%%%%%..%%%%%%.......................%%%%%++((((((((((
// (((((((((++%%%%%...%%%%%%%%%%%%%%%%%%%.........................%%%%%++(((((((((
// ((((((((++%%%%%......%%%%%%%%%%%%%%%%%%%%%......................%%%%%++((((((((
// (((((((++%%%%%.............%%%%%%%%%%%%%%%%%%%%..................%%%%%++(((((((
// (((((((++%%%%................%%%%%%%%%%%%%%%%%%%%%%%%.............%%%%++(((((((
// ((((((++%%%%................%%%%%.....%%%%%%%%%%%%%%%%%%%%.........%%%%++((((((
// ((((((++%%%%..............%%%%%%....%%%%...%%%%%%%%%%%%%%%%%%%%%...%%%%++((((((
// ((((((++%%%%.............%%%%%%.....%%%%%%%%%....%%%%%%%%%%%%%%%%%%%%%%++((((((
// (((((++%%%%.............%%%%%......%%%%%%%%%%%%%%%%...%%%%%%%%%%%%..%%%%++(((((
// (((((++%%%%............%%%%%......%%%%%%%%%%%%%%%%..........%%%%%...%%%%++(((((
// ((((((++%%%%..........%%%%%......%%%%%%%%%%%%%%%%%.................%%%%++((((((
// ((((((++%%%%.........%%%%%.......%%%%%%%%%%%%%%%%..................%%%%++((((((
// ((((((++%%%%..........%%%.......%%%%%%%%%%%%%%%%...................%%%%++((((((
// (((((((++%%%%..................%%%%%%%%%%%%%%%%...................%%%%++(((((((
// (((((((++%%%%%.................%%%%%%%%%%%%%%%%..................%%%%%++(((((((
// ((((((((++%%%%%...............%%%%%%%%%%%%%%%%..................%%%%%++((((((((
// (((((((((++%%%%%.............%%%%%%%%%%%%%%%%..................%%%%%++(((((((((
// ((((((((((++%%%%%...........%%%%%%%%%%%%%%%%..................%%%%%++((((((((((
// ((((((((((((++%%%%%.........%%%%%%%%%%%%%%%%................%%%%%++((((((((((((
// (((((((((((((++%%%%%%......%%%%%%%%%%%%%%%%...............%%%%%%++(((((((((((((
// (((((((((((((((++%%%%%%...%%%%%%%%%%%%%%%%..............%%%%%%++(((((((((((((((
// (((((((((((((((((++%%%%%%%%.....%%%%%%%%%%..........%%%%%%%%++(((((((((((((((((
// ((((((((((((((((((((++%%%%%%%%%%.....%%%%......%%%%%%%%%%++((((((((((((((((((((
// ((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%%%%%%%%%%%++((((((((((((((((((((((((
// (((((((((((((((((((((((((((((++%%%%%%%%%%%%%%%%%++(((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((((((+++++++++++++(((((((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
// (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
//
//  Orientationally averaged form factor for a monodisperse spherical particle with a core-double-shell sphere structure, filled with circular cylinders in its core. Note that the platelets inside are monodisperse with a given radius_cylinder and length_cylinder. Their amount is controlled via the fit parameter volume fraction = N * V_cylinder/ V_shpere_core. The randomly distributed positions of the cylinders inside a sphere with radius radius_cylinder_avgsph within the core translates into a form amplitude for a sphere with radius 0 < radius_cylinder_avgsph < radius_sphere_core. Applying polydispersity to the cylinders means to have core-double-shell spheres with cylinders inside, which differ between spheres, but not within one sphere.

double form_volume(double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph) ;
// double volume_cylinder(double radius_cylinder, double length_cylinder) ;
double volume_sphere(double radius_sphere) ;
double fcyl(double q, double sn, double cn, double radius, double length) ;
double fsph(double qr) ;
double f(double q, double sn, double cn, double volfract_cyl, double sld_sphere_core, double sld_sphere_shell, double sld_sphere_shell_2, double sld_cyl, double sld_solv, double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph) ;
double Iq(double q, double volfract_cyl, double sld_sphere_core, double sld_sphere_shell, double sld_sphere_shell_2, double sld_cyl, double sld_solv, double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph) ;
double Iqxy(double qx, double qy, double volfract_cyl, double sld_sphere_core, double sld_sphere_shell, double sld_sphere_shell_2, double sld_cyl, double sld_solv, double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph, double theta, double phi) ;


// overall volume of particle [Ang^3]
// this function needs to include all volume-"unit-ed" i.e. geometrical parameters (see python file parameters list), no matter whether they are used or not !!!
double form_volume(double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph)
{
    return M_4PI_3 * cube( radius_sphere_core + thickness_sphere_shell + thickness_sphere_shell_2 ) ;
}


// volumes of shapes
// double volume_cylinder(double radius_cylinder, double length_cylinder) { return M_PI * radius_cylinder * radius_cylinder * length_cylinder ; }

double volume_sphere(double radius_sphere) { return M_4PI_3 * cube(radius_sphere) ; }


// form amplitudes of shapes

// cylinder
// lim(q->0) f_cyl(q,...) = 1
double fcyl(double q, double sn, double cn, double radius, double length)
{
    // precompute qr and qh to save time in the loop
    const double qr = q*radius ;
    const double qh = q*0.5*length ;
    // sas_2J1x_x includes factor 2
    return sas_2J1x_x( qr*sn ) * sas_sinx_x( qh*cn ) ;
}

// sphere
// lim(q->0) f_sph(q,...) = 1
double fsph(double x)
{
    return sas_3j1x_x( x ) ;
}


// form amplitude of composite particle
double f(double q, double sn, double cn, double volfract_cyl, double sld_sphere_core, double sld_sphere_shell, double sld_sphere_shell_2, double sld_cyl, double sld_solv, double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph)
{
    double total = 0.0 ;
    total += ( sld_sphere_shell_2 - sld_solv ) * volume_sphere( radius_sphere_core + thickness_sphere_shell + thickness_sphere_shell_2 ) * fsph( q * ( radius_sphere_core + thickness_sphere_shell + thickness_sphere_shell_2 ) ) ;
    total += ( sld_sphere_shell - sld_sphere_shell_2 ) * volume_sphere( radius_sphere_core + thickness_sphere_shell ) * fsph( q * ( radius_sphere_core + thickness_sphere_shell ) ) ;
    total += ( sld_sphere_core - sld_sphere_shell ) * volume_sphere( radius_sphere_core ) * fsph( q*radius_sphere_core ) ;
    total += ( sld_cyl - sld_sphere_core ) * fsph( q*radius_cylinder_avgsph ) * volfract_cyl * volume_sphere( radius_sphere_core ) * fcyl( q, sn, cn, radius_cylinder, length_cylinder) ;

    // if only one shell and sld_{cyl} == sld_{sph,sh} and R_{avgsph,cyl} = R_{sph,c} it simplifies to:
    // ...
    // const double radius_sphere = radius_sphere_core + thickness_sphere_shell ;
    // total += ( sld_sphere_shell - sld_solv ) * volume_sphere( radius_sphere ) * fsph( q * radius_sphere ) ;
    // total += ( sld_sphere_core - sld_sphere_shell ) * volume_sphere( radius_sphere_core ) * fsph( q*radius_sphere_core) * ( 1.0 -  volfract_cyl * fcyl( q, sn, cn, radius_cylinder, length_cylinder)) ;
    // ...

    return total ;
}


// orientational average of form factor
// F^2(q) = int_{0}^{pi/2} f^2(q,alpha) sin(alpha) dalpha, using 76 point integration scheme
double Iq(double q, double volfract_cyl, double sld_sphere_core, double sld_sphere_shell, double sld_sphere_shell_2, double sld_cyl, double sld_solv, double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph)
{
    // translate a point in [-1,1] to a point in [0, pi/2]
    const double zm = M_PI_4 ;
    const double zb = M_PI_4 ;

    double total = 0.0;
    for (int i=0; i<76 ;i++)
    {
        const double alpha = Gauss76Z[i]*zm + zb;
        double sn, cn; // slots to hold sincos function output
        SINCOS(alpha, sn, cn);
        total += Gauss76Wt[i] * square( f(q, sn, cn, volfract_cyl, sld_sphere_core, sld_sphere_shell, sld_sphere_shell_2, sld_cyl, sld_solv, radius_sphere_core, thickness_sphere_shell, thickness_sphere_shell_2, radius_cylinder, length_cylinder, radius_cylinder_avgsph) ) * sn ;
    }
    // note that sum_{i=1}^{76} Gauss76Wt[i] * sin( Gauss76Z[i]*zm + zb ) = 4 / Pi,
    // thus zm * sum_{i=1}^{76} Gauss76Wt[i] * sin( Gauss76Z[i]*zm + zb ) = 1
    total *= zm ;

    // [ DeltaSLD^2/V V^2] = (10^-6 Ang^-2)^2 * Ang^3 = 10^-12 Ang^-1 = 10^-4 cm^-1
    // [ DeltaSLD^2 V^2] = (10^-6 Ang^-2)^2 * Ang^6 = 10^-12 Ang^2 = 10^4 cm^2
    return 1.0e-4 * total ;

    // scaling with scale(volume fraction), background and normalization with whole particle volume (defined in form_volume) done by sasview
    // provide form_volume() function for normalization, has been done in many other models (core-(multi)-shell sphere or vesicles, although not used in C-code there as well)
}


double Iqxy(double qx, double qy, double volfract_cyl, double sld_sphere_core, double sld_sphere_shell, double sld_sphere_shell_2, double sld_cyl, double sld_solv, double radius_sphere_core, double thickness_sphere_shell, double thickness_sphere_shell_2, double radius_cylinder, double length_cylinder, double radius_cylinder_avgsph, double theta, double phi)
{
    double q, sin_alpha, cos_alpha;
    ORIENT_SYMMETRIC(qx, qy, theta, phi, q, sin_alpha, cos_alpha);
    //printf("sn: %g cn: %g
", sin_alpha, cos_alpha);
    return 1.0e-4 * square( f(q, sin_alpha, cos_alpha, volfract_cyl, sld_sphere_core, sld_sphere_shell, sld_sphere_shell_2, sld_cyl, sld_solv, radius_sphere_core, thickness_sphere_shell, thickness_sphere_shell_2, radius_cylinder, length_cylinder, radius_cylinder_avgsph) ) ;
}
