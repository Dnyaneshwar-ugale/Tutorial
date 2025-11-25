# Abaqus Python script - run with: abaqus python extract_odb.py <odb_path> [stepName] [frameIndex] [outdir]
from odbAccess import openOdb
import sys, os, csv

def write_displacements(frame, outpath):
    if 'U' not in frame.fieldOutputs.keys():
        print("No displacement field (U) in frame")
        return
    u = frame.fieldOutputs['U']
    with open(outpath, 'w', newline='') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(['nodeLabel', 'instance', 'u1', 'u2', 'u3'])
        for val in u.values:
            node_label = getattr(val, 'nodeLabel', None)
            inst = getattr(val, 'instanceName', '')
            data = val.data if isinstance(val.data, (list, tuple)) else (val.data,)
            writer.writerow([node_label, inst] + list(data))

def write_stresses(frame, outpath):
    if 'S' not in frame.fieldOutputs.keys():
        print("No stress field (S) in frame")
        return
    s = frame.fieldOutputs['S']
    with open(outpath, 'w', newline='') as csvf:
        writer = csv.writer(csvf)
        # Abaqus S data commonly has 6 components (S11,S22,S33,S12,S13,S23) or a stress/array
        writer.writerow(['elementLabel', 'instance', 'sectionPoint', 's11','s22','s33','s12','s13','s23'])
        for val in s.values:
            el_label = getattr(val, 'elementLabel', None)
            inst = getattr(val, 'instanceName', '')
            sp = getattr(val, 'sectionPoint', '')
            data = val.data if isinstance(val.data, (list, tuple)) else (val.data,)
            # Pad/truncate to 6 components for CSV
            arr = list(data) + [''] * max(0, 6 - len(data))
            writer.writerow([el_label, inst, sp] + arr[:6])

def main(odb_path, step_name=None, frame_index=None, outdir='.'):
    if not os.path.exists(odb_path):
        print("ODB file not found:", odb_path)
        return
    odb = openOdb(path=odb_path)
    step_keys = list(odb.steps.keys())
    if not step_keys:
        print("No steps in ODB")
        odb.close()
        return

    step_name = step_name if step_name else step_keys[-1]
    if step_name not in odb.steps:
        print("Step not found in ODB:", step_name)
        odb.close()
        return

    step = odb.steps[step_name]
    frames = step.frames
    if not frames:
        print("No frames in step", step_name)
        odb.close()
        return

    frame = frames[int(frame_index)] if frame_index is not None else frames[-1]

    os.makedirs(outdir, exist_ok=True)
    write_displacements(frame, os.path.join(outdir, 'displacements.csv'))
    write_stresses(frame, os.path.join(outdir, 'stresses.csv'))

    odb.close()
    print("Extraction finished. CSVs written to", os.path.abspath(outdir))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: abaqus python extract_odb.py <odb_path> [stepName] [frameIndex] [outdir]")
    else:
        main(*sys.argv[1:])


        # ...existing code...
# Abaqus Python script - run with: abaqus python extract_odb.py <odb_path> [stepName] [frameIndex] [outdir]
# Added: small CLI help and error exit codes
# ...existing code...
def main(odb_path, step_name=None, frame_index=None, outdir='.'):
    """Extract displacements and stresses. Writes CSV files to outdir."""
# ...existing code...