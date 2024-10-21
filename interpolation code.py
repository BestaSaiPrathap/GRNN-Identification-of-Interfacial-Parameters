import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

file_path = 'C:\\Users\\Dell\\Downloads\\example f vs u.csv'
data = pd.read_csv(file_path)

# Extracting displacement and force columns
displacement_values = data.iloc[:, 0].values
force_values = data.iloc[:, 1].values

# interpolation function (linear interpolation)
interpolator = interp1d(displacement_values, force_values, kind='linear', fill_value="extrapolate")

# new displacement points (from 0 to 0.06 mm, spaced by 0.0001 mm)
new_displacement_points = np.arange(0, 0.06, 0.0001)

new_force_values = interpolator(new_displacement_points)

# Set any negative force values to 0
new_force_values[new_force_values < 0] = 0

interpolated_df = pd.DataFrame({'Displacement': new_displacement_points, 'Force': new_force_values})

output_file_path = 'D:\\1.sem7\\BTP S\\btp after msem\\codes\\interpolated_sample_data.csv'  # Specify your output path
interpolated_df.to_csv(output_file_path, index=False)

print(f"Interpolated data saved to: {output_file_path}")
