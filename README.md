# Installing
Once all the dependencies are installed, `surface_analyses` can be installed
using `pip install .`.

## Optional dependencies
While most Python-based dependencies are installed by pip, some parts of `pep_patch_electrostatic` use additional software.

* APBS (https://github.com/Electrostatics/apbs) is used to create an electrostatic potential for `pep_patch_electrostatic` if none is provided by the user.
* ANARCI (https://github.com/oxpig/ANARCI) is needed to assign CDRs in `pep_patch_electrostatic`.

# Computing electrostatic surfaces
The `pep_patch_electrostatic` script can use APBS (https://github.com/Electrostatics/apbs) to compute an electrostatic potential.
It then creates a molecular surface and colors it by the potential, or searches
for positive and negative surface patches.

`pep_patch_electrostatic` is presented in "PEP-Patch: Electrostatics in Protein-Protein Recognition, Specificity and Antibody Developability".
To reproduce the values in the paper, use an input like the following:
```
pep_patch_electrostatic input.pdb --apbs_dir apbs --ply_out potential -o patches.csv
```
Additionally, you can use `--ply_cmap` to set the cmap for the (continuous) .ply file output, and `--pos_patch_cmap`
and `--neg_patch_cmap` to set the color map for the patch .ply files.

# Assigning hydrophobicity values
The `pep_patch_hydrophobic` script can use hydrophobicity scales to assign hydrophobicity
to proteins. Additionally, the `eisenberg` and `crippen` scales are
pre-defined. See Eisenberg and McLachlan (1986) or Wildman and Crippen (1999)
for references. Additionally, using `rdkit-crippen` will use a SMILES input to 
assign Crippen parameters using the RdKit (useful for small molecules).

## Examples
Visualize the hydrophobic potential on a non-protein molecule, using an
*ordered* mol2 file as reference:
```
pep_patch_hydrophobic PARM CRD --scale rdkit-crippen --mol2 ORDERED_MOL2FILE --out OUT.npz --ply_out $OUT.ply --potential --patches
```
