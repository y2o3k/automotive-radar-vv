
#range_m : 전방 객체까지의 거리 
#ex)내 차 속도 30 m/s, 앞 차 10m/s ,상대속도(velocity) :-20m/s (내 차가 앞차 보다 10m/s 더 빠르기 때문에 둘 사이 거리가 초당 10m 씩 줄어든다.)
#relative_velocity_mps < 0 : 접근중 
#relative_velocity_mps >= 0 : 충돌 방향으로 접근하지 않으므로 TTC는 계산하지 않음. 
#접근 중이면 TTC = range / closing speed 

def calculate_ttc(range_m, relative_velocity_mps):
  
  if relative_velocity_mps >= 0:
      return None
  return range_m / (-relative_velocity_mps)
