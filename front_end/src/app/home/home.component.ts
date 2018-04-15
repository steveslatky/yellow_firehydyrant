import { Component, OnInit } from '@angular/core';
import { JsonPipe } from '@angular/common';
import { Http } from '@angular/http';

declare var google: any;

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  lat = 39.9526;
  lng = -75.1652;
  mapRef;
  character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  markers = [];

  constructor(
    private http: Http,
  ) {

  };

  onMapReady(map){
    this.mapRef = map;
    this.mapRef.fitBounds(this.findStoresBounds());
  }

  findStoresBounds(){
    let bounds = new google.maps.LatLngBounds();
    if (this.markers.length <= 0) return;

    for (let marker of this.markers) {
      bounds.extend(
        new google.maps.LatLng(marker.lat, marker.lng));
    }

    return bounds;
  }

  getMarkers(loc) {
    this.http.get(`http://localhost:8081?location=${loc}`)
      .subscribe(res => {
        console.log('Response:', res.json());
        this.markers = res.json().data;
        this.mapRef.fitBounds(this.findStoresBounds());
      });
  }

  ngOnInit() {
  }

}
