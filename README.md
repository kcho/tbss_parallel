# tbss_parallel

For use in the multicore computers without SGE setting.
Uses GNU parallel to dispatch jobs in parallel.

## Dependency
- FSL : http://fsl.fmrib.ox.ac.uk/fsl/fslwiki
- GNU parallel : https://www.gnu.org/software/parallel


## Usage

1. git clone

```
cd ~/
git clone https://github.com/kcho/tbss_parallel
```

2. add path

```
export PATH=tbss_parallel:${PATH}
```

* you can add this to ~/.bashrc or ~/.bash_profile



3. Use scripts

```
cd ~/FA_collection
tbss_1_preproc_parallel *
tbss_2_reg_parallel -n
```
