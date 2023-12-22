from dataclasses import dataclass
import asyncio
import winsdk.windows.devices.geolocation as geolocation

@dataclass(slots=True, frozen=True) 
class Coordinates:
  latitude: float
  longitude: float

async def get_gps_coordinates() -> Coordinates:

  geolocator = geolocation.Geolocator()

  try:
    position = await geolocator.get_geoposition_async()
  except Exception as e:
    print("Error getting location: ", e)
    return None

  if position:
    return Coordinates(latitude=position.coordinate.latitude,  
                       longitude=position.coordinate.longitude)
  else:
    return None

if __name__ == '__main__':

  async def main():
    coords = await get_gps_coordinates()
    if coords:
      print(f"Latitude: {coords.latitude}")
      print(f"Longitude: {coords.longitude}") 
    else:
      print("Could not determine coordinates")

  asyncio.run(main())