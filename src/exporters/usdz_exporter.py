import subprocess

from src.exporters.obj_exporter import obj_exporter


def usdz_exporter(export_path):
    obj_export_path = export_path
    output_usdz = export_path + ".usdz"

    obj_exporter(obj_export_path)
    try:
        subprocess.run(['xcrun', 'usdz_converter', obj_export_path, output_usdz], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during USDZ conversion: {str(e)}")
