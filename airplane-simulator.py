import random
import datetime

minutes_per_step = 5

def ToTime(time_step_number):
  start_time_str = '2021-10-07 22:00:00'
  start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
  start_time += datetime.timedelta(minutes=minutes_per_step*time_step_number)
  return start_time

def ToTimeDelta(time_steps):
  return datetime.timedelta(minutes=minutes_per_step*time_steps)


class Airplane(object):
  max_flight_number_digits = 5
  digits = "ABCEFGHJKLMNPRTUWXY2346789"
  # 50% probability of new plane wanting to land.
  probability_of_wanting_to_land = 50

  def __init__(self):
    flight_number_digits = []
    for i in range(Airplane.max_flight_number_digits):
      flight_number_digits.append(random.choice(Airplane.digits))
    self.flight_number = "".join(flight_number_digits)
    self.wants_to_land = (random.randrange(100) <
                          Airplane.probability_of_wanting_to_land)


class Airport(object):

  num_runways = 2
  max_planes_added_per_time = 4
  
  def __init__(self):
    self.landing_queue = []
    self.takeoff_queue = []
    self.time_step = 0
    self.new_waiting_to_land = []
    self.new_waiting_to_takeoff = []
    self.new_done_landing = []
    self.new_done_takeoff = []
    self.total_done_landing = 0
    self.total_done_takeoff = 0
    self.total_time_waiting_to_land = 0
    self.total_time_waiting_to_takeoff = 0

  def AddPlanes(self):
    planes = random.randint(0, Airport.max_planes_added_per_time)
    for i in range(planes):
      a = Airplane()
      a.start_time = self.time_step
      if a.wants_to_land:
        self.new_waiting_to_land.append(a.flight_number)
        self.landing_queue.append(a)
      else:
        self.new_waiting_to_takeoff.append(a.flight_number)
        self.takeoff_queue.append(a)

  def LandPlane(self):
    if not self.landing_queue:
      # no planes waiting to land. Nothing to do.
      return
    self.runways_in_use += 1
    a = self.landing_queue.pop(0)
    self.new_done_landing.append(a.flight_number)
    self.total_done_landing += 1
    self.total_time_waiting_to_land += (self.time_step - a.start_time)

  def TakeOffPlane(self):
    if not self.takeoff_queue:
      # no planes waiting to takeoff. Nothing to do.
      return
    if self.runways_in_use >= Airport.num_runways:
      # no runways left. Nothing to do.
      return
    self.runways_in_use += 1
    a = self.takeoff_queue.pop(0)
    self.new_done_takeoff.append(a.flight_number)
    self.total_done_takeoff += 1
    self.total_time_waiting_to_takeoff += (self.time_step - a.start_time)
      
  def HandlePlanes(self):
    self.runways_in_use = 0
    for i in range(Airport.num_runways):
      self.LandPlane()
    for i in range(Airport.num_runways):
      self.TakeOffPlane()

  def DisplayCurrentStatus(self):
    print("Time: ", ToTime(self.time_step))
    print("new arrival: ", self.new_waiting_to_land)
    self.new_waiting_to_land = []
    print("total waiting to land: ", len(self.landing_queue))
    print("newly landed: ", self.new_done_landing)
    self.new_done_landing = []

    print("new departure: ", self.new_waiting_to_takeoff)
    self.new_waiting_to_takeoff = []
    print("total waiting to take off: ", len(self.takeoff_queue))
    print("newly done takeoff: ", self.new_done_takeoff)
    self.new_done_takeoff = []
    print()

  def DisplaySummaryOfHowLongPlanesWaited(self):
    print("Time: ", ToTime(self.time_step))
    print("Total done landing: ", self.total_done_landing)
    print("Avg time waiting to land: ",
          ToTimeDelta((1.0 * self.total_time_waiting_to_land) /
                      self.total_done_landing))
    print("Total done takeoff: ", self.total_done_takeoff)
    print("Avg time waiting to take off: ",
          ToTimeDelta((1.0 * self.total_time_waiting_to_takeoff) /
                      self.total_done_takeoff))

  def Run(self, num_time_steps):
    for time_step in range(num_time_steps):
      self.time_step = time_step
      self.AddPlanes()
      self.HandlePlanes()
      self.DisplayCurrentStatus()
    self.DisplaySummaryOfHowLongPlanesWaited();


if __name__ == "__main__":
  a = Airport()
  a.Run(122)
