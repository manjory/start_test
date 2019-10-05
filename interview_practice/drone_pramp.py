# remaining_energy = 0
# min_energy_reqd = 0
# z_route = []
# position = 0
# for i in range(len(route)):
#     z_route.append(route[i][2])
# # for position in range(len(z_route)-1):
# if len(z_route) <= 1:
#     return 0
# while position < (len(z_route) - 1):
#     # min_energy_reqd = 0
#
#     if z_route[position] > z_route[position + 1]:
#         remaining_energy = remaining_energy + (z_route[position] - z_route[position + 1])
#         if remaining_energy < 0:
#             min_energy_reqd = min_energy_reqd - remaining_energy
#             if min_energy_reqd > 0:
#                 position = position + 1
#         # else:
#         #     min_energy_reqd=0
#     else:  # z_route[position]<z_route[position+1]:
#         remaining_energy = remaining_energy + (-z_route[position + 1] + z_route[position])
#         if remaining_energy < 0:
#             min_energy_reqd = min_energy_reqd - remaining_energy + (z_route[position + 1] - z_route[position])
#             if min_energy_reqd > 0:
#                 position = position + 1
#
#     position = position + 1
#     # else:
#     #     min_energy_reqd=0
# return (min_energy_reqd)
#
