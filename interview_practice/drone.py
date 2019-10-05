def calc_drone_min_energy(route):
  current_energy=0
  min_energy_required=0
  for row in range(1,len(route)):
    if min_energy_required > current_energy:
      min_energy_required = current_energy
      current_energy=0
      if row<=len(route):
          current_energy = current_energy + route[row-1][2] - route[row][2] + min_energy_required
          min_energy_required=current_energy

    else:
        current_energy=current_energy+ route[row-1][2]-route[row][2]+min_energy_required
  return (-1*min_energy_required)
route =  [[0,   2, 10],
          [3,   5,  0],
          [9,  20,  6],
          [10, 12, 15],
          [10, 12, 27],
          [10, 10, 30]]

print(calc_drone_min_energy(route))