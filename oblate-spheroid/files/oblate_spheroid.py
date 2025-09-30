r"""
For information about polarised and magnetic scattering, see
the :ref:`magnetism` documentation.

Definition
----------

I made this up.

Validation
----------

Definitely not valid.

References
----------

I read it on Facebook.
"""

from numpy import inf

name = "oblate_spheroid"
title = "Spheres with uniform scattering length density"
description = """
P(q)=(scale/V)*[3V(sld-sld_solvent)*(sin(qr)-qr cos(qr))
                /(qr)^3]^2 + background
    r: radius of sphere
    V: The volume of the scatter
    sld: the SLD of the sphere
    sld_solvent: the SLD of the solvent
"""
category = "shape:sphere"

#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [["sld", "1e-6/Ang^2", 1, [-inf, inf], "sld",
               "Layer scattering length density"],
              ["sld_solvent", "1e-6/Ang^2", 6, [-inf, inf], "sld",
               "Solvent scattering length density"],
              ["radius", "Ang", 50, [0, inf], "volume",
               "Sphere radius"],
             ]

source = ["lib/sph_j1c.c", "lib/sphere_form.c"]

# No volume normalization despite having a volume parameter
# This should perhaps be volume normalized?
form_volume = """
    return sphere_volume(radius);
    """

Iq = """
    return sphere_form(q, radius, sld, sld_solvent);
    """

def ER(radius):
    """
    Return equivalent radius (ER)
    """
    return radius

# VR defaults to 1.0

demo = dict(scale=1, background=0,
            sld=6, sld_solvent=1,
            radius=120,
            radius_pd=.2, radius_pd_n=45)

tests = [
    [{}, 0.2, 0.726362],
    [{"scale": 1., "background": 0., "sld": 6., "sld_solvent": 1.,
      "radius": 120., "radius_pd": 0.2, "radius_pd_n":45},
     0.2, 0.228843],
    [{"radius": 120., "radius_pd": 0.2, "radius_pd_n":45}, "ER", 120.],
    [{"radius": 120., "radius_pd": 0.2, "radius_pd_n":45}, "VR", 1.],
]


