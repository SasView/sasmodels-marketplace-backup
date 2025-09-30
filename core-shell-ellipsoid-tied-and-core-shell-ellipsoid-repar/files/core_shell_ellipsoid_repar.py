from numpy import inf

from sasmodels.core import reparameterize
# for full instructions see reparametrerize in sasmodels/sasmodels/core.py 


parameters = [

    # name, units, default, [min, max], type, description

    ["vol_dry_shell_over_core", "None",    0.75,   [0, inf],    "volume",         "volume ratio of dry shell to core"],

    ["sld_dry_shell",           "1e-6/Ang^2", 1,   [-inf, inf], "sld",      "Dry shell scattering length density"],

    ["f_solvent_in_shell",      "None",       0.3, [0.0, 0.99], "volume",      "Local volume fraction of solvent in wet shell"],

]

translation = """

    thick_shell = solve_shell_v3(radius_equat_core, x_core, vol_dry_shell_over_core, x_polar_shell, f_solvent_in_shell)

    sld_shell = f_solvent_in_shell*sld_solvent + (1-f_solvent_in_shell)*sld_dry_shell

    """
# *insert_after* controls parameter placement.  By default, the new
#    parameters replace the old parameters in their original position.
#    Instead, you can provide a dictionary *{'par': 'newpar1,newpar2'}*
#model_info = reparameterize('core_shell_ellipsoid', parameters, translation, __file__, source=['cubic_solve_reparam3.c'])
#
model_info = reparameterize('core_shell_ellipsoid', parameters, translation, __file__,insert_after=
{'x_core':'vol_dry_shell_over_core','sld_core':'sld_dry_shell','sld_solvent':'f_solvent_in_shell'},
source=['cubic_solve_reparam3.c'])

# Note: adding unit tests using the following:

model_info.tests = [
    # first replicate all five tests from core_shell_ellipsoid (used a separate spreadsheet and debug prints from cubic_solve)
    [{'radius_equat_core': 200.0,
      'x_core': 0.1,
      'vol_dry_shell_over_core':1.34375,
      #'thick_shell': 50.0,
      'x_polar_shell': 0.2,
      'sld_core': 2.0,
      'sld_dry_shell': 1.0,
      'sld_solvent': 6.3,
      'f_solvent_in_shell':0.0,
      'background': 0.001,
      'scale': 1.0,
     }, 1.0, 0.00189402],

    # tests with larger range of parameters as per core_shell_ellipsoid
    [{'radius_equat_core': 20.0,
      'x_core': 3.0,
      'vol_dry_shell_over_core':8.3751,
      #'thick_shell': 30.0,
      'x_polar_shell': 1.0,
      'sld_core': 2.0,
      'sld_dry_shell': 1.0,
      'sld_solvent': 6.3,
      'f_solvent_in_shell':0.0,
      'background': 0.01,
      'scale': 1.0,}, 0.1, 11.6915],

    [{'radius_equat_core': 20.0,
      'x_core': 200.0,
      'vol_dry_shell_over_core':13.2444500,
#      'thick_shell': 54.0, - this case has +ve determinant
      'x_polar_shell': 3.0,
      'sld_core': 20.0,
      'sld_dry_shell': 10.0,
      'sld_solvent': 6.0,
      'f_solvent_in_shell':0.0,
      'background': 0.0,
      'scale': 1.0,
     }, 0.01, 8688.53],

    # 2D tests  as per core_shell_ellipsoid
    [{'radius_equat_core': 20.0,
      'x_core': 3.0,
      'vol_dry_shell_over_core':8.375001,
      #'thick_shell': 30.0,
      'x_polar_shell': 1.0,
      'sld_core': 2.0,
      'sld_dry_shell': 1.0,
      'sld_solvent': 6.3,
      'f_solvent_in_shell':0.0,
      'background': 0.001,
      'theta': 90.0,
      'phi': 0.0,
     }, (0.4, 0.5), 0.00690673],

    [{'radius_equat_core': 20.0,
      'x_core': 200.0,
      'vol_dry_shell_over_core':13.2444500,
      #'thick_shell': 54.0,
      'x_polar_shell': 3.0,
      'sld_core': 20.0,
      'sld_dry_shell': 10.0,
      'sld_solvent': 6.0,
      'f_solvent_in_shell':0.0,
      'background': 0.01,
      'scale': 0.01,
      'theta': 90.0,
      'phi': 0.0,
     }, (0.0866025403, 0.05), 0.01000025],

     # 1D using new parameters - not checked by other means
    [{'radius_equat_core': 20.0,
      'x_core': 3.0,
      'vol_dry_shell_over_core':0.75,
#      'thick_shell': try 7.88356 with x-polar_shell=0.5 - this case has +ve determinant
      'x_polar_shell': 0.5,
      'sld_core': 2.0,
      'sld_dry_shell': 1.0,
      'sld_solvent': 6.3,
      'f_solvent_in_shell':0.3,
      'background': 0.01,
      'scale':0.1,
     }, 0.025, 26.45088379],
     # 1D using new parameters - not checked by other means
    [{'radius_equat_core': 20.0,
      'x_core': 3.0,
      'vol_dry_shell_over_core':8.0,
#      'thick_shell': try 50.0 with x-polar_shell=0.0 - this case is quadratic
      'x_polar_shell': 0.0,
      'sld_core': 2.0,
      'sld_dry_shell': 1.0,
      'sld_solvent': 6.3,
      'f_solvent_in_shell':0.2888889,
      'background': 0.01,
      'scale':0.1,
     }, 0.05, 11.83784036],
]



