class TripsController < ApplicationController
  def index
    success = @trips.any? { |(name, place, date)|
      place.downcase == "campus"
    }

    @flag = `./getflag` if success
  end
end
