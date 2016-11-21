#!python
import os
import re
import textwrap
import argparse

def tbss_2_reg_continue(args):
    tbss_dir = os.path.abspath(args.dir)
    FA_process_dir = os.path.join(tbss_dir, 'FA')
    commandFile = os.path.join(FA_process_dir, '.commands')

    FA_process_files = os.listdir(FA_process_dir)
    FA_process_reg_subjects = [x.split('_warp.msf')[0] for x in FA_process_files if x.endswith('_warp.msf')]


    with open(commandFile, 'r') as f:
        commands = f.readlines()

    lines_to_rerun = []
    for FA_process_reg_subject in FA_process_reg_subjects:
        FA_warp_msf_file = FA_process_reg_subject + '_warp.msf'
        with open(os.path.join(FA_process_dir, FA_warp_msf_file), 'r') as f:
            contents = f.read()
        if contents == '':
            lines_to_rerun.append(''.join([x for x in commands if FA_process_reg_subject in x]))

    print ''.join(lines_to_rerun)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            {codeName} : Continues running TBSS registration stage
            ========================================
            eg) {codeName} -d /Users/kevin/TBSS
            '''.format(codeName=os.path.basename(__file__))))
    parser.add_argument(
        '-d', '--dir',
        help='TBSS directory location, default=pwd',
        default=os.getcwd())
    args = parser.parse_args()

    tbss_2_reg_continue(args)
