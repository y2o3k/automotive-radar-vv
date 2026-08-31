
#range_m : 전방 객체까지의 거리 
#relative_velocity_mps < 0 : 접근중 
#relative_velocity_mps >= 0 : 충돌 방향으로 접근하지 않으므로 TTC는 계산하지 않음. 
#접근 중이면 TTC = range / closing speed 

def calculate_ttc(range_m, relative_velocity_mps):
  
  if relative_velocity_mps >= 0:
      return None
  return range_m / (-relative_velocity_mps)
