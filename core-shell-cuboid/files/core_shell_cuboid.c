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
//  Orientationally averaged form factor for a monodisperse core-shell cuboid.
//
//               ,p=.,,_                   
//             ,/l:]:::::77t==.,,_          
//          ,/5::::[::::::::::::::773==.,,_ 
//       ,/5:::::::{zps;;:::::::::::::::::ZL
//    ,/5::::::::;z$3EtttZZ5sws;;:::::::yEJ.
// ,/5:::::::::zEtt$3EtttttttttttZZQ@:yE::[ 
// J=775es;;;Z5tttt3EEtttttttttttt@E@/::::L 
//  L::::::@8N@@szj3EEtttttttttt@E3@E::::3L 
//  {::::::$ttttZ59Q@BgszjttttgE1ZZ3E::::{  
//  J::::::Jttttttt3EEZZ55B@@SE2K5t3L::::[  
//   L:::::JEttttt25E35Sz@zz$ttQttt$:::::L  
//   [::::::Ettt25EttttttttZV5U$szj$::::J.  
//   J::::::$t25Ettttttttttt$t31tt2Pwsz;]   
//    L:::::@5EtttttttttttttEt3[zZ:::::y`   
//    [:::/5?3Gszjtttttttttt$tJ@E:::::/     
//    J;z5:::::::775szjtttttEz@L:::::F      
//     *+z;::::::::::::73Gsg@EJ.:::yF       
//         `*+z;::::::::::::::{:::/`        
//              `*=z;:::::::::[::F          
//                   `*=c;::::[yF           
//                        `*=cE`            
//
double form_volume( double length, double thick_rim) ;
double Iq( double q, double core_sld, double rim_sld, double solvent_sld, double length, double thick_rim) ;
double Iqxy( double qx, double qy, double core_sld, double rim_sld, double solvent_sld, double length, double thick_rim, double theta, double phi, double psi) ;


double form_volume( double length, double thick_rim)
{
    // return length_a * length_b * length_c;
    return ( length + 2.0 * thick_rim ) * ( length + 2.0 * thick_rim ) * ( length + 2.0 * thick_rim ) ;
}


double Iq( double q, double core_sld, double rim_sld, double solvent_sld, double length, double thick_rim)
{
    const double l2 = 0.5 * length ;
    const double l2d = 0.5 * length + thick_rim ;

    const double muc = q * l2 ;
    const double mucs = q * l2d ;

    const double delta_rho_core_shell = core_sld - rim_sld ;
    const double delta_rho_shell_solvent = rim_sld - solvent_sld ;

    // outer integral for costhetaQ (with gauss points), integration limits = 0, 1
    double outer_total = 0; // initialize integral

    for( int i=0; i<76; i++)
    {
        const double costhetaQ = 0.5 * ( Gauss76Z[i] + 1.0 ) ;
        const double sinthetaQ = sqrt( 1.0 - costhetaQ * costhetaQ ) ;
        const double muc_proj = muc * sinthetaQ ;
        const double mucs_proj = mucs * sinthetaQ ;

        const double sic3 = 2.0 * l2 * sas_sinx_x( muc * costhetaQ ) ;
        const double sics3 = 2.0 * l2d * sas_sinx_x( mucs * costhetaQ ) ;

        // inner integral for phiQ (with gauss points), integration limits = 0, 1
        double inner_total = 0.0 ;

        for( int j=0; j<76; j++)
        {
            const double phiQ = M_PI_2 * 0.5 * ( Gauss76Z[j] + 1.0 ) ;
            double sinphiQ, cosphiQ ;
            SINCOS( phiQ, sinphiQ, cosphiQ) ;
            const double sic1 = 2.0 * l2 * sas_sinx_x( muc_proj * cosphiQ ) ;
            const double sic2 = 2.0 * l2 * sas_sinx_x( muc_proj * sinphiQ ) ;
            const double sics1 = 2.0 * l2d * sas_sinx_x( mucs_proj * cosphiQ ) ;
            const double sics2 = 2.0 * l2d * sas_sinx_x( mucs_proj * sinphiQ ) ;

            // last multiplicant could be pulled out
            const double f = delta_rho_core_shell * sic1 * sic2 * sic3 + delta_rho_shell_solvent * sics1 * sics2 * sics3 ;

            inner_total += Gauss76Wt[j] * f * f ;
        }
        // note that sum_{i=1}^{76} Gauss76Wt[i] * 1 = 2, thus normalize with 1/2
        inner_total *= 0.5;

        // now sum up the outer integral
        outer_total += Gauss76Wt[i] * inner_total ;
    }
    // note that sum_{i=1}^{76} Gauss76Wt[i] * 1 = 2, thus normalize with 1/2
    outer_total *= 0.5;

    // [ DeltaSLD^2/V V^2] = (10^-6 Ang^-2)^2 * Ang^3 = 10^-12 Ang^-1 = 10^-4 cm^-1
    // [ DeltaSLD^2 V^2] = (10^-6 Ang^-2)^2 * Ang^6 = 10^-12 Ang^2 = 10^4 cm^2
    return 1.0e-4 * outer_total ;

    // scaling with scale(volume fraction), background and normalization with whole particle volume done by sasview
    // provide form_volume() function for normalization, has been done in many other models (core-(multi)-shell sphere or vesicles, although not used in C-code there as well)
}


double Iqxy( double qx, double qy, double core_sld, double rim_sld, double solvent_sld, double length, double thick_rim, double theta, double phi, double psi)
{
    double q, cos_val_a, cos_val_b, cos_val_c ;
    ORIENT_ASYMMETRIC( qx, qy, theta, phi, psi, q, cos_val_c, cos_val_b, cos_val_a) ;

    const double l2 = 0.5 * length ;
    const double l2d = 0.5 * length + thick_rim ;

    const double muc = q * l2 ;
    const double mucs = q * l2d ;

    const double delta_rho_core_shell = core_sld - rim_sld ;
    const double delta_rho_shell_solvent = rim_sld - solvent_sld ;

    const double sic1 = 2.0 * l2 * sas_sinx_x( muc * cos_val_a ) ;
    const double sic2 = 2.0 * l2 * sas_sinx_x( muc * cos_val_b ) ;
    const double sic3 = 2.0 * l2 * sas_sinx_x( muc * cos_val_c ) ;
    const double sics1 = 2.0 * l2d * sas_sinx_x( mucs * cos_val_a ) ;
    const double sics2 = 2.0 * l2d * sas_sinx_x( mucs * cos_val_b ) ;
    const double sics3 = 2.0 * l2d * sas_sinx_x( mucs * cos_val_c ) ;

    const double f = delta_rho_core_shell * sic1 * sic2 * sic3 + delta_rho_shell_solvent * sics1 * sics2 * sics3 ;

    return 1.0e-4 * f * f ;
}
