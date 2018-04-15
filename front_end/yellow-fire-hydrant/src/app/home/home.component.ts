import { Component, OnInit } from '@angular/core';
import { JsonPipe } from '@angular/common';

// https://github.com/SebastianM/angular-google-maps/issues/719

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  lat = 39.9526;
  lng = -75.1652;
  map;

  markers = [
    {
      label: 'A',
      lat: this.lat,
      lng: this.lng,
    },
    {
      label: 'B',
      lat: this.lat + 0.02,
      lng: this.lng - 0.01,
    },
    {
      label: 'C',
      lat: this.lat - 0.012,
      lng: this.lng - 0.01,
    },
    {
      label: 'D',
      lat: this.lat - 0.031,
      lng: this.lng + 0.011,
    },
    {
      label: 'E',
      lat: this.lat + 0.03,
      lng: this.lng + 0.04,
    },
  ];

  constructor() { }

  generateMarkers() {
  }

  onMapReady(map){
    this.mapRef = map;
    this.mapRef.fitBounds(this.findStoresBounds());
  }

  findStoresBounds(){
    let bounds: LatLngBounds = new google.maps.LatLngBounds();

    for(let marker of this.markers){
      bounds.extend(new google.maps.LatLng(marker.lat, marker.lng));
    }

    return bounds;
  }

  ngOnInit() {
  }

}
