# coding: utf-8
class DestinationsController < ApplicationController
  skip_before_action :verify_authenticity_token
  PLACES = %w{ venice london paris }

  def root
    redirect_to '/index.html'
  end

  def index
    @id = params[:id]
    if @id
      render file: 'destinations/' + @id
    end
  end

  def book
    @name = params[:name]
    @destination = params[:destination]
    @date = params[:date]

    unless PLACES.include? @destination
      render plain: "La destination demandé n'est pas disponible en ce moment. Les destinations suivantes sont disponibles: " + PLACES.join(", ") + "."
    else
      @trips << [@name, @destination, @date]
      save_trips

      flash[:notice] = 'Votre voyage a été créé avec succès!'

      redirect_to '/trips'
    end
  end
end
