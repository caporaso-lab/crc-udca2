#!/usr/bin/env python

import sys
import subprocess
import os.path
import os

if len(sys.argv) == 1:
    print "USAGE: %s feature-table-path bootstrap-iterations output-dir" % sys.argv[0]
    sys.exit(0)

sparcc_dir = os.path.expandvars("$HOME/bin/sparcc/")

feature_table_fp = sys.argv[1]
bootstrap_iterations = int(sys.argv[2])
output_dir = sys.argv[3]

def run_command(cmd, verbose=True, dry_run=False):
    """ This function is derived from:
    https://github.com/qiime2/q2-alignment/blob/fe3df48330777626380f5ba706fd6feda07525df/q2_alignment/_mafft.py
    """
    cmd = map(str, cmd)
    if verbose:
        print " ".join(cmd)
    if not dry_run: subprocess.check_call(cmd)

os.mkdir(output_dir)
correlations_fp = os.path.join(output_dir, "corr.out")

run_command(['%s/SparCC.py' % sparcc_dir, feature_table_fp, '-c', correlations_fp],
            verbose=True)

bootstrap_dir = os.path.join(output_dir, 'bootstraps/')
os.mkdir(bootstrap_dir)

run_command(["%s/MakeBootstraps.py" % sparcc_dir, feature_table_fp, "-t", "permutation_#.txt", "-p", bootstrap_dir, "-n", bootstrap_iterations],
            verbose=True)

for i in range(bootstrap_iterations):
    perm_feature_table_fp = os.path.join(bootstrap_dir, 'permutation_%d.txt' % i)
    perm_correlations_fp = os.path.join(bootstrap_dir, 'perm_cor_%d.txt' % i)
    run_command(['%s/SparCC.py' % sparcc_dir, perm_feature_table_fp, '-c', perm_correlations_fp], verbose=True)

pvalues_fp = os.path.join(output_dir, "p-value.out")
perm_correlations_pattern = os.path.join(bootstrap_dir, 'perm_cor_#.txt')

run_command(["%s/PseudoPvals.py" % sparcc_dir, correlations_fp, perm_correlations_pattern, bootstrap_iterations, "-o", pvalues_fp, "-t", "two_sided"], verbose=True)
