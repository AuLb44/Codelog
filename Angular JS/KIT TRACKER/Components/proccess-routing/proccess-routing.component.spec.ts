import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProccessRoutingComponent } from './proccess-routing.component';

describe('ProccessRoutingComponent', () => {
  let component: ProccessRoutingComponent;
  let fixture: ComponentFixture<ProccessRoutingComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProccessRoutingComponent]
    });
    fixture = TestBed.createComponent(ProccessRoutingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
