# nanodisc_simple

This is a simple model that loads the built-in "core_shell_bicelle" model and re-defines its fit parameters in molecular terms. For example, you would specify the number of lipids, number of belt proteins, and sum of scattering lengths for a lipid molecule and a belt protein molecule. The numbers of molecules should be used as fit parameters, whereas the sum of scattering lengths for each molecule would normally be held fixed (e.g. you know what kind of lipids you used, so there wouldn't be a need to "fit" this). This model will then use these parameters, combined with the volumes of the disc core, face, and rim, to calculate the SLDs of each part of the disc. Finally, the SLDs and geometric parameters are fed to the "core_shell_bicelle" model for the actual scattering calculations. SLDs are fixed during polydispersity calculations. For example, if you include radial polydispersity, the SLDs will be calculated based on the *average* radius, and then held fixed for the discs with a distribution of radii about the average.

This is a simple model that loads the built-in "core_shell_bicelle" model and re-defines its fit parameters in molecular terms. For example, you would specify the number of lipids, number of belt proteins, and sum of scattering lengths for a lipid molecule and a belt protein molecule. The numbers of molecules should be used as fit parameters, whereas the sum of scattering lengths for each molecule would normally be held fixed (e.g. you know what kind of lipids you used, so there wouldn't be a need to "fit" this). This model will then use these parameters, combined with the volumes of the disc core, face, and rim, to calculate the SLDs of each part of the disc. Finally, the SLDs and geometric parameters are fed to the "core_shell_bicelle" model for the actual scattering calculations.

SLDs are fixed during polydispersity calculations. For example, if you include radial polydispersity, the SLDs will be calculated based on the *average* radius, and then held fixed for the discs with a distribution of radii about the average.

# Example Data:

Source: https://marketplace.sasview.org/models/86/
