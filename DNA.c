#include <stdio.h>
#include <stdlib.h>
#include "ods.h"

int main() {
  // Initialize ODS
  ods_init();

  // Create a new design
  ods_design_t *design = ods_design_new("dna_helix");

  // Define the DNA helix parameters
  double pitch = 3.4; // nm
  int n_helix = 2;
  int n_steps = 50;

  // Add the helices to the design
  for (int i = 0; i < n_helix; i++) {
    ods_helix_t *helix = ods_helix_new(pitch, n_steps);
    ods_design_add_helix(design, helix);
  }

  // Add staples to the design
  ods_staple_t *staple = ods_staple_new("5'-GGGTTAAGGGTTAAGGGTTAAGGGT-3'");
  ods_design_add_staple(design, staple, 0, 0, 1);
  ods_staple_t *staple2 = ods_staple_new("5'-CCCTTAACCCTTAACCCTTAACCCT-3'");
  ods_design_add_staple(design, staple2, 1, 0, 1);

  // Generate the design
  ods_generate(design);

  // Write the design to a PDB file
  ods_write_pdb(design, "dna_helix.pdb");

  // Clean up
  ods_design_free(design);
  ods_cleanup();

  return 0;
}